import random
def playgame():
 if(yourchoice == computerchoice):
    print("Game draw")
 elif(yourchoice == "Rock" and computerchoice == "Paper"):
        print("You Loose!")
 elif(yourchoice == "Rock" and computerchoice == "Scissors"):
        print("You Win!")
 elif(yourchoice == "Paper" and computerchoice == "Scissors"):
        print("You Loose!")
 elif(yourchoice == "Paper" and computerchoice == "Rock"):
        print("You Win!")
 elif(yourchoice == "Scissors" and computerchoice == "Paper"):
        print("You Win!")
 elif(yourchoice == "Scissors" and computerchoice == "Rock"):
       print("You Loose!")


n=0
while(n<1):
 computer =  random.choice([1,2,3])
 computerdict = {
    1 : "Rock",
    2 : "Paper",
    3 : "Scissors"
 }
 userchoice = int(input("Enter your choice :"))
 userdict = {
   1 : "Rock",
   2 : "Paper",
   3 : "Scissors"
 }
 
 yourchoice = userdict[userchoice]
 computerchoice = computerdict[computer]
 
 print("Your choice is :",yourchoice)
 print("Computer choice is :",computerchoice)
 
 playgame()

 choice = input("Wanna play again :")
 if(choice=="Yes"):
    continue
 else:
    print("Bye")
    break
