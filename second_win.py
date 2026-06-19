
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QApplication, QLineEdit, QHBoxLayout
from instr import * 
from PyQt5.QtCore import Qt

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


        self.label_time = QLabel("00:00:00")
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
        pass

    def next_click(self):
        self.hide()
        # self.final_win = 
