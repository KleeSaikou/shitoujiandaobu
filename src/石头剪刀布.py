# -* - coding: UTF-8 -* -
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
import mainw




class shitoujiandaobu(mainw.Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(shitoujiandaobu, self).__init__()

    def clickedButtons(self, strr):
        # print("strr")
        self.label_getText.setText(strr)
        # return strr

    def lineTextConcerned(self):
        strr = self.lineEdit.text()
        if strr == "石头":
            self.label_getText.setText("我出布！哈哈哈哈既然你出了石头，那就是我赢咯")
        elif strr == "剪刀":
            self.label_getText.setText("我出石头！哈哈哈哈既然你出了剪刀，那就是我赢咯")
        elif strr == "布":
            self.label_getText.setText("我出剪刀！哈哈哈哈既然你出了布，那就是我赢咯")
        else:
            self.label_getText.setText("年轻人不讲武德，不按套路出牌，耗子尾汁")


if __name__ == '__main__':
    shitou = "我出布！哈哈哈哈既然你出了石头，那就是我赢咯"
    jiandao = "我出石头！哈哈哈哈既然你出了剪刀，那就是我赢咯"
    bu = "我出剪刀！哈哈哈哈既然你出了布，那就是我赢咯"
    app = QApplication(sys.argv)
    ui = shitoujiandaobu()

    MainWindow = QMainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_shitou.clicked.connect(lambda: ui.clickedButtons(shitou))
    ui.pushButton_jiandao.clicked.connect(lambda: ui.clickedButtons(jiandao))
    ui.pushButton_bu.clicked.connect(lambda: ui.clickedButtons(bu))
    ui.pushButton_shuru_queren.clicked.connect(lambda: ui.lineTextConcerned())


    MainWindow.show()
    sys.exit(app.exec_())