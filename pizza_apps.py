import random
size = ["s", "m", "l", "xl"]
price = [40, 50, 60, 75]
sizeP = {
"s" : 40,
"m" : 50,
"l" : 60,
"xl" : 75

}

deli = {
"b" : 20,
"o" : 60,
}

sum = 0
def choice():
    ch = input("""
           press 'S' for small size (4 slices)
           press 'M' for medium size (6 slices)
           press 'L' for large size (8 slices)
           press 'XL' for extra large (8 large slices
           : """)
    return (ch)


s = choice()
def quantity():
    global sum
    pizzaNumber = int(input("How many pizzas do you want? "))
    sum += (sizeP[s] * pizzaNumber) - sizeP[s]
    return (sum)



def extras():
    global sum
    extra = input("Do you want extra? ")
    if extra == "yes":
      sum += (sizeP[s] + 2) - sizeP[s]
    return (sum)

def contiunation():
    con = input("do you want to continue?")
    if con == "no":
        exit()
    else:
        while True:
           choice()
           quantity()
           extras()
           stoping = input("do you want to continue again? ")
           if stoping == "no":
               break



def delivery():
    global sum
    city = input("Do you live in Beersheva? ")
    if city == "yes":
        sum += sizeP[s] + 20
    else:
        sum = sizeP[s] + 60


def summationPrice():
    from pizza_utiles import playGame
    global sum
    print("The total price with delivery will be: ", sum)
    print("The total price with discount will be", sum - (sum * (playGame() / 100)), "dollars")



# def contiunation():
#     con = input("do you want to continue?")
#     if con == "no":
#         exit()
#     else:
#         choice()
#         quantity()
#         extras()






