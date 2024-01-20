import json
from difflib import get_close_matches

def load_QA(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[dict]) -> str | None:
    q_list = [q["question"] for q in questions]
    matches: list = get_close_matches(user_question, q_list, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, QA: dict) -> str | None:
    for q in QA["questions"]:
        if q["question"] == question:
            return q["answers"]

def chatbot():
    QA: dict = load_QA('C:\\Users\\Karthik\\Desktop\\QA.json')
    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(user_input, QA["questions"])

        if best_match:
            answer: str = get_answer_for_question(best_match, QA)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip:')

            if new_answer.lower() != 'skip':
                QA["questions"].append({"question": user_input, "answers": [new_answer]})
                save_knowledge('C:\\Users\\Karthik\\Desktop\\QA.json', QA)
                print('Bot: Thank you! I learned a new response.')

if __name__ == '__main__':
    chatbot()