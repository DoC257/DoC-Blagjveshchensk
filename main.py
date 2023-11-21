from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint
from random import randint
import sys
from math import sin, cos, pi


class Supermatism(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.qp = QPainter
        self.coord = tuple()
        self.ind = False

    def initUI(self):
        self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle("Рисование")
        self.typefigure = None

    def mousePressEvent(self, event):
        self.coord = (event.x(), event.y())
        if event.button() == Qt.LeftButton:
            self.typefigure = "circle"
            self.drawf()
        elif event.button() == Qt.RightButton:
            self.typefigure = "square"
            self.drawf()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.typefigure = "triangle"
            self.drawf()

    def mouseMoveEvent(self, event):
        self.coord = (event.x(), event.y())

    def drawf(self):
        self.ind = True
        self.update()

    def paintEvent(self, event):
        if self.ind:
            self.qp = QPainter()
            self.qp.begin(self)
            self.drawfigure()
            self.qp.end()

    def drawfigure(self):
        if self.typefigure == "triangle":
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x, y = self.coord
            a = randint(20, 100)
            coords = [QPoint(x, y - a),
                      QPoint(int(x + cos(7 * pi / 6) * a),
                             int(y - sin(7 * pi / 6) * a)),
                      QPoint(int(x + cos(11 * pi / 6) * a),
                             int(y - sin(11 * pi / 6) * a))]
            self.qp.drawPolygon(coords)
        elif self.typefigure == "circle":
            r = randint(0, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawEllipse(int(self.coord[0] - r / 2), int(self.coord[1] - r / 2), r, r)
        elif self.typefigure == "square":
            a = randint(0, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawRect(int(self.coord[0] - a / 2), int(self.coord[1] - a / 2), a, a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Supermatism()
    window.show()
    sys.exit(app.exec())
