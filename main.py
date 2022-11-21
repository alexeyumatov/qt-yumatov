from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui')
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        pass
