import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_counter = 0
        self.setWindowTitle("My App")
        self.setMaximumSize(QSize(500, 700))
        self.setMinimumSize(QSize(500, 700))

        #main widget
        main_widget  = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        main_widget.setStyleSheet("background-color:#1E90FFf;")
        self.setCentralWidget(main_widget)

        #top layout
        top_layout = QVBoxLayout()
        title = QLabel("TO DO TASKS")
        title.setStyleSheet("""
          font-family: "Segoe UI", Arial, sans-serif;
          font-size: 26px;
          font-weight: bold;
          color: #ffffff;""")
        
        top_layout.addWidget(title)

        input_layout = QHBoxLayout()
        self.input  = QLineEdit()
        self.input.setPlaceholderText("Enter text")
        self.input.setStyleSheet("""
            font-size: 16px;
            padding: 8px 12px;  
            border-radius: 8px;
            border: 1px solid #888;
            background-color: #f0f0f0;
            color: #000000;""")

        button = QPushButton("add item")
        button.setStyleSheet("""
            
            QPushButton {
                background-color: Green;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
    
        """)
        
        input_layout.addWidget(self.input)
        input_layout.addWidget(button)

        top_layout.addLayout(input_layout)
        main_layout.addLayout(top_layout)

        self.task_list = QListWidget()
        self.task_list.setStyleSheet("""background-color: #2c2c34;
        color: #ffffff;
        font-size: 16px;
        border-radius: 8px;
        padding: 5px;
        """)
        main_layout.addWidget(self.task_list)

        button_delete = QPushButton("Delete a task")
        button_delete.setStyleSheet("""font-size: 26px;
        padding: 8px 16px;
        border-radius: 8px;
        background-color: #E74C3C;  /* rouge vif pour danger/supprimer */
        color: white;
        border: none;""")
        


        main_layout.addWidget(button_delete)



        button.clicked.connect(self.add)
        button_delete.clicked.connect(self.delete)
        

    def add(self, task_list):
        
        text = self.input.text()
       
        if text:
            self.task_counter +=1
            self.task_list.addItem(str(self.task_counter)+'.'+ text)
            self.input.clear()
            
          
    
    def delete(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
           row = self.task_list.row(selected_item)
           self.task_list.takeItem(row)

application = QApplication(sys.argv)
window = MainWindow()
window.show()
application.exec()
