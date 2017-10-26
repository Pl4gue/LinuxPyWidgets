import sys
from PyQt4 import QtGui, QtCore

app = 0
calendar = 0


class CalendarTrayIcon(QtGui.QSystemTrayIcon):
    menu = ''

    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        global calendar
        calendar = CalendarWidget()
        self.menu = CalendarTrayContextMenu(parent)
        self.setContextMenu(self.menu)


class CalendarTrayContextMenu(QtGui.QMenu):
    quitAction = ''
    showCalendarAction = ''
    menu = ''

    def __init__(self, parent=None):
        QtGui.QMenu.__init__(self, parent)
        self.menu = QtGui.QMenu(self)
        self.quitAction = self.menu.addAction("Quit")
        self.showCalendarAction = self.menu.addAction("Show calendar")
        self.hideCalendarAction = self.menu.addAction("Hide calendar")

    def contextMenuEvent(self, event):
        action = self.menu.exec_(self.mapToGlobal(event.pos()))
        if action == self.quitAction:
            app.quit()
        elif action == self.showCalendarAction:
            calendar.show()
        elif action == self.hideCalendarAction:
            calendar.hide()


class CalendarWidget(QtGui.QWidget):
    def __init__(self):
        super(CalendarWidget, self).__init__()
        self.initUI()

    def initUI(self):
        print("initUI")
        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.setFirstDayOfWeek(QtCore.Qt.Monday)
        cal.clicked[QtCore.QDate].connect(self.showDate)

        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 300, 300)
        self.setMaximumSize(300, 300)
        self.setWindowTitle('Calendar')

    def showDate(self, date):
        self.lbl.setText(date.toString())

    def closeEvent(self, QCloseEvent):
        self.hide()


def main():
    global app
    app = QtGui.QApplication(sys.argv)
    app.aboutToQuit.connect(exitHandler)
    app.setQuitOnLastWindowClosed(False)

    w = QtGui.QWidget()
    trayIcon = CalendarTrayIcon(QtGui.QIcon("calendar-icon.png"), w)

    trayIcon.show()

    sys.exit(app.exec_())


def exitHandler():
    print("hiding")
    calendar.hide()


if __name__ == '__main__':
    main()
