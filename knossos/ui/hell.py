# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/hell.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from ..qt import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 756)
        MainWindow.setMinimumSize(QtCore.QSize(1126, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget, #centralwidget > QWidget > QLabel {\n"
"  background: #1c1c1c;\n"
"  color: #fff;\n"
"}\n"
"\n"
"QProgressBar {\n"
"  color: #fff;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBarArea = QtWidgets.QWidget(self.centralwidget)
        self.titleBarArea.setObjectName("titleBarArea")
        self.titleBarAreaLayout = QtWidgets.QHBoxLayout(self.titleBarArea)
        self.titleBarAreaLayout.setObjectName("titleBarAreaLayout")
        self.cornerIcon = QtWidgets.QLabel(self.titleBarArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cornerIcon.sizePolicy().hasHeightForWidth())
        self.cornerIcon.setSizePolicy(sizePolicy)
        self.cornerIcon.setText("")
        self.cornerIcon.setPixmap(QtGui.QPixmap(":/knossos/data/hlp_corner.png"))
        self.cornerIcon.setScaledContents(False)
        self.cornerIcon.setObjectName("cornerIcon")
        self.titleBarAreaLayout.addWidget(self.cornerIcon)
        self.titleBar = QtWidgets.QLabel(self.titleBarArea)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setLegacyWeight(50)
        self.titleBar.setFont(font)
        self.titleBar.setObjectName("titleBar")
        self.titleBarAreaLayout.addWidget(self.titleBar)
        self.minimizeButton = QtWidgets.QPushButton(self.titleBarArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizeButton.sizePolicy().hasHeightForWidth())
        self.minimizeButton.setSizePolicy(sizePolicy)
        self.minimizeButton.setMinimumSize(QtCore.QSize(20, 20))
        self.minimizeButton.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    background: no-repeat url(:/html/images/window_icons/min.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: no-repeat url(:/html/images/window_icons/min-h.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: no-repeat url(:/html/images/window_icons/min-a.png);\n"
"}")
        self.minimizeButton.setText("")
        self.minimizeButton.setObjectName("minimizeButton")
        self.titleBarAreaLayout.addWidget(self.minimizeButton)
        self.maximizeButton = QtWidgets.QPushButton(self.titleBarArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maximizeButton.sizePolicy().hasHeightForWidth())
        self.maximizeButton.setSizePolicy(sizePolicy)
        self.maximizeButton.setMinimumSize(QtCore.QSize(20, 20))
        self.maximizeButton.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    background: no-repeat url(:/html/images/window_icons/max.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: no-repeat url(:/html/images/window_icons/max-h.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: no-repeat url(:/html/images/window_icons/max-a.png);\n"
"}")
        self.maximizeButton.setText("")
        self.maximizeButton.setObjectName("maximizeButton")
        self.titleBarAreaLayout.addWidget(self.maximizeButton)
        self.restoreButton = QtWidgets.QPushButton(self.titleBarArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restoreButton.sizePolicy().hasHeightForWidth())
        self.restoreButton.setSizePolicy(sizePolicy)
        self.restoreButton.setMinimumSize(QtCore.QSize(20, 20))
        self.restoreButton.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    background: no-repeat url(:/html/images/window_icons/res.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: no-repeat url(:/html/images/window_icons/res-h.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: no-repeat url(:/html/images/window_icons/res-a.png);\n"
"}")
        self.restoreButton.setText("")
        self.restoreButton.setObjectName("restoreButton")
        self.titleBarAreaLayout.addWidget(self.restoreButton)
        self.closeButton = QtWidgets.QPushButton(self.titleBarArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(20, 20))
        self.closeButton.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    background: no-repeat url(:/html/images/window_icons/close.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: no-repeat url(:/html/images/window_icons/close-h.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: no-repeat url(:/html/images/window_icons/close-a.png);\n"
"}")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.titleBarAreaLayout.addWidget(self.closeButton)
        self.verticalLayout.addWidget(self.titleBarArea)
        self.webSpacing = QtWidgets.QHBoxLayout()
        self.webSpacing.setContentsMargins(6, 6, 6, 6)
        self.webSpacing.setObjectName("webSpacing")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setStyleSheet("QWebEngineView {\n"
"  padding: 5;\n"
"}")
        self.webView.setProperty("url", QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.webSpacing.addWidget(self.webView)
        self.verticalLayout.addLayout(self.webSpacing)
        self.progressInfo = QtWidgets.QWidget(self.centralwidget)
        self.progressInfo.setObjectName("progressInfo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.progressInfo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressLabel = QtWidgets.QLabel(self.progressInfo)
        self.progressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressLabel.setObjectName("progressLabel")
        self.verticalLayout_2.addWidget(self.progressLabel)
        self.progressBar = QtWidgets.QProgressBar(self.progressInfo)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.progressInfo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Knossos"))
        self.titleBar.setText(_translate("MainWindow", "Knossos"))
        self.progressLabel.setText(_translate("MainWindow", "TextLabel"))
from ..qt import QtWebEngineWidgets
