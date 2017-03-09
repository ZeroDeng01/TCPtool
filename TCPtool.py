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
        Form.resize(581, 435)
        Form.setMinimumSize(QtCore.QSize(581, 435))
        Form.setMaximumSize(QtCore.QSize(581, 435))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(13, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 47, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 77, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 109, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.HOST = QtGui.QLineEdit(Form)
        self.HOST.setGeometry(QtCore.QRect(110, 20, 141, 21))
        self.HOST.setObjectName(_fromUtf8("HOST"))
        self.PORT = QtGui.QLineEdit(Form)
        self.PORT.setGeometry(QtCore.QRect(110, 50, 141, 21))
        self.PORT.setObjectName(_fromUtf8("PORT"))
        self.TIME = QtGui.QLineEdit(Form)
        self.TIME.setGeometry(QtCore.QRect(110, 80, 111, 21))
        self.TIME.setObjectName(_fromUtf8("TIME"))
        self.NUM = QtGui.QLineEdit(Form)
        self.NUM.setGeometry(QtCore.QRect(110, 110, 141, 21))
        self.NUM.setObjectName(_fromUtf8("NUM"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(229, 77, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Start = QtGui.QPushButton(Form)
        self.Start.setGeometry(QtCore.QRect(12, 150, 101, 23))
        self.Start.setObjectName(_fromUtf8("Start"))
        self.Exit = QtGui.QPushButton(Form)
        self.Exit.setGeometry(QtCore.QRect(150, 150, 101, 23))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(11, 189, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.TEXT = QtGui.QPlainTextEdit(Form)
        self.TEXT.setGeometry(QtCore.QRect(10, 220, 241, 181))
        self.TEXT.setObjectName(_fromUtf8("TEXT"))
        self.STATUS = QtGui.QPlainTextEdit(Form)
        self.STATUS.setGeometry(QtCore.QRect(280, 50, 291, 351))
        self.STATUS.setObjectName(_fromUtf8("STATUS"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(280, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(220, 410, 91, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Start.clicked.connect(self.tcp)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TCP发包工具", None))
        self.label.setText(_translate("Form", "IP", None))
        self.label_2.setText(_translate("Form", "端          口", None))
        self.label_3.setText(_translate("Form", "间隔时间", None))
        self.label_4.setText(_translate("Form", "发包次数", None))
        self.HOST.setText(_translate("Form", "127.0.0.1", None))
        self.PORT.setText(_translate("Form", "8080", None))
        self.TIME.setText(_translate("Form", "0", None))
        self.NUM.setText(_translate("Form", "1", None))
        self.label_5.setText(_translate("Form", "秒", None))
        self.Start.setText(_translate("Form", "开始发包", None))
        self.Exit.setText(_translate("Form", "退出", None))
        self.label_6.setText(_translate("Form", "发送数据", None))
        self.TEXT.setPlainText(_translate("Form", "Email:denglin0105@vip.qq.com", None))
        self.label_7.setText(_translate("Form", "接收数据", None))
        self.label_8.setText(_translate("Form", "作者：ZeroDeng", None))



    #运行tcp
    def TCP(self):
        HOST = str(self.HOST.text())  # ip
        PORT = int(self.PORT.text())  # 端口
        TEXT = str(self.TEXT.toPlainText())  # 发送内容
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



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

