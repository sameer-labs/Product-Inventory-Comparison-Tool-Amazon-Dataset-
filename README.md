# Amazon Inventory Change Tracker

## Overview
This project compares two snapshots of Amazon-style product inventory data to identify what changed between them.

It detects:
- Products that were added
- Products that were removed
- Products with price changes

The output is a clean, easy-to-review change report and summary, suitable for inventory tracking, pricing audits, or operational monitoring.

---

## Dataset
The project utilises an Amazon product inventory dataset that contains product identifiers, pricing information, and product metadata.

Since real-world comparison datasets are rarely provided in multiple versions, a snapshot generation step was used to simulate inventory changes over time.

---

## How It Works

1. A single source CSV is used to generate two inventory snapshots:
   - `inventory_day1.csv` (baseline)
   - `inventory_day2.csv` (updated)

2. The comparison script:
   - Matches products using `product_id`
   - Detects added and removed products
   - Identifies price changes for existing products

3. Results are written to:
   - A detailed CSV change log
   - A plain-text summary file

---

## Project Structure

CSV Comparison Tool/
│
├── data/
│ ├── inventory_day1.csv
│ └── inventory_day2.csv
│
├── output/
│ ├── inventory_changes.csv
│ └── summary.txt
│
├── make_inventory_snapshots.py
├── compare_inventory.py
├── README.md
└── .gitignore


---

## Scripts

### make_inventory_snapshots.py
This script creates two inventory snapshots from a single CSV file by:
- Modifying prices for a subset of products
- Removing some products
- Adding a small number of new products

This simulates real inventory changes over time and makes the comparison process reproducible.

### compare_inventory.py
This script compares two inventory snapshots and:
- Identifies added and removed products
- Detects price changes
- Outputs a detailed CSV change log
- Generates a plain-text summary of changes

---

## How to Run

1. Place the source inventory CSV inside the `data/` directory.
2. Generate inventory snapshots:
   ```bash
   python make_inventory_snapshots.py
3. Run the comparison:
python compare_inventory.py
