# Quiz App - Tutorial for Learn IT

# Questions and possible answers as well as the define for which answer is correct. Make note of the formatting and placement of symbols
questions = [
    {
        "question": "In which year did world war 2 end?",
        "options": ["A: 1946", "B: 1945", "C: 2019", "D: 1960"],
        "answer": "B"
    },

    {
        "question": "who wrote the famous play romeo and juliet?",
        "options": ["A: charles dicken", "B: jane austin", "C: mark twain", "D: william shakespeare"],
        "answer": "D"
    },

    {
        "question": "what is the capital city of afghanistan?",
        "options": ["A: kabul", "B: london", "C: gana", "D: Madrid"],
        "answer": "A"
    },

    {
        "question": "how many continents are there in the world?",
        "options": ["A: 5", "B: 6", "C: 12", "D: 7"],
        "answer": "D"
    },

    {
        "question": "who paited the famous artwork satrry night?",
        "options": ["A: claude monet", "B: leonardo da vinci", "C: vincent van gogh", "D: pablo picasso"],
        "answer": "C"
    },

    {
        "question": "what is the largest mammal in the world?",
        "options": ["A: elephant", "B: blue whale", "C: hippopotamus", "D: giraffe"],
        "answer": "B"
    },

    {
        "question": "which planet is known as the red planet?",
        "options": ["A: saturn", "B: jupiter", "C: mars", "D: venus"],
        "answer": "C"
    },

    {
        "question": "what is the cemical symbol for gold?",
        "options": ["A: au", "B: pt", "C: ag", "D: go"],
        "answer": "A"
    },

    {
        "question": "who is the author of the harry potter book series?",
        "options": ["A: stephan king", "B: geprge r.r martin", "C: j.k. rowling", "D: tolkien"],
        "answer": "C"
    },

    {
        "question": "what is the tallest mpuntain in the world?",
        "options": ["A: k2", "B: mount kilimanjaro", "C: mount mckunley", "D: maount everest"],
        "answer": "D"
    },
    # You can remove this comment or move it down and add more questions. You should enclose each question in their own {} brackets.
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

# Run the quiz
run_quiz(questions)