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


