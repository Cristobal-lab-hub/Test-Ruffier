from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QApplication, QLineEdit, QHBoxLayout
from instr import * 
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont
from final_win import FinalWin


class Datos():
    def __init__(self, name, age, test_1, test_2, test_3):
        self.name = name
        self.age = int(age)
        self.test_1 = int(test_1)
        self.test_2 = int(test_2)
        self.test_3 = int(test_3)



class testWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connection()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.label_name = QLabel(txt_name)
        self.input_name = QLineEdit(txt_hintname)
        self.input_name.setPlaceholderText(txt_hintname)
        self.label_age = QLabel(txt_age)
        self.input_age = QLineEdit(txt_hintage)

        self.test1_inst = QLabel(txt_test1)
        self.test1_button = QPushButton(txt_starttest1)
        self.rest1_restult = QLineEdit(txt_hinttest1)

        self.test2_inst = QLabel(txt_test2)
        self.test2_button = QPushButton(txt_starttest2)

        self.test3_inst = QLabel(txt_test3)
        self.test3_button = QPushButton(txt_starttest3)

        self.rest2_restult = QLineEdit(txt_hinttest2)
        self.rest3_restult = QLineEdit(txt_hinttest3)



        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.label_name, alignment= Qt.AlignLeft)
        self.left_layout.addWidget(self.input_name, alignment= Qt.AlignLeft)
        self.left_layout.addWidget(self.label_age, alignment= Qt.AlignLeft)
        self.left_layout.addWidget(self.input_age, alignment= Qt.AlignLeft)

        self.left_layout.addWidget(self.test1_inst, alignment= Qt.AlignLeft)
        self.left_layout.addWidget(self.test1_button, alignment= Qt.AlignLeft)
        self.left_layout.addWidget(self.rest1_restult, alignment= Qt.AlignLeft)

        self.left_layout.addWidget(self.test2_inst, alignment= Qt.AlignLeft)
        self.left_layout.addWidget(self.test2_button, alignment= Qt.AlignLeft)
        

        self.left_layout.addWidget(self.test3_inst, alignment= Qt.AlignLeft)
        self.left_layout.addWidget(self.test3_button, alignment= Qt.AlignLeft)
        self.left_layout.addWidget(self.rest2_restult, alignment= Qt.AlignLeft)
        self.left_layout.addWidget(self.rest3_restult, alignment= Qt.AlignLeft)

        self.label_time = QLabel(txt_timer)
        self.label_time.setFont(QFont("Arian", 35, QFont.Bold))

        self.label_time = QLabel(txt_timer)
        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.label_time)


        self.button = QPushButton("Siguiente")

        self.h_layout = QHBoxLayout()
        self.h_layout.addLayout(self.left_layout)
        self.h_layout.addLayout(self.right_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.h_layout)
        self.main_layout.addWidget(self.button)



        self.setLayout(self.main_layout)


    def connection(self):
        self.test1_button.clicked.connect(self.timer_test)
        self.test2_button.clicked.connect(self.timer_sits)
        self.test3_button.clicked.connect(self.timer_final)
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        results = Datos(self.input_name.text(), self.input_age.text(), self.rest1_restult.text(), self.rest2_restult.text(), self.rest3_restult.text())
        self.hide()
        self.final = FinalWin(results)
        
        

    def timer_test(self):
        self.time = QTime(0,0,15)
        self.label_time.setText(self.time.toString())
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1event)
        self.timer.start(1000)
        #self.timer.stop()

    def timer1event(self):
        self.time = self.time.addSecs(-1)
        self.label_time.setText(self.time.toString())
        if self.time.toString() == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        self.time = QTime(0,0,30)
        self.label_time.setText(self.time.toString()[6:8])
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2event)
        self.timer.start(1500)

    def timer2event(self):
        self.time = self.time.addSecs(-1)
        self.label_time.setText(self.time.toString()[6:8])
        if self.time.toString() == "00:00:00":
            self.timer.stop()


    def timer_final(self):
        self.time = QTime(0,1,0)
        self.label_time.setText(self.time.toString())
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3event)
        self.timer.start(1000)

    def timer3event(self):
        self.time = self.time.addSecs(-1)
        self.label_time.setText(self.time.toString())
        if self.time.toString() == "00:00:59":
            self.label_time.setStyleSheet("color: rgb(0,255,0)")
        elif self.time.toString() == "00:00:44":
            self.label_time.setStyleSheet("color: rgb(0,0,0)")
        elif self.time.toString() == "00:00:15":
            self.label_time.setStyleSheet("color: rgb(0,255,0)")
        if self.time.toString() == "00:00:00":
            self.timer.stop()
            self.label_time.setStyleSheet("color: rgb(0,0,0)")
