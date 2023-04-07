import cv2
import qrcode

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('qrcodegui.ui', self)
        self.show()

        self.current_file = ""
        self.actionLoad.triggered.connect(self.load_image)
        self.actionSave.triggered.connect(self.save_image)
        self.pushButton.clicked.connect(self.generate_code)
        self.pushButton_2.clicked.connect(self.read_code)

    def load_image(self):
        pass

    def save_image(self):
        pass



def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()



if __name__ == "__main__":
    main()