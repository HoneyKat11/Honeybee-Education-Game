# Name: Katarya Johnson-Williams
# Date Started: 9/1/2020
# Description: This is a honeybee-themed series of mini-games and quizzes!
# The goal will be to teach users something new about honeybees.
# Sources: https://rb.gy/uyhalo

#A function to check for a valid answer to a math question
def math_answer_check(question, answer):
    print(question)
    new_answer = input("Enter in your new answer: ")
    if new_answer == answer:
        print("Awesome! That's correct.")

# Math game with a honeybee theme (stored in a function)
def honeybee_math():
    print("It's math time! Buzz buzz.")
    confirm = input("When you're ready to start, press ENTER. ")
    print("\nIMPORTANT: All answers are integers and must be submitted without words, commas, or any extraneous characters. Thank you!")
    print("\nQuestion 1: Humans have been collecting honey, beeswax, and honeycombs from wild honeybees since 5500 BCE.")
    print("Today, we still use honeybee products on a daily basis.")
    question = print("About how many years have humans been using honeybee products as of the year 2020? \n")
    answer = 5500 + 2020
    answer_1 = input()
    if answer_1 == (5500 + 2020):
        score_count = 1
        print("Congratulations! 7,520 years was the correct answer!")
    else:
        math_answer_check(question, answer)
    print("\nQuestion 2: The average beehive can produce 60 pounds (960 ounces) of honey in a productive season.")
    print("A beekeeper is filling eight ounce bottles of honey to sell at a farmer's market.")
    print("If a hive produces 15.25 pounds of honey this month, how many ounces are leftover if the beekeeper fills as many bottles as possible?")
    print("Note: There are 16 ounces in one pound. \n")
    answer_2 = input()
    if answer_2 == (244 % 8):
        score_count += 1
        print("Awesome job! 4 ounces was the correct answer!")
    print("\nQuestion 3: In 2016, the United States imported 369 million pounds of honey from foreign nations to meet demand.")
    print("A shipping box holds three layers of three by three stacks of honey jars. How many jars will fit in the box? \n")
    answer_3 = input()
    if answer_3 == (3 ** 3):
        score_count += 1
        print("Great! 27 jars was the correct answer!")
    print("\nQuestion 4: Warm Florida weather allows beekeepers to harvest honey all year long.")
    print("However, in colder places honey needs to be stored at a temperature above 59 ºF to prevent crystallization.")
    print("If a pantry is 48 ºF, how many degrees warmer does it need to be to keep honey from crystalizing? \n")
    answer_4 = input()
    if answer_4 == (60 - 48):
        score_count += 1
        print("Good work! 12ºF was the correct answer!")
    print("\nQuestion 5: A queen bee can lay up to 2,000 eggs in a day.")
    print("About how many eggs does a queen bee lay in an hour?")
    print("Note: Round your answer to the nearest whole integer. \n")
    answer_5 = input()
    if answer_5 == (2000 // 24):
        score_count += 1
        print("Wonderful! 83 eggs an hour was the correct answer!")
    print("\nQuestion 6: A nuc is a small hive with three to five frames of bees and a mated, accepted queen.")
    print("Nucs are used by beekeepers to establish new beehive colonies.")
    print("If a fully developed beehive has ten frames and a beekeeper has eight fully developed hives,")
    print("how many five-frame nucs can the beekeeper put together?")
    print("Keep in mind only five frames can be taken from each hive in order for the developed hives to survive.  \n")
    answer_6 = input()
    if answer_6 == (40 / 5):
        score_count += 1
        print("That's it! 8 nucs was the correct answer!")
    print("\nQuestion 7: The population of a beehive fluctuates depending on the season and availability of food.")
    print("In colder months, beehive populations can drop below 20,000 bees,")
    print("while in warmer months beehives can reach a peak population of up to 60,000 bees.")
    print("If a beehive has a population of 50,000 honeybees and 7.5% of the population is made up of drones (male bees),")
    print("about how many drones are in the beehive?  \n")
    answer_7 = input()
    if answer_7 == (50000 * 0.075):
        score_count += 1
        print("Winner! " * 3)
        print("Congratulations! 3,750 drones was the correct answer!")
        print("\nThanks for playing! Your score was " + str(score_count) + " out of 7! I hope you learned something new.")
        play_more = input("Would you like to play another game? Y or N ")
        if play_more == "Y":
            print("\nAwesome to hear! Have fun!\n")
            get_level()
        else:
            print("\nThat's okay! Have a nice day!")
            exit()

# Quiz to evaluate knowledge of honeybees (stored in a function)
def honeybee_quiz():
    print("Time to test your knowledge!")
    confirm = input("When you're ready to start, press ENTER. ")
    if confirm == "":
        print("Sorry, this mini game is still under construction!")
        menu_select()
    else:
        print("Oops, I guess you weren't ready!")
        honeybee_quiz()


# Adventure game where you make choices as a worker honeybee (stored in
# a function)
def honeybee_adventure():
    print("Time for an adventure!")
    confirm = input("When you're ready to start, press ENTER. ")
    if confirm == "":
        print("Sorry, this mini game is still under construction!")
        menu_select()
    else:
        print("Oops, I guess you weren't ready!")
        honeybee_adventure()


# Function to select a game from a menu
def menu_select():
    print("\nPlease enter the number of your selection.")
    game_choice = input(
        "Select One:\n 1)Math\n 2)Quiz (under construction)\n 3)Adventure "
        "(under construction)\n")
    if game_choice == "1":
        honeybee_math()
    elif game_choice == "2":
        honeybee_quiz()
    elif game_choice == "3":
        honeybee_adventure()
    else:
        print(
            "Oops! That's not an option. Please enter a number "
            "corresponding ")
        print("with an option listed on the menu.")
        menu_select()


# Function to evaluate player knowledge of honeybees on a scale of 1 to 5
# One way this function could be improved is by adding a backup "else"
# statement in case the user enters an
# input not recognized by the current elif conditions
def get_level():
    # The user is asked to self-evaluate their knowledge of honeybees
    # on a scale of 1 (very poor) to 5 (expert)
    print("How would you rate your knowledge of honeybees?")
    knowledge = input("1 (very poor) to 5 (expert)\n ")
    level = int(knowledge)
    # If the user inputs a level of 4 or higher, they are prompted to
    # confirm their selection
    # and asked if they would like to learn more (because even
    # experts can learn new things!)
    if level >= 4:
        level_check = input("Are you sure that is correct? Y or N ")
        if level_check == "Y":
            learn_more = input("Would you like to learn more? Y or N ")
            # If the user confirms their rating was correct and
            # they want to learn more,
            # they are sent to the menu_select() function
            if level_check == "Y" and learn_more == "Y":
                print("Great! Let's play a game.")
            # If the user confirms their rating was correct and
            # they do not want to
            # learn more, the program terminates
            elif level_check == "Y" and learn_more == "N":
                print("Thanks for playing!")
        # If the user did not rate themselves correctly, the
        # evaluation function restarts
        elif level_check == "N":
            print("Oh no! Time to start again!\n")
            get_level()
    # If the user inputs a level of 3 or lower, they are prompted to
    # confirm their selection
    # and asked if they would like to learn more
    elif level <= 3:
        level_check = input("Are you sure that is correct? Y or N ")
        if level_check == "Y":
            learn_more = input("Would you like to learn more? Y or N ")
            # If the user confirms their rating was correct and they want
            # to learn more,
            # they are sent to the menu_select() function
            if level_check == "Y" and learn_more == "Y":
                print("Awesome! Let's play a game to learn more.")
            # If the user confirms their rating was correct and they
            # do not want to
            # learn more, the program terminates
            elif level_check == "Y" and learn_more == "N":
                print("Thanks for playing!")
        # If the user did not rate themselves correctly, the evaluation
        # function restarts
        elif level_check == "N":
            print("Oh no! Time to start again!\n")
            get_level()


# Get player name and welcome them to the program
player_name = input("Buzz buzz...What's your name? ")
# The user is welcomed to the program and told the purpose.
# Their name is concatenated with the welcome message using the + string
# operator
print("\nWelcome to my COP 1500 integration project, " + player_name + "!")
print("Today, we'll be learning about honeybees.")
print("Hopefully, you'll learn something new today!\n")
# The user is sent to the evaluation (eval()) function to get started
get_level()
menu_select()
