# JT Cars - Dealership Management System

## Overview
**JT Cars Dealership Management System** is a lightweight, interactive command-line interface (CLI) application built in Python. Designed for car dealerships, this tool simplifies inventory management, vehicle sales tracking, and financial performance monitoring. It allows dealership operators to easily manage vehicle intake, track associated costs (purchase price + repairs), process sales, and generate real-time Profit & Loss (P&L) reports.

---

## Features
- **Pre-loaded Sample Data:** Comes pre-configured with default inventory items for immediate demonstration and testing.
- **Inventory Tracking:** Maintain detailed records for each vehicle, including VIN, Make, Model, Year, Purchase Cost, Repair Cost, Total Cost, and Listing Price.
- **Vehicle Acquisition:** Easily add new vehicles to the active inventory with automatic computation of total investment costs (`purchase_cost + repair_cost`).
- **Sales Processing:** Record vehicle sales by VIN, calculate profit/loss per transaction automatically, and update stock status.
- **Available Stock View:** Quick display of available inventory showing key details and listing prices.
- **Financial Reporting:** Generate a comprehensive Profit & Loss report summarizing costs, revenues, and net profits across all sales records.

---

## Technologies/Tools Used
- **Language:** Python 3.x
- **Standard Libraries:** No external dependencies required (uses built-in Python data structures like dictionaries and lists).

---

## Steps to Install & Run the Project

### Prerequisites
- Make sure Python 3.x is installed on your computer. You can verify this by running:
  ```bash
  python --version
  # or
  python3 --version
  ```

### Installation & Execution
1. **Clone or Download the Project:**
   Save the application code into a file named `main.py` (or `dealership.py`).

2. **Open Terminal / Command Prompt:**
   Navigate to the directory where the file is saved:
   ```bash
   cd path/to/your/folder
   ```

3. **Run the Application:**
   Execute the script using Python:
   ```bash
   python main.py
   # or
   python3 main.py
   ```

---

## Instructions for Testing

Follow these manual testing procedures in the CLI menu to verify application functionality:

### 1. View Initial Inventory (Choice `3`)
- Enter `3` at the main menu.
- **Expected Outcome:** You should see pre-loaded vehicles (Honda Accord and Tesla Model 3) displayed with their respective VINs and listing prices.

### 2. Add a New Car (Choice `1`)
- Enter `1` at the main menu.
- Provide test data when prompted:
  - **VIN:** `TEST123456`
  - **Make:** `Toyota`
  - **Model:** `Camry`
  - **Year:** `2020`
  - **Purchase Price:** `10000`
  - **Repair Costs:** `1000`
  - **Listing Price:** `14000`
- **Expected Outcome:** Message confirming the car was added. Check inventory again using option `3` to verify it appears in the list.

### 3. Sell a Car (Choice `2`)
- Enter `2` at the main menu.
- Test selling one of the pre-loaded cars:
  - **VIN:** `1HGCM826`
  - **Sold Price:** `16000`
- **Expected Outcome:** Console displays `Car Sold! Profit: $3500.00` (since total cost was $12,500).

### 4. Generate P&L Report (Choice `4`)
- Enter `4` at the main menu.
- **Expected Outcome:** Displays a breakdown of sold vehicles alongside individual profit/loss figures and the net dealership profit.

### 5. Input Validation & Edge Cases
- **Invalid Menu Option:** Enter `9` at the menu prompt to ensure it displays an error message without crashing.
- **Invalid Data Type:** Enter text (e.g., `abc`) when asked for a price choice to confirm the application catches `ValueError` gracefully.
- **Sell Non-existent Vehicle:** Attempt to sell a vehicle using an invalid VIN (e.g., `INVALID999`) to confirm it reports "Vehicle not found or already sold."