class JTdealership:
    def __init__(self):
        self.inventory = [
            {
                "vin": "1HGCM826",
                "make": "Honda",
                "model": "Accord",
                "year": 2018,
                "purchase_cost": 12000,
                "repair_cost": 500,
                "total_cost": 12500,
                "list_price": 15500,
                "status": "Available",
            },
            {
                "vin": "5YJ3E1EA",
                "make": "Tesla",
                "model": "Model 3",
                "year": 2021,
                "purchase_cost": 22000,
                "repair_cost": 1000,
                "total_cost": 23000,
                "list_price": 26000,
                "status": "Available",
            },
        ]
        self.sales_record = []

    def add_car(self, vin, make, model, year, cp, listed, repair_cost):
        car = {
            "vin": vin,
            "make": make,
            "model": model,
            "year": year,
            "purchase_cost": cp,
            "repair_cost": repair_cost,
            "total_cost": cp + repair_cost,
            "list_price": listed,
            "status": "Available",
        }
        self.inventory.append(car)
        print(f"\nAdded: {year} {make} {model} (VIN: {vin})")

    def sell_car(self, vin, sp=0):
        for car in self.inventory:
            if car["vin"] == vin and car["status"] == "Available":
                car["status"] = "Sold"
                profit_loss = sp - car["total_cost"]

                sale_info = {
                    "vin": vin,
                    "car": f"{car['year']} {car['make']} {car['model']}",
                    "total_cost": car["total_cost"],
                    "sale_price": sp,
                    "profit_loss": profit_loss,
                }
                self.sales_record.append(sale_info)

                status_label = "Profit" if profit_loss >= 0 else "Loss"
                print(f"\nCar Sold! {status_label}: ${abs(profit_loss):.2f}")
                return
        print("\nVehicle not found or already sold.")

    def display_inventory(self):
        print("\n--- Current Available Inventory ---")
        available = [c for c in self.inventory if c["status"] == "Available"]
        if not available:
            print("No cars in stock.")
        for c in available:
            print(f"[{c['vin']}] {c['year']} {c['make']} {c['model']} - Price: ${c['list_price']:.2f}")

    def generate_pnl_report(self):
        print("\n--- Profit & Loss Report ---")
        if not self.sales_record:
            print("No sales recorded yet.")
            return

        total_revenue = sum(s["sale_price"] for s in self.sales_record)
        total_cost = sum(s["total_cost"] for s in self.sales_record)
        net_pnl = total_revenue - total_cost

        for s in self.sales_record:
            print(f"Sold: {s['car']} | Cost: \({s['total_cost']:.2f} | Revenue:\){s['sale_price']:.2f} | P/L: ${s['profit_loss']:.2f}")

        print(f"\nNet Dealership P&L: ${net_pnl:.2f}")


JT = JTdealership()

while True:
    print("\n" + "=" * 50)
    print("\t\tWELCOME TO JT CARS")
    print("=" * 50)
    print("1. ADD CAR TO INVENTORY")
    print("2. SELL CAR")
    print("3. CHECK INVENTORY")
    print("4. CHECK PROFIT/LOSS REPORT")
    print("5. EXIT")
    print("-" * 50)

    try:
        choice = int(input("ENTER YOUR CHOICE (1-5): "))
    except ValueError:
        print("\nInvalid input! Please enter a number.")
        continue

    if choice == 1:
        vin1 = input("ENTER CAR VIN NO.: ")
        make1 = input("ENTER CAR MAKE: ")
        model1 = input("ENTER CAR MODEL: ")
        year1 = input("ENTER CAR YEAR: ")
        purchase1 = float(input("ENTER CAR PURCHASE PRICE: "))
        repair1 = float(input("ENTER CAR REPAIR COSTS: "))
        listprice1 = float(input("ENTER CAR LISTING PRICE: "))
        JT.add_car(vin1, make1, model1, year1, purchase1, listprice1, repair1)

    elif choice == 2:
        vin1 = input("ENTER CAR VIN NO.: ")
        sell1 = float(input("ENTER CAR SOLD PRICE: "))
        JT.sell_car(vin1, sell1)

    elif choice == 3:
        JT.display_inventory()

    elif choice == 4:
        JT.generate_pnl_report()

    elif choice == 5:
        print("\nThank you for using JT Cars Management System. Goodbye!")
        break

    else:
        print("\nInvalid option. Please choose between 1 and 5.")