import random


def gameWin(PC, You):  #Checks who wins PC or Your
    if PC == You:
        return None

    elif PC == 'R':

       if You == "S":
         return False
       elif You == "P":
         return True

    elif PC == "P":

       if You == "R":
         return False
       elif You == "S":
         return True

    elif PC == 'S':

       if You == 'P':
         return False
       elif You == "R":
         return True

print("PC turn: ROCK(R),PAPER(P),SCISSORS(S)?")


randNo=random.randint(1,3)      #PC will select randomly
if randNo==1:
    PC="R"
elif randNo==2:
    PC="P"
elif randNo==3:
    PC="R"

You=input("Your Turn: ROCK(R),PAPER(P),SCISSORS(S)?")#takes input from player

a= gameWin(PC,You) #function call

print(f"Computer choose{PC}") #USED literal string interpolation OR F STRING
print(f"You choose{You}")


if a==None:
    print("Tie")
elif a:
    print("you win")
else:
    print('You lose')
