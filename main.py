import os
from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QShortcut, QKeySequence
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('window.ui', self)
        self.setFixedSize(779, 210)
        self.setWindowTitle("LinkMaker")
        
        self.template="""[Desktop Entry]
Name={}
Exec={}
Icon={}
Type=Application
Categories={};
Comment={}
StartupNotify={}"""

        shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        shortcut.activated.connect(self.quitApp)

        self.save.clicked.connect(self.savelink)
        self.remove.clicked.connect(self.removelink)
    
    def removelink(self):
        try:
            os.remove(f"{self.name.text()}.desktop")
        except:pass

    def savelink(self):
        link=self.template.format(self.name.text(),
                                  self.exec.text(),
                                  self.icon.text(),
                                  self.categories.text(),
                                  self.comment.text(),
                                  self.notify.isChecked()
                                  )
        with open(f"{self.name.text()}.desktop","w") as f:
            f.write(link)
        os.system(f"chmod -x {self.name.text()}.desktop")

    def quitApp(self):
        QApplication.instance().quit()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    os.chdir(f"{os.path.expanduser('~')}/.local/share/applications/")
    app.exec()