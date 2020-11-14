import sys
import random
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPolygon

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        print(self.width(), self.height())
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        radius = random.randint(10, 150)
        qp.setBrush(QColor('#ffff00'))
        qp.drawEllipse(QPoint(x, y), radius, radius)
        self.do_paint = False


    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        print(self.x, self.y)
        self.setMouseTracking(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())