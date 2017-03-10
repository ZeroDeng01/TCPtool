# -*- coding:utf-8 -*-
import win32com
import socket
import sys
import ConfigParser
import time
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setEnabled(True)
        Form.resize(1293, 643)
        Form.setMinimumSize(QtCore.QSize(1293, 643))
        Form.setMaximumSize(QtCore.QSize(1293, 643))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 620, 91, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 271, 371))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(230, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.DATETIME = QtGui.QTimeEdit(self.groupBox)
        self.DATETIME.setGeometry(QtCore.QRect(111, 206, 141, 22))
        self.DATETIME.setTime(QtCore.QTime(10, 10, 10))
        self.DATETIME.setObjectName(_fromUtf8("DATETIME"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(11, 146, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(11, 177, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.NUM = QtGui.QLineEdit(self.groupBox)
        self.NUM.setGeometry(QtCore.QRect(111, 114, 141, 21))
        self.NUM.setObjectName(_fromUtf8("NUM"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(11, 49, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(11, 266, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.HOST = QtGui.QLineEdit(self.groupBox)
        self.HOST.setEnabled(True)
        self.HOST.setGeometry(QtCore.QRect(111, 24, 141, 21))
        self.HOST.setObjectName(_fromUtf8("HOST"))
        self.WARING = QtGui.QComboBox(self.groupBox)
        self.WARING.setGeometry(QtCore.QRect(111, 295, 141, 22))
        self.WARING.setObjectName(_fromUtf8("WARING"))
        self.WARING.addItem(_fromUtf8(""))
        self.WARING.addItem(_fromUtf8(""))
        self.WARING.addItem(_fromUtf8(""))
        self.E = QtGui.QLineEdit(self.groupBox)
        self.E.setGeometry(QtCore.QRect(111, 240, 141, 20))
        self.E.setObjectName(_fromUtf8("E"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(11, 114, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(11, 296, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.Start = QtGui.QPushButton(self.groupBox)
        self.Start.setGeometry(QtCore.QRect(13, 334, 101, 23))
        self.Start.setObjectName(_fromUtf8("Start"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(11, 81, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.DATE = QtGui.QDateEdit(self.groupBox)
        self.DATE.setGeometry(QtCore.QRect(111, 176, 141, 22))
        self.DATE.setDate(QtCore.QDate(2017, 3, 10))
        self.DATE.setObjectName(_fromUtf8("DATE"))
        self.TIME = QtGui.QLineEdit(self.groupBox)
        self.TIME.setGeometry(QtCore.QRect(111, 81, 111, 21))
        self.TIME.setObjectName(_fromUtf8("TIME"))
        self.Exit = QtGui.QPushButton(self.groupBox)
        self.Exit.setGeometry(QtCore.QRect(151, 334, 101, 23))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(13, 14, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.PORT = QtGui.QLineEdit(self.groupBox)
        self.PORT.setGeometry(QtCore.QRect(111, 52, 141, 21))
        self.PORT.setObjectName(_fromUtf8("PORT"))
        self.N = QtGui.QLineEdit(self.groupBox)
        self.N.setGeometry(QtCore.QRect(111, 267, 141, 20))
        self.N.setObjectName(_fromUtf8("N"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(11, 237, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(11, 207, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.ID = QtGui.QLineEdit(self.groupBox)
        self.ID.setGeometry(QtCore.QRect(111, 144, 141, 20))
        self.ID.setObjectName(_fromUtf8("ID"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 400, 271, 221))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.STATUS = QtGui.QPlainTextEdit(self.groupBox_2)
        self.STATUS.setEnabled(True)
        self.STATUS.setGeometry(QtCore.QRect(10, 20, 251, 191))
        self.STATUS.setObjectName(_fromUtf8("STATUS"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 20, 981, 601))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.webView = QtWebKit.QWebView(self.groupBox_3)
        self.webView.setGeometry(QtCore.QRect(10, 20, 961, 561))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://api.map.baidu.com/lbsapi/getpoint/")))
        self.webView.setObjectName(_fromUtf8("webView"))

        self.retranslateUi(Form)
        self.WARING.setCurrentIndex(0)
        QtCore.QObject.connect(self.Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Start.clicked.connect(self.tcp)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "大爱定位器测试工具v1.0", None))
        self.label_8.setText(_translate("Form", "作者：ZeroDeng", None))
        self.groupBox.setTitle(_translate("Form", "定位器配置", None))
        self.label_5.setText(_translate("Form", "秒", None))
        self.DATETIME.setDisplayFormat(_translate("Form", "HHmmss", None))
        self.label_6.setText(_translate("Form", "设备编号", None))
        self.label_9.setText(_translate("Form", "定位日期", None))
        self.NUM.setText(_translate("Form", "1", None))
        self.label_2.setText(_translate("Form", "端          口", None))
        self.label_12.setText(_translate("Form", "纬           度", None))
        self.HOST.setText(_translate("Form", "127.0.0.1", None))
        self.WARING.setItemText(0, _translate("Form", "正常", None))
        self.WARING.setItemText(1, _translate("Form", "低电", None))
        self.WARING.setItemText(2, _translate("Form", "拆除", None))
        self.label_4.setText(_translate("Form", "发包次数", None))
        self.label_13.setText(_translate("Form", "报警状态", None))
        self.Start.setText(_translate("Form", "开始模拟", None))
        self.label_3.setText(_translate("Form", "间隔时间", None))
        self.DATE.setDisplayFormat(_translate("Form", "ddMMyy", None))
        self.TIME.setText(_translate("Form", "1", None))
        self.Exit.setText(_translate("Form", "退出", None))
        self.label.setText(_translate("Form", "Sever   IP", None))
        self.PORT.setText(_translate("Form", "1099", None))
        self.label_11.setText(_translate("Form", "经           度", None))
        self.label_10.setText(_translate("Form", "定位时间", None))
        self.ID.setText(_translate("Form", "801160900001", None))
        self.groupBox_2.setTitle(_translate("Form", "返回信息", None))
        self.groupBox_3.setTitle(_translate("Form", "坐标查看", None))



    #运行tcp
    def TCP(self):
        HOST = str(self.HOST.text())  # ip
        PORT = int(self.PORT.text())  # 端口
        ID = str(self.ID.text())
        Date = str(self.DATE.text())
        DateTime = str(self.DATETIME.text())
        E = str(self.E.text())
        N = str(self.N.text())
        print E
        print N
        War = str(self.WARING.currentIndex())
        WarStr = ''
        if (War=="0"):
            WarStr = 'B1'
        if (War=="1"):
            WarStr = 'B0'
        if (War=="2"):
            WarStr = 'WN'

        TEXT = "$%s,A,D:%s,T:%s,E,%s,N,%s*%s#"%(ID,Date,DateTime,E,N,WarStr)                # 发送内容
        s = None
        for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                s = socket.socket(af, socktype, proto)
            except socket.error, msg:
                s = None
                continue
            try:
                s.connect(sa)
            except socket.error, msg:
                s.close()
                s = None
                continue
            break
        if s is None:
            print u'连接失败'
            StatusStr = u"连接失败"
            self.STATUS.setPlainText(StatusStr)
        s.sendall(TEXT)  # 1）发送数据
        data = s.recv(1024)  # 4）接受服务器回显的数据
        s.close()
        return repr(data)  # 打印输出

    def tcp(self):
        NUM = int(self.NUM.text())  # 发包次数
        TIME = int(self.TIME.text())  # 发包次数
        i = 1
        StatusStr = ""
        while (i <= int(NUM)):
            date = self.TCP()
            print u'系统进行第' + str(i) + u'次发包'
            print u'接收到的数据是：'+ str(date)
            StatusStr = u'系统第' + str(i) + u'次发包\n' + u'接收到的数据是：'+ date + '\n\n'+ StatusStr
            self.STATUS.setPlainText(StatusStr)
            time.sleep(int(TIME))
            i += 1;
        print u'运行结束'









from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

