from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("prog_pyqt5/tracker.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def on_click():
    print(form.plainTextEdit.toPlainText())
    print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    print("Clicked!!!")
    #print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    #date = QDate(2022, 9, 17)
    #form.calendarWidget.setSelectedDate(date)


def on_click_calendar():
    global start_date, calc_date
    #print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    form.dateEdit.setDate(form.calendarWidget.selectedDate())
    calc_date = form.calendarWidget.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    form.label_3.setText("До наступления события осталось : %s дней" % delta_days)

def on_dateedit_change():
    #print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    form.calendarWidget.setSelectedDate(form.dateEdit.date())
    calc_date = form.dateEdit.date()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    form.label_3.setText("До наступления события осталось : %s дней" % delta_days)


form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateedit_change)
#form.label.setText('Чкркз main')


start_date = form.calendarWidget.selectedDate()
calc_date = form.calendarWidget.selectedDate()
form.label.setText("<html><head/><body><p align=\"center\">Трекер события от: %s</p></body></html>" % start_date.toString('dd-MM-yyyy')) #"<html><head/><body><p align=\"center\">Трекер события !@#</p></body></html>")
on_click_calendar()


app.exec_()




'''
from tracker import *

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.label.setText('Чкркз main')

sys.exit(app.exec_())
'''