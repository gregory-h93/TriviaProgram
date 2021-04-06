import random

def computers():
    rNum = int(random.random() * 3)
    if rNum == 0:
        print("What are the words of the acronym CD-ROM?")
        print("1. Complete Disregard Regarding Optimal Minimization")
        print("2. Compact Disc Read Only Memory")
        choice = int(input())
        while choice < 1 or choice > 2:
            print("Invalid input! Please enter your selection for the correct answer(1 or 2): ")
            choice = int(input())
        if choice == 2:
            print("Congratulations! You were correct! CD-ROM is a type of optical disc that originated in Japan in 1982.")
        else:
            print("Incorrect! The correct answer was option #2.")
    else:
        if rNum == 1:
            print("When working in Microsoft Internet Explorer, in 2013, what is the shortcut to open the window to your favorites?")
            print("1. Ctrl+B")
            print("2. Ctrl+D")
            choice = int(input())
            while choice < 1 or choice > 2:
                print("Invalid input! Please enter your selection for the correct answer(1 or 2): ")
                choice = int(input())
            if choice == 2:
                print("Incorrect! The correct answer was option #1.")
            else:
                print("Congratulations! You were correct! This shortcut will open the window to your favorites where you can organize and delete your favorites.")
        else:
            print("Which general term refers to all kinds of harmful software, including viruses, worms, trojan horses, and spyware?")
            print("1. Palware")
            print("2. Malware")
            choice = int(input())
            while choice < 1 or choice > 2:
                print("Invalid input! Please enter your selection for the correct answer(1 or 2): ")
                choice = int(input())
            if choice == 2:
                print("Congratulations! You were correct! Malware is a shortened form of 'malicious software'")
            else:
                print("Incorrect! The correct answer was option #2.")

def music():
    rNum = int(random.random() * 3)
    if rNum == 0:
        print("What musician won the Nobel Prize for Literature in 2016?")
        print("1. Bruce Springsteen")
        print("2. Bob Dylan")
        choice = int(input())
        while choice < 1 or choice > 2:
            print("Invalid input! Please enter your selection for the correct answer(1 or 2): ")
            choice = int(input())
        if choice == 2:
            print("Congratulations! You were correct! Bob Dylan won the Nobel Prize for Literature in 2016.")
        else:
            print("Incorrect! The correct answer was option #2.")
    else:
        if rNum == 1:
            print("Which artist(s) won the Grammy for Best New Artist in 1990?")
            print("1. Milli Vanilli")
            print("2. Bobby Brown")
            choice = int(input())
            while choice < 1 or choice > 2:
                print("Invalid input! Please enter your selection for the correct answer(1 or 2): ")
                choice = int(input())
            if choice == 2:
                print("Incorrect! The correct answer was option #1.")
            else:
                print("Congratulations! You were correct! Milli Vanilli won the award in 1990 for their outstanding debut album: Girl You Know It's True")
                print("Fun Fact: They returned the award after it was revealed they did not actually contribute any of the vocals.")
        else:
            print("Who was the first Western music artist(s) to be allowed to perform a concert in China?")
            print("1. Elton John")
            print("2. Wham!")
            choice = int(input())
            while choice < 1 or choice > 2:
                print("Invalid input! Please enter your selection for the correct answer(1 or 2): ")
                choice = int(input())
            if choice == 2:
                print("Congratulations! You were correct! In 1985, Wham!'s visit and concert in China were both firsts by a Western pop act in that country.")
            else:
                print("Incorrect! The correct answer was option #2.")

def sports():
    rNum = int(random.random() * 3)
    if rNum == 0:
        print("In golf, which other word refers to the terminology 'a hole-in-one'?")
        print("1. Score!")
        print("2. Ace")
        choice = int(input())
        while choice < 1 or choice > 2:
            print("Invalid input! Please enter your selection for the correct answer(1 or 2): ")
            choice = int(input())
        if choice == 2:
            print("Congratulations! You were correct! Ace in golf is another term that describes 'a hole-in-one'. This term describes a situation where a golfer hits the ball into the bottom of the cup from the tee.")
        else:
            print("Incorrect! The correct answer was option #2.")
    else:
        if rNum == 1:
            print("Who was the last professional hockey player to play without a helmet?")
            print("1. Craig MacTavish")
            print("2. Bob Bergloff")
            choice = int(input())
            while choice < 1 or choice > 2:
                print("Invalid input! Please enter your selection for the correct answer(1 or 2): ")
                choice = int(input())
            if choice == 2:
                print("Incorrect! The correct answer was option #1.")
            else:
                print("Congratulations! You were correct! Craig MacTavish is a Canadian professional ice hockey executive and former player from 1979-1997.")
        else:
            print("Which Boston Celtics' player won the NBA Finals MVP in 1981?")
            print("1. Rick Robey")
            print("2. Cedric Maxwell")
            choice = int(input())
            while choice < 1 or choice > 2:
                print("Invalid input! Please enter your selection for the correct answer(1 or 2): ")
                choice = int(input())
            if choice == 2:
                print("Congratulations! You were correct! Despite being featured on a team with three future Hall of Famers, the relatively-obscure Cedric Maxwell was most credited with leading the team to victory during the 1981 NBA Finals.")
            else:
                print("Incorrect! The correct answer was option #2.")

# Main
print("Welcome to trivia where your knowledge will be tested on the genre of your choice!")
n = ""
while True:    #This simulates a Do Loop
    print("Please select a genre: ")
    print("1. Music")
    print("2. Computers")
    print("3. Sports")
    print("4. End the program")
    print(" Which would you like to select? ")
    choice = int(input())
    while choice < 0 or choice > 4:
        print("Invalid input! Please enter a valid choice(1, 2, 3, or 4): ")
        choice = int(input())
    if choice == 1:
        music()
    else:
        if choice == 2:
            computers()
        else:
            if choice == 3:
                sports()
    if choice == 4:
        again = n
    else:
        print("Would you like to play again? (Y/N)")
        again = input()
        while again != "Y" and again != "y" and again != "N" and again != "n":
            print("Please enter in (Y/N). Would you like to run the program again? (Y/N)")
            again = input()
    if not(again == "Y" or again == "y"): break   #Exit loop
print("You have chosen to end the trivia game. Goodbye!")
