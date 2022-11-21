import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'UI.ui', self)
        self.click_pB.clicked.connect(self.btn_clicked)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            for _ in range(7):
                x, y = randint(30, 300), randint(30, 350)
                radius = randint(30, 100)
                qp.drawEllipse(x, y, radius, radius)
            qp.end()

    def btn_clicked(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
