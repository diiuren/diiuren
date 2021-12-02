from MainWind import *
from Monitor import *
from Vedio import *
from Warning import *
from Check import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys

class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog()
        self.child.setupUi(self)

class childWindow2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog2()
        self.child.setupUi(self)

class childWindow3(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog3()
        self.child.setupUi(self)

class childWindow4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog4()
        self.child.setupUi(self)

if __name__=='__main__':

    app=QApplication(sys.argv)
    window=parentWindow()
    child=childWindow()
    child2 = childWindow2()
    child3 = childWindow3()
    child4 = childWindow4()

    #通过toolButton将两个窗体关联
    btn=window.main_ui.toolButton
    btn2=window.main_ui.toolButton_2
    btn3 = window.main_ui.toolButton_3
    btn4 = window.main_ui.toolButton_4

    btn.clicked.connect(child.show)
    btn2.clicked.connect(child2.show)
    btn3.clicked.connect(child3.show)
    btn4.clicked.connect(child4.show)

    # 显示
    window.show()
    sys.exit(app.exec_())
