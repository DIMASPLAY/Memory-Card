from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append( Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append( Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

app = QApplication([])
main_win = QWidget()
main_win.resize(400, 300)
main_win.show()
main_win.setWindowTitle('Memory Card')
mainText = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox('Варианты ответов')
ans1 = QRadioButton('2005')
ans2 = QRadioButton('2010')
ans3 = QRadioButton('2015')
ans4 = QRadioButton('2020')
answer = QPushButton('Ответить')

main = QVBoxLayout()
RadioGroup = QButtonGroup()
RadioGroup.addButton(ans1)
RadioGroup.addButton(ans2)
RadioGroup.addButton(ans3)
RadioGroup.addButton(ans4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(mainText, alignment = Qt.AlignCenter)
layout_ans2.addWidget(ans1)
layout_ans2.addWidget(ans2)
layout_ans3.addWidget(ans3)
layout_ans3.addWidget(ans4)
line2.addWidget(RadioGroupBox)
line3.addWidget(answer, alignment = Qt.AlignHCenter | Qt.AlignVCenter, stretch = 20)

layout_ans2.setSpacing(15)
layout_ans3.setSpacing(15)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
main.addLayout(line1)
main.addLayout(line2)
main.addLayout(line3)
line3.addStretch(2)

RadioGroupBox.setLayout(layout_ans1)
main_win.setLayout(main)

#RadioGroupBox.hide()
AnsGroupBox = QGroupBox('Результат теста:')
result = QLabel('Правильно\неправильно')
correct = QLabel('тут типа правильный ответ')
layout_result = QVBoxLayout()
layout_result.addWidget(result)
layout_result.addWidget(correct, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
AnsGroupBox.setLayout(layout_result)
answer.setText('Следующий вопрос')

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [ans1, ans2, ans3, ans4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    mainText.setText(q.question)
    correct.setText(q.right_answer)
    show_question()

def show_correct(right_answer):
    correct.setText(right_answer)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')

def next_question():
    main_win.cur_question = main_win.cur_question + 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)

def click_OK():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()


answer.clicked.connect(click_OK)
main_win.cur_question = -1
next_question()
app.exec_()