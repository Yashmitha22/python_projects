#define the menu of the resturent
menu = {
    'Pizza':40,
    'Pasta':100,
    'Burger':50,
    'Salad':60,
    'coffee':70

}

#Greating
print("Welcome to K9 resturant")
print("Pizza: Rs 40\n Pasta: Rs 100\n Burger:Rs 50\nSalad: Rs 60\n coffee:Rs 70 ")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to order")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")
print(f"The total amount of item to pay is {order_total}")