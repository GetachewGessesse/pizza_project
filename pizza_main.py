print("*************************************************************")
print("Welcome to our pizza store:")
print("*************************************************************")
age = int(input("Please enter your age: "))
while age < 18:
    print("You are under age, thanks for your visit:")
    break
else:
    from pizza_apps import quantity
    quantity()
    from pizza_apps import extras
    extras()
    from pizza_apps import contiunation
    contiunation()
    from pizza_apps import delivery
    delivery()
    from pizza_apps import summationPrice
    sum = summationPrice()
    # from pizza_apps import contiunation
    # contiunation()


