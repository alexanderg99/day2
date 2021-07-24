from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface


import requests

parameters = {

    "amount":10,
    "category":31,
    "type":"boolean"


}
response = requests.get('https://opentdb.com/api.php?amount=10&category=31&type=boolean',params = parameters)
response.raise_for_status()
data = response.json()
question_bank = data["results"]
question_list = []

for question in question_bank:
    if type(question) == dict:

        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_list.append(new_question)

quiz = QuizBrain(question_list)


quiz_ui = QuizInterface(quiz)
while quiz.still_has_questions():
    quiz.next_question()



