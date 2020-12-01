"""Honeybee Integration Project"""
__author__ = "Katarya Johnson-Williams"
"""This file is a honeybee-themed series of mini-games and quizzes. The 
purpose of this project is to teach the user something new about honeybees."""
"""Date Started: 9/1/2020"""
"""Date Finished: 11/30/2020"""
"""Sources: https://rb.gy/uyhalo"""


def valid_yes_or_no(user_input):
    """The purpose of this function is to receive user input and determine
    if the user input is a valid yes (Y) or no (N) response to the prompt.
    This function is called throughout the program to ensure errors do not
    occur. Once the user has entered a valid yes (Y) or no (N) response,
    the valid input is returned."""
    # The initial if statement verifies that user_input is a string. The
    # not operator checks to see if the statement isinstance(user_input,
    # str) is false. However, because the input() function takes a string
    # by default, the while loop within this condition will never be run.
    if not isinstance(user_input, str):
        # This while loop prompts the user to input a valid "Y" or "N"
        # input and loops until the user inputs one of them. The != is a
        # rational operator that ensures the while loop continues until
        # the user_input is equivalent to "Y" or "N". The and operator
        # ensures the while loop is checking for both conditions ("Y" or "N").
        while user_input.capitalize() != "Y" and user_input != "N":
            user_input = input("Please enter Y for Yes or N for No: ")
    # Once user_input is verified to be a string, this elif statement checks
    # to see if user_input is not equivalent to the valid input "Y" or "N".
    # If it is not, a while loop is run.
    elif user_input.capitalize() != "Y" or user_input != "N":
        # This while loop prompts the user to input a valid "Y" or "N"
        # input and loops until the user inputs one of them. The != is a
        # rational operator that ensures the while loop continues until
        # the user_input is equivalent to "Y" or "N". The and operator
        # ensures the while loop is checking for both conditions ("Y" or "N").
        while user_input.capitalize() != "Y" and user_input != "N":
            user_input = input("Please enter Y for Yes or N for No: ")
    # If the user input is equivalent to "Y" or "N", the function returns
    # the user_input as it entered the function by passing the else failsafe.
    else:
        pass
    # The updated (or not updated) user_input is returned
    return user_input.capitalize()


def math_answer_valid(answer):
    """The purpose of this function is to prevent errors within the
    honeybee_math() function by ensuring answers to the math questions
    are integers. If the user does not provide a valid input, this function
    will prompt the user until they enter a valid integer input. Once the
    user enters a valid integer value, the value is returned."""
    # A try statement tests to ensure the user input is an integer (all math
    # question answers are integers)
    try:
        # If the user input is an integer, it is returned in integer form
        valid_answer = int(answer)
        return int(valid_answer)
    # If the user input cannot be converted into an integer class,
    # the function restarts with an error reminding the user the answer
    # needs to be an integer. The program asks for a new answer to pass
    # to the function before restarting.
    except ValueError:
        print("\nOops! Make sure you enter an integer.")
        new_answer = input("Enter your new answer: ")
        math_answer_valid(new_answer)


def math_answer_retry(question, answer):
    """The purpose of this function is to give the user the opportunity to
    re-submit their answer to a given question in the honeybee_math()
    function until they enter the correct integer answer. The function first
    ensures the answer is an integer and then compares it to the correct
    answer to see if the new answer is correct. If not, the user is prompted
    to enter a new answer. This loop continues until the user enters the
    correct answer."""
    # The question is reprinted for the user and they are prompted to submit
    # a new answer stored in new_answer
    print(question)
    new_answer = input("Enter in your new answer: ")
    new_answer_check = 0
    # A try statement is used to check and see if the new answer is a valid
    # integer input. If so, the value new_answer_check continues to the
    # if statement.
    try:
        new_answer_check = int(new_answer)
    # If the user input cannot be converted into an integer class,
    # the function restarts
    except ValueError:
        print("\nOops! Please make sure your answer is an integer.")
        math_answer_retry(question, answer)
    # An if statement compares new_answer_check to answer (which now holds
    # the correct answer) and if the answers match then the user is
    # congratulated. If new_answer still does not match the value of answer
    # then the function restarts.
    if new_answer_check == answer:
        print("\nAwesome! That's correct.")
        return new_answer_check
    # If the user is incorrect, the function starts over so the user has
    # another opportunity to input the correct answer
    else:
        print("\nSorry! Try again.")
        math_answer_retry(question, answer)


