import random
import time

questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Mercury"],
        "answer": "A"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 0"],
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Van Gogh", "B. Picasso", "C. Da Vinci", "D. Michelangelo"],
        "answer": "C"
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Hydrogen", "D. Nitrogen"],
        "answer": "B"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 8", "C. 7", "D. 9"],
        "answer": "B"
    },
    {
        "question": "Who is known as the father of computers?",
        "options": ["A. Alan Turing", "B. Charles Babbage", "C. Steve Jobs", "D. Bill Gates"],
        "answer": "B"
    },
    {
        "question": "Which language is used to create web pages?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "Which country won the FIFA World Cup 2022?",
        "options": ["A. Germany", "B. France", "C. Brazil", "D. Argentina"],
        "answer": "D"
    }
]

def ask_question(q, q_num):
    print(f"\nQuestion {q_num}: {q['question']}")
    for option in q['options']:
        print(option)
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    while ans not in ['A', 'B', 'C', 'D']:
        ans = input("Please enter A, B, C, or D: ").strip().upper()
    return ans == q['answer']

def quiz_game():
    print("\n=== Welcome to the Ultimate Quiz Game ===\n")
    time.sleep(1)
    score = 0
    correct = 0
    wrong = 0
    random.shuffle(questions)

    for i, q in enumerate(questions, 1):
        if ask_question(q, i):
            print("✅ Correct!\n")
            score += 1
            correct += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")
            wrong += 1
        time.sleep(1)

    print("=== Quiz Complete! ===")
    print(f"✅ Correct Answers: {correct}")
    print(f"❌ Wrong Answers: {wrong}")
    print(f"🎯 Final Score: {score}/{len(questions)}")
    print("Thanks for playing!\n")

if __name__ == "__main__":
    quiz_game()
