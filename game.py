import random


def rules():                                      # Create a function for the rules of the game
    print("""Number Guessing Game.
Rules of the game:
1. A random number between 1 and 1000 will be generated at the start of the game.
2. The player starts with a total of 100 points at the start of the game.
3. Each incorrect guess results in a deduction of 1 point.
4. If an incorrect guess is repeated, 5 points will be deducted instead.
5. Hints will be given each time an incorrect guess is made.
6. If the player's point count reaches 0, the game ends.""")


def evenOdd(n):                                   # Create a funtion with parameter n to determine whether n is even or odd
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


def hints(guess, g):                              # Create a function with parameter guess and g that gives the player hints when an incorrect guess is made.
    if evenOdd(guess) == evenOdd(g):              # If both the guess and g are both even/odd, the hint for which g is an even/odd is not returned.
        if len(str(guess)) == len(str(g)):        # If the number of digits for both guess and g are the same then the hint for how many digits g has is not returned.
            if guess > g:                         # If guess is more than g then the hint for that is given and vice versa.
                return "The number is less than " + str(guess)
            else:
                return "Then number is greater than " + str(guess)
        else:
            return "The number has " + str(len(str(g))) + " digits."
    else:
        return "The number is an " + evenOdd(g) + " number."


def guessing(n1, g1, p):                          # Create a function with parameters n1, g1 and p.
    numGuessed = []                               # Create an empty array for the numbers guessed.

    while n1 != g1:
        if p > 0 and n1 != g1:                    # Make sure that n1 is not equal to g1 and that the player still have points left.
            n1 = int(input("Enter a number: "))   # Store the player's guess into variable n1.

            if n1 == g1:
                print("""Congratulations! You've guessed the number!
Points remaining: """ + str(p))
            else:
                if n1 in numGuessed:              # Check if the number guessed is in the array.
                    p -= 10
                    print("""You've already guessed this number.
Points remaining: """ + str(p))
                else:
                    numGuessed.append(n1)
                    p -= 5
                    print(hints(n1, g1))          # Use the hints function with guess and g initialised to n1 and g1 to display the appropriate hint.
                    print("Points remaining: " + str(p))
        else:
            print("No points left. Game over.")
            break


def main():                                       # Create a main function
    endGame = False
    rules()
    while endGame is False:
        outLoop = False
        numGenerated = random.randint(1, 1000)    # Generate a random number between 1 and 1000.
        points = 100

        guessing(-1, numGenerated, points)        # Use the guessing function with n1, g1 and p initialised to -1, numGenerated and points respectively.
        choice = input("Would you like to play again? (Y/N)")
        if choice == "N":
            endGame = True
        while outLoop is False:
            if choice == "Y":
                rule = input("Read the rules again? (Y/N)")
                if rule == "Y":
                    rules()
                    outLoop = True
                elif rule == "N":
                    outLoop = True
                while rule != "Y" and rule != "N":
                    rule = input("Please input Y/N ")
                    if rule == "Y":
                        rules()
                        outLoop = True
            else:
                choice = input("Please input Y/N ")
    print("Thank you for playing!")


main()
