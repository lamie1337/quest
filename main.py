import sys
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.setWindowTitle('Круги')
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        xx = randint(1, 400)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(randint(1, 800), randint(1, 800), xx, xx)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
