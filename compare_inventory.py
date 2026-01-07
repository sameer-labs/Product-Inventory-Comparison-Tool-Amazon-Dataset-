import os
import csv

base_dir = os.path.dirname(os.path.abspath(__file__))

Day1_file = os.path.join(base_dir, "data", "inventory_day1.csv")
Day2_file= os.path.join(base_dir, "data", "inventory_day2.csv")
output_dir = os.path.join(base_dir, "output")

os.makedirs(output_dir, exist_ok=True)

changes_file = os.path.join(output_dir, "inventory_changes.csv")
summary_file = os.path.join(output_dir, "summary.txt")

key_field = "product_id"
price_field = "discounted_price"

# ------------ #
# CSV INTO DICT
# ------------ #

def load_inventory(path):
    inventory = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            inventory[row[key_field]] = row
    return inventory

day1 = load_inventory(Day1_file)
day2 = load_inventory(Day2_file)

day1_ids = set(day1.keys())
day2_ids = set(day2.keys())

# ------------ #
# DETECT CHANGES
# ------------ #

added = day2_ids - day1_ids
removed = day1_ids - day2_ids
common = day1_ids & day2_ids

price_changes = []

for pid in common:
    if day1[pid][price_field] != day2[pid][price_field]:
        price_changes.append({
            "product_id": pid,
            "old_price": day1[pid][price_field],
            "new_price": day2[pid][price_field]
            })
   
# ------------ #
# WRITE CSV CHANGES
# ------------ #

with open(changes_file, "w", newline="", encoding="utf-8") as f:
    fieldnames = ["change_type", "product_id", "old_price", "new_price"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    for pid in added:
        writer.writerow({
            "change_type": "ADDED",
            "product_id": pid,
            "old_price": "",
            "new_price": day2[pid][price_field]
        })

    for pid in removed:
        writer.writerow({
            "change_type": "REMOVED",
            "product_id": pid,
            "old_price": day1[pid][price_field],
            "new_price": ""
        })

    for change in price_changes:
        writer.writerow({
            "change_type": "PRICE_CHANGED",
            "product_id": change["product_id"],
            "old_price": change["old_price"],
            "new_price": change["new_price"]
        })
    
# ------------ #
# WRITE SUMMARY
# ------------ #

with open(summary_file, "w") as f:
    f.write("INVENTORY CHANGE SUMMARY\n")
    f.write("=" * 30 + "\n\n")
    f.write(f"Products added: {len(added)}\n")
    f.write(f"Products removed: {len(removed)}\n")
    f.write(f"Price changes: {len(price_changes)}\n")

print("Comparison complete.")
print("- inventory_changes.csv")
print("- summary.txt")