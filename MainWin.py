from PyQt5.Qt import *
import sys

import datetime


class newwindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.resize(600,300)
        self.lb=QLabel(self)
        # global date
        # self.lb.setText(date)
    def showdateinfo(self,dateinfo):
        self.setWindowTitle(dateinfo)


class mainwindow(QMainWindow):
    def __init__(self,targetmonth):
        super().__init__()
        self.setWindowTitle('main')
        self.resize(600,400)
        menubar = self.menuBar()
        filemenu=menubar.addMenu('文件')
        filemenu.addAction('导出')

        labletext = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        x = 0
        for text in labletext:
            self.lable = QLabel(self)
            self.lable.resize(100, 50)
            self.lable.move(x + 30, 50)
            self.lable.setText(text)
            x = x + 100

        # targetmonth=datetime.date.today()
        firstdate=targetmonth.replace(day=1)
        print(firstdate)
        self.lb1=QLabel(self)
        self.lb1.resize(50,20)
        self.lb1.move(0,20)
        self.lb1.setText(str(targetmonth.year))

        self.sp2=QSpinBox(self)
        self.sp2.setMaximum(12)
        self.sp2.setMinimum(1)
        self.sp2.resize(50,20)
        self.sp2.move(50,20)
        self.sp2.setValue(targetmonth.month)
        self.sp2.valueChanged.connect(self.spvc)




        self.d={}
        for i in range(1,43):
            self.d['button'+str(i)]=QPushButton(self)
            self.d['button' + str(i)].setText(str(datetime.date.fromordinal(firstdate.toordinal() + i-1)))
            print(i,firstdate,self.d['button' + str(i)].text())

            # self.d['text' + str(i)]=(str(datetime.date.fromordinal(datetime.date.today().toordinal() + i-1)))
            self.d['button' + str(i)].resize(100,50)

            x=((i-1)%7)*100
            y=(i-1)//7*50+100
            self.d['button'+str(i)].move(x,y)

            self.d['button' + str(i)].clicked.connect(self.btnclicked)
        self.new=newwindow()


    # 注意def 的对齐位置！！！！！此处时定义该类的一个方法！！！！！
    def btnclicked(self):
        dateinfo=self.sender().text()
        print(dateinfo)
        self.new.showdateinfo(dateinfo)
        self.new.show()


    def spvc(self):
        value = self.sender().value()
        a=datetime.date(2021,value,1)
        print(a)
        # main.targetmonth=value
        window=mainwindow(a)
        window.show()




pass


if __name__ == '__main__':
    import datetime
    app = QApplication(sys.argv)
    targetmonth = datetime.date.today()
    # targetmonth=datetime.date(2022,12,12)
    window =mainwindow(targetmonth)
    window.show()
    sys.exit(app.exec_())