import os
from PyQt6 import QtWidgets, uic, QtGui, QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QShortcut, QKeySequence
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 244)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(779, 244))
        MainWindow.setMaximumSize(QtCore.QSize(779, 244))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 761, 221))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_6)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.exec = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_6)
        self.exec.setObjectName("exec")
        self.horizontalLayout_2.addWidget(self.exec)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.icon = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_6)
        self.icon.setObjectName("icon")
        self.horizontalLayout_3.addWidget(self.icon)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.categories = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_6)
        self.categories.setObjectName("categories")
        self.horizontalLayout_4.addWidget(self.categories)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comment = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_6)
        self.comment.setObjectName("comment")
        self.horizontalLayout_5.addWidget(self.comment)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.notify = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget_6)
        self.notify.setChecked(True)
        self.notify.setTristate(False)
        self.notify.setObjectName("notify")
        self.verticalLayout.addWidget(self.notify)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.save = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.verticalLayout_2.addWidget(self.save)
        self.remove = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove.sizePolicy().hasHeightForWidth())
        self.remove.setSizePolicy(sizePolicy)
        self.remove.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.remove.setFont(font)
        self.remove.setObjectName("remove")
        self.verticalLayout_2.addWidget(self.remove)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "name"))
        self.label_2.setText(_translate("MainWindow", "command"))
        self.label_3.setText(_translate("MainWindow", "icon"))
        self.label_4.setText(_translate("MainWindow", "categories"))
        self.label_5.setText(_translate("MainWindow", "comment"))
        self.notify.setText(_translate("MainWindow", "StartupNotify"))
        self.save.setText(_translate("MainWindow", "save"))
        self.remove.setText(_translate("MainWindow", "remove"))

class Ui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
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