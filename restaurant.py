
print("----- RESTAURANT MENU -----")
print("1. Burger - Rs. 80")
print("2. Pizza - Rs. 150")
print("3. Sandwich - Rs. 60")

name = input("Enter customer name: ")
choice = int(input("Select food item (1-3): "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Burger"
    price = 80
elif choice == 2:
    item = "Pizza"
    price = 150
elif choice == 3:
    item = "Sandwich"
    price = 60
else:
    item = ""
    price = 0

if price == 0:
    print("Invalid food item")
else:
    total = price * quantity

    print("\n----- CUSTOMER BILL -----")
    print("Customer Name:", name)
    print("Food Item:", item)
    print("Quantity:", quantity)
    print("Total Bill: Rs.", total)
