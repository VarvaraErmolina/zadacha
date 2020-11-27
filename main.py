import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(500, 300)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        x = random.randint(10, 490)
        y = random.randint(10, 290)
        size = random.randint(1, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, size, size)
        x2 = random.randint(10, 490)
        y2 = random.randint(10, 290)
        size2 = random.randint(1, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x2, y2, size2, size2)
        x3 = random.randint(10, 490)
        y3 = random.randint(10, 290)
        size3 = random.randint(1, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x3, y3, size3, size3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
