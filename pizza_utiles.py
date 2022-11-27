import random

def playGame():
    game = input("do you want to play game for discount?")
    if game == "yes":
      numberRandom = random.randint(0, 9)
      print("The discount will be :", numberRandom, "%")
    else:
        exit()
    return(numberRandom)
