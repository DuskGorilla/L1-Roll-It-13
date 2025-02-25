def int_check(question):
    """Checks user enter an integer more than / equal to 13"""

    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == "":
            return "infinite"

        try:
            response = int(response)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts Here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("💎📃✂️ Rock / Paper/ Scissors Game ✂️📃💎")
print()

# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")


if num_rounds == "infinite":
    mode = "infinite"
    print("you chose infinite")
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break
        
    rounds_played += 1
    print("rounds played: ", rounds_played)

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    print("num rounds: ", num_rounds)

# Game loop ends here

# Game History / Statistics area
