# even though I used list comprehentions, I expanded so you could see my # indentation.
myPizzas = ["vegetarian", "cheese", "ham and pineapple"]
friendPizzas = myPizzas[:]
myPizzas.append("spinach and feta")
friendPizzas.append("all dressed")
print("My favorite pizzas are:")
for pizza in myPizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friendPizzas:
    print(pizza)