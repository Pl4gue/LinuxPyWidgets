import sys
import time
from random import randint
from PyQt4.QtGui import *
from PyQt4 import QtCore


# PyQt qtClockScreensaver screen saver

class ClockWidget(QWidget):
    screen_width = 0
    screen_height = 0

    def __init__(self, screen_width, screen_height):
        QWidget.__init__(self)
        self.lblFont = QFont()
        self.lbl = QLabel(self)
        self.timer = QtCore.QTimer(self)
        self.moveTimer = QtCore.QTimer(self)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.initUI()
        self.showFullScreen()

    def initUI(self):
        self.timer.timeout.connect(self.time)
        self.timer.start(10)

        self.moveTimer.timeout.connect(self.moveTime)
        self.moveTimer.start(3000)

        self.lblFont.setFamily("Arial Black")
        self.lblFont.setPointSize(72)
        self.lblFont.setBold(True)
        self.lblFont.setWeight(75)
        self.lbl.setFont(self.lblFont)
        self.lbl.resize(450, 100)
        self.lbl.move(randint(0, self.screen_width - 475),  # 25px margin
                      randint(0, self.screen_height - 125))

    def moveTime(self):
        self.lbl.move(randint(0, self.screen_width - 475),  # 25px margin
                      randint(0, self.screen_height - 125))

    def time(self):
        self.lbl.setText(time.strftime("%H:%M:%S"))

    def mousePressEvent(self, event):
        exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ClockWidget(app.desktop().screenGeometry().width(),
                         app.desktop().screenGeometry().height())
    widget.show()
    sys.exit(app.exec_())
