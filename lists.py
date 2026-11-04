shopping_list = ["Milk", "Bread", "Eggs", "Apples", "Cheese"]

shopping_list.append("Bananas")
shopping_list.append("Rice")

shopping_list.remove("Cheese")

number_of_products = len(shopping_list)

print("Number of products:", number_of_products)

print("Shopping list:", shopping_list)

if "Milk" in shopping_list:
    print("Milk is on the shopping list.")
else:
    print("Milk is not on the shopping list.")
