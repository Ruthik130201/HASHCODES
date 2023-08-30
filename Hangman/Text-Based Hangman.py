def game_code(dictionary, guesses):
    import random
    word = (dictionary [random.randint(0, len(dictionary) - 1)]).lower()

    print("This word has " + (str(len(word))) + " letters in it.")
    underscores = []
    separator = " "
    for letter in word:
        underscores += "_"
    
    ListOf_Guesses = []

    while guesses > 0:
        print(separator.join(underscores))
        print("Number of Guesses Remaining: " + str(guesses))
        print("These are the guesses you have made: " + str(ListOf_Guesses))
        guess = input("Make a guess: ").lower()

        if not guess.isalpha():
            print("\n Please guess a letter. \n")
            continue
        elif len(guess) != len(word) and len(guess) != 1:
            print("\n You can either guess the entire word or just one letter at a time. \n")
            continue
        alreadyGuessed = False
        for w in ListOf_Guesses:
            if w == guess:
                alreadyGuessed = True
                break
        if alreadyGuessed:
            print("\n You already guessed this letter. Please try again. \n")
            continue
        elif len(guess) == len(word):
            if guess == word:
                print("\n Congratulations! You guessed the entire word with " + str(guesses) + " guess" + ("" if guess == 1 else "es") + " remaining! \n")
                break
            else:
                print("\n You did not guess the entire word correctly. \n")
                guesses -= 2
                ListOf_Guesses.append(guess)
                continue
        else:
            ListOf_Guesses.append(guess)
            positions = []
            for pos in range(len(word)):
                if guess == word[pos]:
                    positions.append(pos)
            if len(positions) > 0:
                print("\n Good job! There " + ("is " if len(positions) == 1 else "are ") + str(len(positions))
                      + (" instance " if len(positions) == 1 else " instances ") + "where that letter appears in this word. \n")
                for pos in positions:
                    underscores[pos] = guess
            else:
                print("\n The letter " + guess + " is not found in this word. \n")
                guesses -= 1
                continue
            if not "_" in underscores:
                print(separator.join(underscores))
                print("\n Congratulations! You have found the word with " + str(guesses) + " guess" + ("" if guess == 1 else "es") + " remaining! \n")
                break
    if guesses <= 0:
        print("You have run out of guesses. The word was " + word.upper() + ". Game Over. \n")
Menu = True 
amtGuesses = 6

DictFile = open("Dictionary.txt")
dictionary = []
for line in DictFile:
    dictionary.append(line.strip("\n"))

    
while Menu == True:
    print("""Main Menu:
    [1] Start Game
    [2] Settings
    [3] Exit""")
    menuChoice = input()
    if menuChoice == "1":
        game_code(dictionary, amtGuesses)
    elif menuChoice == "2":
        print("""Settings:
    What would you like to set the difficulty to?:
    [1] Easy
    [2] Medium
    [3] Hard
    [4] Return to Main Menu""")
        difficulty = input()
        if difficulty == "1":
            amtGuesses = 9
        elif difficulty == "2":
            amtGuesses = 6
        elif difficulty == "3":
            amtGuesses = 3
        elif difficulty == "4":
            continue
        else:
            print("Please select a valid menu option.")
    elif menuChoice == "3":
        Menu = False
    else:
        print("Please select a valid menu option.")