def honeybee_math():
    """The purpose of this function is to teach the user something new about
    honeybees by asking a series of honeybee-themed math questions. There are
    seven total questions and the user has infinite tries to get the correct
    answer."""
    # The variable score_count will be used to keep track of the score.
    # It is assigned an initial value of 0.
    score_count = 0
    # A print statement welcomes the user to the game
    print("It's math time! Buzz buzz.")
    # The first question is asked and the user is prompted for an answer
    question = "\nQuestion 1: Humans have been collecting honey, beeswax, " \
               "and honeycombs from wild honeybees since 5500 BCE. " \
               "\nToday, we still use honeybee products on a daily basis. " \
               "\nAbout how many years have humans been using honeybee " \
               "products as of the year 2020? \n"
    answer = input(question)
    # The user's input is checked to ensure it is an integer by passing
    # it through the function math_answer_valid()
    math_answer_valid(answer)
    # If the user answers the question correctly, they are congratulated
    # and will move on to the next question.
    if str(answer) == str(5500 + 2020):
        print("Congratulations! 7,520 years was the correct answer!")
    # If the user answers the question incorrectly, they are sent to the
    # function math_answer_check with the question and answer to
    # ensure they are able to eventually get the correct answer. The question
    # argument (assigned earlier) and the answer argument (assigned below)
    # are sent to fulfill the parameters of the function.
    else:
        print("\nOops, that's not right! Try again!")
        answer = 7520
        math_answer_retry(question, answer)
    # Once the user comes up with the correct answer (7520), one point is
    # added to the score_count variable
    score_count += 1
    # The question variable (which is used for the math_answer_check function)
    # is reassigned to represent the second question. The user is prompted for
    # their answer, which updates the answer variable (which is also used by
    # the math_answer_check function).
    question = "\nQuestion 2: The average beehive can produce 60 pounds " \
               "(960 ounces) of honey in a productive season. \nA " \
               "beekeeper is filling eight ounce bottles of honey to sell " \
               "at a farmer's market.\nIf a hive produces 15.25 pounds of" \
               " honey this month, how many ounces are leftover if the " \
               "beekeeper fills as many bottles as possible? \nNote: " \
               "There are 16 ounces in one pound. \n"
    answer = input(question)
    # The user's input is checked to ensure it is an integer by passing
    # it through the function math_answer_valid()
    math_answer_valid(answer)
    # If the user answers the question correctly, they are congratulated
    # and will move on to the next question.
    if str(answer) == str(244 % 8):
        print("Awesome job! 4 ounces was the correct answer!")
    # If the user answers the question incorrectly, they are sent to the
    # function math_answer_check with the question and answer to
    # ensure they are able to eventually get the correct answer.
    else:
        print("\nOops, that's not right! Try again!")
        answer = 4
        math_answer_retry(question, answer)
    # Once the user comes up with the correct answer (4), one point is
    # added to the score_count variable
    score_count += 1
    # The question variable (which is used for the math_answer_check function)
    # is reassigned to represent the third question. The user is prompted for
    # their answer, which updates the answer variable (which is also used by
    # the math_answer_check function).
    question = "\nQuestion 3: In 2016, the United States imported 369 " \
               "million pounds of honey from foreign nations to meet " \
               "demand. \nA shipping box holds three layers of three by " \
               "three stacks of honey jars. How many jars will fit in " \
               "the box? \n"
    answer = input(question)
    # The user's input is checked to ensure it is an integer by passing
    # it through the function math_answer_valid()
    math_answer_valid(answer)
    # If the user answers the question correctly, they are congratulated
    # and will move on to the next question.
    if str(answer) == str(3 ** 3):
        print("Great! 27 jars was the correct answer!")
    # If the user answers the question incorrectly, they are sent to the
    # function math_answer_check with the question and answer to
    # ensure they are able to eventually get the correct answer.
    else:
        print("\nOops, that's not right! Try again!")
        answer = 27
        math_answer_retry(question, answer)
    # Once the user comes up with the correct answer (27), one point is
    # added to the score_count variable
    score_count += 1
    # The question variable (which is used for the math_answer_check function)
    # is reassigned to represent the fourth question. The user is prompted for
    # their answer, which updates the answer variable (which is also used by
    # the math_answer_check function).
    question = "\nQuestion 4: Warm Florida weather allows beekeepers to " \
               "harvest honey all year long. \nHowever, in colder places " \
               "honey needs to be stored at a temperature above 59 ºF " \
               "to prevent crystallization. \nIf a pantry is 48 ºF, how " \
               "many degrees warmer does it need to be to keep honey from " \
               "crystalizing? \n"
    answer = input(question)
    # The user's input is checked to ensure it is an integer by passing
    # it through the function math_answer_valid()
    math_answer_valid(answer)
    # If the user answers the question correctly, they are congratulated
    # and will move on to the next question.
    if str(answer) == str(60 - 48):
        print("Good work! 12ºF was the correct answer!")
    # If the user answers the question incorrectly, they are sent to the
    # function math_answer_check with the question and answer to
    # ensure they are able to eventually get the correct answer.
    else:
        print("\nOops, that's not right! Try again!")
        answer = 12
        math_answer_retry(question, answer)
    # Once the user comes up with the correct answer (12), one point is
    # added to the score_count variable
    score_count += 1
    # The question variable (which is used for the math_answer_check function)
    # is reassigned to represent the fifth question. The user is prompted for
    # their answer, which updates the answer variable (which is also used by
    # the math_answer_check function).
    question = "\nQuestion 5: A queen bee can lay up to 2,000 eggs in a " \
               "day. \nAbout how many eggs does a queen bee lay in an " \
               "hour? \nNote: Round your answer to the nearest whole " \
               "integer. \n"
    answer = input(question)
    # The user's input is checked to ensure it is an integer by passing
    # it through the function math_answer_valid()
    math_answer_valid(answer)
    # If the user answers the question correctly, they are congratulated
    # and will move on to the next question.
    if str(answer) == str(2000 // 24):
        print("Wonderful! 83 eggs an hour was the correct answer!")
    # If the user answers the question incorrectly, they are sent to the
    # function math_answer_check with the question and answer to
    # ensure they are able to eventually get the correct answer.
    else:
        print("\nOops, that's not right! Try again!")
        answer = 83
        math_answer_retry(question, answer)
    # Once the user comes up with the correct answer (83), one point is
    # added to the score_count variable
    score_count += 1
    # The question variable (which is used for the math_answer_check function)
    # is reassigned to represent the sixth question. The user is prompted for
    # their answer, which updates the answer variable (which is also used by
    # the math_answer_check function).
    question = "\nQuestion 6: A nuc is a small hive with three to five " \
               "frames of bees and a mated, accepted queen. \nNucs are " \
               "used by beekeepers to establish new beehive colonies. " \
               "\nIf a fully developed beehive has ten frames and a " \
               "beekeeper has eight fully developed hives,\nhow many " \
               "five-frame nucs can the beekeeper put together? \nKeep " \
               "in mind only five frames can be taken from each hive in " \
               "order for the developed hives to survive.  \n"
    answer = input(question)
    # The user's input is checked to ensure it is an integer by passing
    # it through the function math_answer_valid()
    math_answer_valid(answer)
    # If the user answers the question correctly, they are congratulated
    # and will move on to the next question.
    if str(answer) == str(40 / 5):
        print("That's it! 8 nucs was the correct answer!")
    # If the user answers the question incorrectly, they are sent to the
    # function math_answer_check with the question and answer to
    # ensure they are able to eventually get the correct answer.
    else:
        print("\nOops, that's not right! Try again!")
        answer = 8
        math_answer_retry(question, answer)
    # Once the user comes up with the correct answer (8), one point is
    # added to the score_count variable
    score_count += 1
    # The question variable (which is used for the math_answer_check function)
    # is reassigned to represent the seventh question. The user is prompted for
    # their answer, which updates the answer variable (which is also used by
    # the math_answer_check function).
    question = "\nQuestion 7: The population of a beehive fluctuates " \
               "depending on the season and availability of food. \nIn " \
               "colder months, beehive populations can drop below 20,000 " \
               "bees, \nwhile in warmer months beehives can reach a peak " \
               "population of up to 60,000 bees. \nIf a beehive has a " \
               "population of 50,000 honeybees and 7.5% of the population " \
               "is made up of drones (male bees), \nabout how many drones " \
               "are in the beehive?  \n"
    answer = input(question)
    # The user's input is checked to ensure it is an integer by passing
    # it through the function math_answer_valid()
    math_answer_valid(answer)
    # If the user answers the question correctly, they are congratulated
    # and will move on to the next question.
    if str(answer) == str(50000 * 0.075):
        print("Congratulations! 3,750 drones was the correct answer!")
    # If the user answers the question incorrectly, they are sent to the
    # function math_answer_check with the question and answer to
    # ensure they are able to eventually get the correct answer.
    else:
        print("\nOops, that's not right! Try again!")
        answer = 3750
        math_answer_retry(question, answer)
    # Once the user comes up with the correct answer (3750), one point is
    # added to the score_count variable
    score_count += 1
    # Once the user has correctly answered all seven questions, they are
    # congratulated by a "Winner! Winner! Winner!" message (created by using
    # the * string operator to concatenate copies of the same string together)
    # and congratulated fro scoring a perfect 7 out of 7 on the quiz!
    print("Winner! " * 3)
    print("\nThanks for playing! Your score was " + str(score_count)
          + " out of 7! I hope you learned something new.\n")
    # The user is asked if they would like to play another game
    play_more = input("Would you like to play another game? Y or N ")
    # The function valid_yes_or_no() verifies that play_more is
    # equivalent to a valid "Y" (Yes) or "N" (No) input by the user.
    play_more = valid_yes_or_no(play_more)
    # If the user does want to play another game, they are sent back to
    # the get_level() function.
    if play_more == "Y":
        print("\nAwesome to hear! Have fun!\n")
        get_level()
    # If the user does not want to play another game, the program
    # terminates with the exit() function
    else:
        print("\nThat's okay! Have a nice day!")


def honeybee_quiz():
    """The purpose of this function is to teach the user something new about
    honeybees through a series of honeybee-themed multiple choice questions.
    There are five total questions and the user has infinite attempts to get
    each question correct."""
    # The variable score_count will be used to keep track of the score.
    # It is assigned an initial value of 0.
    score_count = 0
    # The user is greeted and then asked the first question
    print("Time to test your knowledge!")
    # In order to ensure the question can be used as an argument in a function
    # later on (when improvements are made to the program), the question
    # variable is used to hold the first question.
    question = "\nHow can you tell the difference between a drone " \
               "(male bee), a worker bee, and a queen bee? \n " \
               "A. Drone bees have larger eyes than workers and the queen. " \
               "\n B. Queen bees are longer than all the other bees. " \
               "\n C. Worker bees are the only bees that leave the hive " \
               "to forage. \n D. All of the above. " \
               "\nPlease enter the letter of your choice."
    print(question)
    # The user is prompted for their answer, a choice of A, B, C, or D
    answer = input()
    # A while loop is used to ensure the user eventually selects the
    # correct answer (D).
    while answer != "D":
        print("\nOops! That's not correct! Try again.")
        answer = input("Enter the letter of your choice: ")
    # The user is congratulated and a point is added to score_count.
    print("\nGreat! The correct answer is D. Did you know drone bees "
          "are the only male bees in the hive?")
    score_count += 1
    # The question variable us updated with the second question string
    question = "\nWhat color is not visible to bees? \n A. Yellow \n " \
               "B. Red \n C. Blue \n D. Black \nPlease enter the " \
               "letter of your choice."
    # The question is printed and the user is prompted for an answer
    print(question)
    answer = input()
    # A while loop is used to ensure the user eventually selects the
    # correct answer (B).
    while answer != "B":
        print("\nOops! That's not correct! Try again.")
        answer = input("Enter the letter of your choice: ")
    # The user is congratulated and a point is added to score_count.
    print("\nAwesome! The correct answer is B. Beekeepers wear white "
          "because darker colors resemble predators (like bears)\n"
          "and are therefore more threatening to honeybees.")
    score_count += 1
    # The question variable us updated with the third question string
    question = "\nHow many species of bee exist in the world? \n " \
               "A. More than 20,000 \n B. More than 30,000 \n C. " \
               "More than 1,000 \n D. More than 400 \nPlease enter " \
               "the letter of your choice."
    # The question is printed and the user is prompted for an answer
    print(question)
    answer = input()
    # A while loop is used to ensure the user eventually selects the
    # correct answer (A).
    while answer != "A":
        print("\nOops! That's not correct! Try again.")
        answer = input("Enter the letter of your choice: ")
    # The user is congratulated and a point is added to score_count.
    print("\nGood job! The correct answer is A. Did you know that "
          "Osmia lignaria (or the Orchard mason bee) is blue?")
    score_count += 1
    # The question variable us updated with the fourth question string
    question = "\nWhat honeybee species is a good choice for beginners? \n " \
               "A. Africanized honeybee \n B. Varroa destructor \n C. " \
               "Italian honeybee \n D. Apis cerana \nPlease enter the " \
               "letter of your choice."
    # The question is printed and the user is prompted for an answer
    print(question)
    answer = input()
    # A while loop is used to ensure the user eventually selects the
    # correct answer (C).
    while answer != "C":
        print("\nOops! That's not correct! Try again.")
        answer = input("Enter the letter of your choice: ")
    # The user is congratulated and a point is added to score_count.
    print("\nPerfect! The correct answer is C. Varroa destructor "
          "(or Varroa mites) are external parasites that feed on honeybees.")
    score_count += 1
    # The question variable us updated with the fifth question string
    question = "\nHow long is the lifespan of a worker honeybee? \n " \
               "A. 3 days \n B. 5 to 7 months \n C. 6 months \n D. " \
               "3 to 5 months \nPlease enter the letter of your choice."
    # The question is printed and the user is prompted for an answer
    print(question)
    # A while loop is used to ensure the user eventually selects the
    # correct answer (B).
    while answer != "B":
        print("\nOops! That's not correct! Try again.")
        answer = input("Enter the letter of your choice: ")
    # The user is congratulated and a point is added to score_count.
    print("\nNice! The correct answer is B. Did you know worker "
          "honeybees literally work to death? Morbid, I know.")
    score_count += 1
    # Once the user successfully answers all 5 questions, a for loop counts
    # out each point by using the range of score_count. This results in a
    # similar outcome to the countdown loop seen in the Python textbook.
    print("\nCongratulations! You got...")
    for point_num in range(score_count):
        print(point_num + 1)
    print("out of 5 points!\n")
    # The user is asked if they would like to play another game
    play_more = input("Would you like to play another game? Y or N ")
    # The function valid_yes_or_no() verifies that play_more is
    # equivalent to a valid "Y" (Yes) or "N" (No) input by the user.
    play_more = valid_yes_or_no(play_more)
    # If the user does want to play another game, they are sent back to
    # the get_level() function.
    if play_more == "Y":
        print("\nAwesome to hear! Have fun!\n")
        get_level()
    # If the user does not want to play another game, the program
    # terminates with the exit() function
    else:
        print("\nThat's okay! Have a nice day!")


def honeybee_adventure():
    """The purpose of this function is to act as a placeholder for the third
    activity within this program. The program has not been completed yet, so
    currently this option is not available to play."""
    print("Time for an adventure!")
    confirm = input("When you're ready to start, press ENTER. ")
    # If the user successfully submits a blank statement the program
    # sends them back to the menu_select() function because the game
    # is not complete.
    if confirm == "":
        print("Sorry, this mini game is still under construction!")
        menu_select()
    # If the user does not submit a blank statement, the program
    # restarts the function.
    else:
        print("Oops, I guess you weren't ready!")
        honeybee_adventure()


def menu_select():
    """The purpose of this function is to prompt the user for the game they
    want to play. They have three options that redirect them to the above
    functions. Their options include: honeybee_math(), honeybee_quiz(), and
    honeybee_adventure()."""
    # The user is prompted for the game they want to play. There are three
    # options: Math, Quiz, and Adventure!
    print("\nPlease enter the number of your selection.")
    game_choice = input("Select One:\n 1)Math\n 2)Quiz "
                        "\n 3)Adventure (under construction)\n")
    # If the user selects "1" (Math), they are sent to the
    # honeybee_math() function
    if game_choice == "1":
        honeybee_math()
    # If the user selects "2" (Quiz), they are sent to the
    # honeybee_quiz() function
    elif game_choice == "2":
        honeybee_quiz()
    # If the user selects "3" (Adventure), they are sent to the
    # honeybee_adventure() function
    elif game_choice == "3":
        honeybee_adventure()
    # If the user inputs something other than a number on the menu
    # the function restarts
    else:
        print("Oops! That's not an option. Please enter a number "
              "corresponding with an option listed on the menu.")
        menu_select()


def get_level():
    """The purpose of this function is to welcome the user and guide them
    through the menu options in order to determine what kind of experience
    they would like. Currently, the user enters their personal level of
    honeybee knowledge on a scale of 1 to 5, but the program does not react
    the information in a significant way (yet)."""
    # The user is asked to self-evaluate their knowledge of honeybees
    # on a scale of 1 (very poor) to 5 (expert)
    print("How would you rate your knowledge of honeybees?")
    knowledge = input("1 (very poor) to 5 (expert)\n ")
    # The variable level is assigned an initial value
    level = 0
    # A try statement tests to ensure the user input can be converted
    # into an integer
    try:
        level = int(knowledge)
    # If the user input cannot be converted into an integer class,
    # the function restarts
    except ValueError:
        print("\nOops! Make sure you enter a number between 1 and 5.\n")
        get_level()
    # If the user inputs a level of 4 or higher, they are prompted to
    # confirm their selection and asked if they would like to learn more
    # (because even experts can learn new things!)
    if 4 <= level < 6:
        level_check = input("Are you sure that is correct? Y or N ")
        # The valid_yes_or_no() function passes the level_check input as an
        # argument to test and ensure the input was a valid "Y" or "N" input.
        level_check = valid_yes_or_no(level_check)
        if level_check == "Y":
            learn_more = input("Would you like to learn more? Y or N ")
            # The valid_yes_or_no() function passes the learn_more input
            # as an argument to test and ensure the input was a valid "Y"
            # or "N" input.
            learn_more = valid_yes_or_no(learn_more)
            # If the user confirms their rating was correct and
            # they want to learn more,
            # they are sent to the menu_select() function
            if level_check == "Y" and learn_more == "Y":
                print("Great! Let's play a game.")
                menu_select()
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
    elif 3 >= level > 0:
        level_check = input("Are you sure that is correct? Y or N ")
        # The valid_yes_or_no() function passes the level_check input as an
        # argument to test and ensure the input was a valid "Y" or "N" input.
        level_check = valid_yes_or_no(level_check)
        valid_yes_or_no(level_check)
        if level_check == "Y":
            learn_more = input("Would you like to learn more? Y or N ")
            # The valid_yes_or_no() function passes the learn_more input
            # as an argument to test and ensure the input was a valid "Y"
            # or "N" input.
            learn_more = valid_yes_or_no(learn_more)
            # If the user confirms their rating was correct and they want
            # to learn more,
            # they are sent to the menu_select() function
            if level_check == "Y" and learn_more == "Y":
                print("Awesome! Let's play a game to learn more.")
                menu_select()
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
    # If the user input at the initial prompt for a level from 1 to 5 is not
    # within the range of 1 to 5 (but it is an integer), the function
    # restarts because that is not a valid input
    else:
        print("\nOops! Make sure you enter a number between 1 and 5.\n")
        get_level()


# The player is prompted for their name
player_name = input("Buzz buzz...What's your name? ")
# The user is welcomed to the program and given a brief purpose statement.
# The name they input is concatenated with the welcome message using
# the + string operator
print("\nWelcome to my COP 1500 integration project, " + player_name + "!")
print("Today, we'll be learning about honeybees.")
print("Hopefully, you'll learn something new today!\n")
# The user is sent to the evaluation get_level() function to get started
get_level()
