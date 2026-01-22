def run_quiz():
    questions = [
        {
            "question": "Question 1",
            "options": ["1", "2", "3", "4"],
            "answer": "2",
        },
        {
            "question": "Question 2",
            "options": ["1", "2", "3", "4"],
            "answer": "2",
        },
        {
            "question": "Question 3",
            "options": ["1", "2", "3", "4"],
            "answer": "2",
        },
        {
            "question": "Question 4",
            "options": ["1", "2", "3", "4"],
            "answer": "3",
        },
        {
            "question": "Question 5",
            "options": ["1", "2", "3", "4"],
            "answer": "3",
        },
    ]

    score = 0
    index = 0

    print("Welcome to the Quiz!")
    print("Answer using 1, 2, 3, or 4.")

    while index < len(questions):
        q = questions[index]

        print(f"\nQuestion {index + 1}: {q['question']}")
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer: ").strip()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

        index += 1

    print("\nQuiz Complete!")
    print(f"You scored {score} out of {len(questions)}.")
    print("Thank you for playing!")


run_quiz()
