import random

def main():
    # prob1()
    # prob2()
    prob3()
    # prob4()

def prob1():
    print(random.randint(0,9))

def prob2():
    while 1==1:
        userInput = input("Enter a word: ")
        if userInput == "q":
            print("User has Quit")
            break
        else:
            print("Again, Again")

def prob3():
    while 9==9:
        number = int(input("Enter a positive number!: "))
        if number !=0:
            i = 0
            while i <= number:
                print(i)
                i += 1
        else:
            print("User Has Quit")
            break

def prob4():
    cpuNum = random.randint(1,100)
    while cpuNum <= 100:
        userNum = int(input("The computer has picked a number between 1 - 100! Guess it!!!:"))
        if userNum == cpuNum:
            print("You got the right number!")
            break
        elif userNum > cpuNum:
            print("Go lower")
        elif userNum < cpuNum:
            print("Go Higher")
        else:
            print("Try Again")

if __name__ == '__main__':
    main()