# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input("Enter a letter: ")
    if len(letter) != 1:
        print("Please enter a single letter.")
    elif letter.isalpha() == False:
        print("Please enter an alphabetical letter.")
    elif letter.lower() in 'aeiou':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    voting_age = 18
    age = input("Please enter your age: ")
    if age.isdigit() == False:
        print("Please enter a valid age.")
    elif int(age) < 0:
        print("Please enter a positive age.")
    elif int(age) >= voting_age:    
        print("You are old enough to vote.")
    else:
        print("You're too young to vote kid.")

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    age = input("Input a dog's age: ")
    if age.isdigit() == False:
        print("Please enter a valid age.")
    elif int(age) < 0:
        print("Please enter a positive age.")
    elif int(age) == 1:
        dog_years = 10
    elif int(age) == 2:
        dog_years = 20
    else:
        dog_years = 20 + (int(age) - 2) * 7
    print(f"The dog's {dog_years} old.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold = input("Is it cold? (yes/no): ")
    raining = input("Is it raining? (yes/no): ")
    if cold.lower() == 'yes' and raining.lower() == 'yes':
        print("Wear a waterproof coat.")
    elif cold.lower() == 'yes' and raining.lower() == 'no':
        print("Wear a warm coat.")
    elif cold.lower() == 'no' and raining.lower() == 'yes':
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month = input("Enter the month of the year (Jan - Dec): ")
    day = input("Enter the day of the month: ")
    if month.capitalize() not in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        print("Please enter a valid month.")
    elif day.isdigit() == False:
        print("Please enter a valid day.")
    elif int(day) < 1 or int(day) > 31:
        print("Please enter a valid day.")
    else:
        if month.capitalize() in ['Dec', 'Jan', 'Feb']:
            season = 'Winter'
        elif month.capitalize() in ['Mar', 'Apr', 'May']:
            season = 'Spring'
        elif month.capitalize() in ['Jun', 'Jul', 'Aug']:
            season = 'Summer'
        else:
            season = 'Fall'
        print(f"{month.capitalize()} {day} is in {season}.")

# Call the function
determine_season()

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    target = 42
    for i in range(6):
        guess = input("Guess a number between 1 and 100: ")
        if guess.isdigit() == False:
            print("Please enter a valid number.")
        elif int(guess) < 1 or int(guess) > 100:
            print("Please enter a number between 1 and 100.")
        elif int(guess) < target:
            print("Guess is too low.")
        elif int(guess) > target:
            print("Guess is too high.")
        else:
            print("Congratulations, you guessed correctly!")
            return
        if i == 4:
            print("Last chance!")
        
# Call the function
guess_number()

color = ''

while color != 'quit':
    color = input('Enter "green", "yellow", "red", or enter "quit" to exit: ').lower()
    print(f'The user entered {color}')
    if color == 'green':
        print("Go!")
    elif color == 'yellow':
        print("Caution!")
    elif color == 'red':
        print("Stop!")
    elif color == 'quit':
        print("Goodbye...")
    else:
        print("Bogus!")