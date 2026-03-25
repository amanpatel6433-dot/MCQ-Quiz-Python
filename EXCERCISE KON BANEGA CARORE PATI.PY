# 
def ask_question(question, options, correct):
    print("\n" + question)

    for option in options:
        print(option)

    user = input("Answer (A/B/C/D): ").upper()

    if user == correct:
        print("Correct ✅")
        return 1
    else:
        print("Wrong ❌")
        return 0

questions = [
    ("2 + 2 = ?", ["A. 3", "B. 4", "C. 5", "D. 6"], "B"),
    ("Capital of India?", ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"], "B"),
    ("5 * 3 = ?", ["A. 10", "B. 15", "C. 20", "D. 25"], "B")
]

score = 0

for q, opts, ans in questions:
    score += ask_question(q, opts, ans)

print("\nYour final score is:", score)