from PyQt5.Qt import *
import sys
import datetime
import MainWin

app=QApplication(sys.argv)

targetmonth=datetime.date.today()

def showwindow(tm):
    window=MainWin.mainwindow(tm)
    window.show()
    sys.exit(app.exec_())

showwindow(targetmonth)

