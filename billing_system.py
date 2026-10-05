class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, products, tax_rate=0.05):
        self.products = products
        self.tax_rate = tax_rate

    def calculate_total(self):
        subtotal = sum(product.total() for product in self.products)
        tax = subtotal * self.tax_rate
        return subtotal, tax, subtotal + tax

    def display_bill(self):
        subtotal, tax, grand_total = self.calculate_total()

        print(f"{'Product':<15}{'Price':>10}{'Qty':>6}{'Amount':>12}")
        print("-" * 43)
        for product in self.products:
            print(f"{product.name:<15}{product.price:>10.2f}{product.quantity:>6}{product.total():>12.2f}")
        print("-" * 43)
        print(f"{'Subtotal':<31}{subtotal:>12.2f}")
        print(f"{'Tax (' + str(int(self.tax_rate * 100)) + '%)':<31}{tax:>12.2f}")
        print(f"{'Grand Total':<31}{grand_total:>12.2f}")


def main():
    products = []
    bill = Bill(products, tax_rate=0.05)

    while True:
        print("\n===== Billing System =====")
        print("1. Add Product")
        print("2. Display Bill")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                if price < 0 or quantity <= 0:
                    print("Price must be non-negative and quantity must be positive")
                    continue
                products.append(Product(name, price, quantity))
                print(f"Product '{name}' added")
            except ValueError:
                print("Invalid price or quantity")
        elif choice == "2":
            if products:
                bill.display_bill()
            else:
                print("No products added yet")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
