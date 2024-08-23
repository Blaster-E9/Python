
def playgame():

    print("Welcome to to this quiz game!")

    questions = ("What is the capital of France: ",
            "How many elements are in the periodic table: ",
            "Which planet in the solar system is the hottest: ",
            "Which animal lays the largest eggs: ",
            "How many bones are in the human body: ")

    options = (("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
           ("A. 116", "B. 118", "C. 115", "D. 117"),
           ("A. Sun", "B. Jupiter", "C. Venus", "D. Mercury"),
           ("A. Ostrich", "B. Chicken", "C. Cassowaries", "D. Emu"),
           ("A. 186", "B. 206", "C. 230", "D. 270"))

    answers = (("C"),
           ("B"),
           ("C"),
           ("A"),
           ("B"))


    guesses = []
    score = 0
    question_num = 0



    for question in questions:
        print("-----------------------------------------")
        print(question)
        for option in options[question_num]:
            print(option)


        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT")

        else:
            print("INCORRECT")
            print(f"Correct answer was {answers[question_num]}")
        
        question_num += 1
        
    
    


    print("-----------------------------------------")
    print("-----------------RESULTS-----------------")
    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"you scored {score}% out of 100%. \n Thank you for playing this quiz")

playgame()

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

while play_again():
    playgame()

print("Thank you for playing!")




