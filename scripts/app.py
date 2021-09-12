import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtTest
import webbrowser


from .custom_qstacked_widgets import *
from .code_img import coding
from .decode_img import decoding

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PyQt5.QtWinExtras import QtWin
    myappid = 'ilyaskhiat.company'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #setup of the main widget
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setFixedSize(1000,600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(247, 251, 252);")
        self.centralwidget.setObjectName("centralwidget")
        #----------------------------------------------------------------------------#
        MainWindow.setWindowIcon(QtGui.QIcon(':/img/img/icon.png'))


        ### TOP FRAME:CONTAINS THE NAVBAR.

        #frame setup
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 80))
        self.frame.setStyleSheet("background:None;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #adding the name of the app
        self.stegano = QtWidgets.QLabel(self.frame)
        self.stegano.setGeometry(QtCore.QRect(50, 37, 111, 26))
        font = QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        font.setKerning(False)
        self.stegano.setFont(font)
        self.stegano.setStyleSheet("letter-spacing:4px; color: rgb(29, 61, 86);")
        self.stegano.setObjectName("stegano")
        # +icon
        self.icon = QtWidgets.QLabel(self.frame)
        self.icon.setGeometry(QtCore.QRect(151, 41, 24, 24))
        self.icon.setStyleSheet("background-image: url(:/img/img/tabler-icon-search (1).svg);")
        self.icon.setText("")
        self.icon.setObjectName("icon")

        #making and customizing the decode button
        self.decode = QtWidgets.QPushButton(self.frame)
        self.decode.setGeometry(QtCore.QRect(876, 41, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        self.decode.setFont(font)
        self.decode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decode.setStyleSheet("QPushButton{\nletter-spacing:3.2px;\nbackground:None;\nborder:None;\n color:#111747;}")
        self.decode.setObjectName("decode")

        #making and customizing the encode button
        self.encode = QtWidgets.QPushButton(self.frame)
        self.encode.setGeometry(QtCore.QRect(719, 40, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        self.encode.setFont(font)
        self.encode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.encode.setStyleSheet("QPushButton{\nletter-spacing:3.2px;\nbackground:None;\nborder:None;\n color:#111747;}")
        self.encode.setObjectName("encode")

        #making and customizing the home button
        self.home = QtWidgets.QPushButton(self.frame)
        self.home.setGeometry(QtCore.QRect(557, 40, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        self.home.setFont(font)
        self.home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home.setStyleSheet("QPushButton{\nletter-spacing:3.2px;\nbackground:None;\nborder:None;\n color:#06818E;}")
        self.home.setObjectName("home")
        #at this point ,the navbar is completed
        #------------------------------------------------------------------------------------#


        ### MAIN FRAME: CONTAINS THE PAGES, 
        # the stackedwidget is imported from the custom_qstacked_widget file ,because of aditionnal options needed to animate the translation between the pages

        #creating the stack
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 80, 1000, 520))
        self.stackedWidget.setObjectName("stackedWidget")

        #Home page setup 
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")

        #ui component
        self.pattern = QtWidgets.QLabel(self.home_page)
        self.pattern.setGeometry(QtCore.QRect(280, 0, 720, 520))
        self.pattern.setStyleSheet("background-image: url(:/img/img/pattern1.svg);")
        self.pattern.setText("")
        self.pattern.setObjectName("pattern")

        #slogan
        self.T1 = QtWidgets.QLabel(self.home_page)
        self.T1.setGeometry(QtCore.QRect(50, 58, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.T1.setFont(font)
        self.T1.setStyleSheet("line-height:1.2px;\n"
                              "color:#06818E;\n"
                              "letter-spacing:6.4px;")
        self.T1.setObjectName("T1")
        self.T2 = QtWidgets.QLabel(self.home_page)
        self.T2.setGeometry(QtCore.QRect(50, 112, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.T2.setFont(font)
        self.T2.setStyleSheet("line-height:1.2px;\n"
                              "color:#06818E;\n"
                              "letter-spacing:6.4px;\n"
                              "background:None;")
        self.T2.setObjectName("T2")
        self.T3 = QtWidgets.QLabel(self.home_page)
        self.T3.setGeometry(QtCore.QRect(50, 164, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.T3.setFont(font)
        self.T3.setStyleSheet("line-height:1.2px;\n"
                              "color:#06818E;\n"
                              "letter-spacing:6.4px;\n"
                              "background:None;")
        self.T3.setObjectName("T3")

        #paragraph
        self.b1 = QtWidgets.QLabel(self.home_page)
        self.b1.setGeometry(QtCore.QRect(50, 244, 312, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b1.setFont(font)
        self.b1.setStyleSheet("letter-spacing:2.4px;\n"
                              "color:#111747;")
        self.b1.setMidLineWidth(0)
        self.b1.setScaledContents(False)
        self.b1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.b1.setWordWrap(True)
        self.b1.setOpenExternalLinks(False)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QLabel(self.home_page)
        self.b2.setGeometry(QtCore.QRect(50, 273, 312, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b2.setFont(font)
        self.b2.setStyleSheet("letter-spacing:2.4px;\n"
                              "color:#111747;")
        self.b2.setMidLineWidth(0)
        self.b2.setScaledContents(False)
        self.b2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.b2.setWordWrap(True)
        self.b2.setOpenExternalLinks(False)
        self.b2.setObjectName("b2")
        self.b4 = QtWidgets.QLabel(self.home_page)
        self.b4.setGeometry(QtCore.QRect(50, 331, 312, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b4.setFont(font)
        self.b4.setStyleSheet("letter-spacing:2.4px;\n"
                              "color:#111747;")
        self.b4.setMidLineWidth(0)
        self.b4.setScaledContents(False)
        self.b4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.b4.setWordWrap(True)
        self.b4.setOpenExternalLinks(False)
        self.b4.setObjectName("b4")
        self.b3 = QtWidgets.QFrame(self.home_page)
        self.b3.setGeometry(QtCore.QRect(50, 302, 312, 21))
        self.b3.setStyleSheet("background:None;")
        self.b3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.b3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.b3.setObjectName("b3")
        self.b31 = QtWidgets.QLabel(self.b3)
        self.b31.setGeometry(QtCore.QRect(0, 0, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b31.setFont(font)
        self.b31.setStyleSheet("letter-spacing:2.4px;\n"
                               "color:#16A3B2;")
        self.b31.setMidLineWidth(0)
        self.b31.setScaledContents(False)
        self.b31.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.b31.setWordWrap(True)
        self.b31.setOpenExternalLinks(False)
        self.b31.setObjectName("b31")
        self.b32 = QtWidgets.QLabel(self.b3)
        self.b32.setGeometry(QtCore.QRect(150, 0, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b32.setFont(font)
        self.b32.setStyleSheet("letter-spacing:2.4px;\n"
                               "color:#111747;")
        self.b32.setMidLineWidth(0)
        self.b32.setScaledContents(False)
        self.b32.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.b32.setWordWrap(True)
        self.b32.setOpenExternalLinks(False)
        self.b32.setObjectName("b32")
        self.b6 = QtWidgets.QFrame(self.home_page)
        self.b6.setGeometry(QtCore.QRect(50, 360, 312, 21))
        self.b6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.b6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.b6.setObjectName("b6")
        self.b61 = QtWidgets.QLabel(self.b6)
        self.b61.setGeometry(QtCore.QRect(0, 0, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b61.setFont(font)
        self.b61.setStyleSheet("letter-spacing:2.4px;\n"
                               "color:#111747;")
        self.b61.setMidLineWidth(0)
        self.b61.setScaledContents(False)
        self.b61.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.b61.setWordWrap(True)
        self.b61.setOpenExternalLinks(False)
        self.b61.setObjectName("b61")
        self.b62 = QtWidgets.QLabel(self.b6)
        self.b62.setGeometry(QtCore.QRect(130, 0, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b62.setFont(font)
        self.b62.setStyleSheet("letter-spacing:2.4px;\n"
                               "color:#16A3B2;")
        self.b62.setMidLineWidth(0)
        self.b62.setScaledContents(False)
        self.b62.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.b62.setWordWrap(True)
        self.b62.setOpenExternalLinks(False)
        self.b62.setObjectName("b62")
        self.b63 = QtWidgets.QLabel(self.b6)
        self.b63.setGeometry(QtCore.QRect(260, 0, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.b63.setFont(font)
        self.b63.setStyleSheet("letter-spacing:2.4px;\n"
                               "color:#111747;")
        self.b63.setMidLineWidth(0)
        self.b63.setScaledContents(False)
        self.b63.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.b63.setWordWrap(True)
        self.b63.setOpenExternalLinks(False)
        self.b63.setObjectName("b63")

        #adding info button
        self.clear = QtWidgets.QPushButton(self.home_page)
        self.clear.setGeometry(QtCore.QRect(50, 450, 32, 32))
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear.setObjectName("clear")
        self.clear.setStyleSheet('''QPushButton {
            border: 0px;
            background: url(:/img/img/info2.svg);}
            QPushButton:hover {
            border: 0px;
            background: url(:/img/img/info.svg);}''')

        #adding copyright notice
        self.cr = QtWidgets.QLabel(self.home_page)
        self.cr.setGeometry(QtCore.QRect(50, 490, 312, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(8)
        font.setBold(False)
        #font.setWeight(50)
        self.cr.setFont(font)
        self.cr.setStyleSheet("letter-spacing:2.4px;\n"
                              "color:rgba(17,23,71,0.5);")
        self.cr.setMidLineWidth(0)
        self.cr.setScaledContents(False)
        self.cr.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.cr.setWordWrap(True)
        self.cr.setOpenExternalLinks(False)
        self.cr.setObjectName("cr")

        #adding the home page to the stack
        self.stackedWidget.addWidget(self.home_page)

        #------#
        ##############################################################################
        ##############################################################################
        #------#

        #encode page setup
        self.encode_page = QtWidgets.QWidget()
        self.encode_page.setStyleSheet("background-image: url(:/img/img/pattern2.svg);")
        self.encode_page.setObjectName("encode_page")

        #input box :contains the msg to hide
        self.msg_input = QtWidgets.QTextEdit(self.encode_page)
        self.msg_input.setGeometry(QtCore.QRect(146, 54, 369, 370))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.msg_input.setFont(font)
        self.msg_input.setStyleSheet("background:rgba(255,255,255,0.7);\n"
                                     "border: 5px solid rgba(246,174,156,1);\n"
                                     "border-radius:15px;\n"
                                     "color:#111747;\n"
                                     "letter-spacing:1.5px;\n"
                                     "padding:5px;")
        self.msg_input.setMarkdown("")
        self.msg_input.setObjectName("msg_input")

        #pop up text: alerts the user about the back_end operations
        self.console = QtWidgets.QLabel(self.encode_page)
        self.console.setGeometry(QtCore.QRect(575, 400, 350, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.console.setFont(font)
        self.console.setStyleSheet("color:rgba(17,23,71,0.5);\n"
                                      "letter-spacing:0.7px;")
        self.console.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.console.setObjectName("console")

        #ui component
        self.choose_img = QtWidgets.QLabel(self.encode_page)
        self.choose_img.setGeometry(QtCore.QRect(575, 66, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.choose_img.setFont(font)
        self.choose_img.setStyleSheet("color:#111747;\n"
                                      "letter-spacing:0.7px;")
        self.choose_img.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.choose_img.setObjectName("choose_img")

        #ui component
        self.choose_folder = QtWidgets.QLabel(self.encode_page)
        self.choose_folder.setGeometry(QtCore.QRect(575, 166, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.choose_folder.setFont(font)
        self.choose_folder.setStyleSheet("color:#111747;\n"
                                         "letter-spacing:0.7px;")
        self.choose_folder.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.choose_folder.setObjectName("choose_folder")


        self.img_icon = QtWidgets.QLabel(self.encode_page)
        self.img_icon.setGeometry(QtCore.QRect(575, 96, 24, 24))
        self.img_icon.setStyleSheet("background-image: url(:/img/img/image.svg);")
        self.img_icon.setText("")
        self.img_icon.setObjectName("img_icon")


        self.folder_icon = QtWidgets.QLabel(self.encode_page)
        self.folder_icon.setGeometry(QtCore.QRect(575, 196, 24, 24))
        self.folder_icon.setStyleSheet("background-image: url(:/img/img/folder.svg);")
        self.folder_icon.setText("")
        self.folder_icon.setObjectName("folder_icon")

        #browse button
        self.browse1 = QtWidgets.QPushButton(self.encode_page)
        self.browse1.setGeometry(QtCore.QRect(851, 91, 99, 29))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.browse1.setFont(font)
        self.browse1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse1.setStyleSheet("QPushButton{\n"
                                   "color:#16A3B2;\n"
                                   "border:1px solid #16A3B2;\n"
                                   "border-radius:14.4px;\n"
                                   "letter-spacing:1.2px;\n"
                                   "background:None;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "color:#F7FBFC;\n"
                                   "background:#16A3B2;\n"
                                   "border:None;\n"
                                   "}\n"
                                   "")
        self.browse1.setObjectName("browse1")

        #button used to change the the path of the output
        self.change = QtWidgets.QPushButton(self.encode_page)
        self.change.setGeometry(QtCore.QRect(851, 191, 99, 29))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.change.setFont(font)
        self.change.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change.setStyleSheet("QPushButton{\n"
                                  "color:#16A3B2;\n"
                                  "border:1px solid #16A3B2;\n"
                                  "border-radius:14.4px;\n"
                                  "letter-spacing:1.2px;\n"
                                  "background:None;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "color:#F7FBFC;\n"
                                  "background:#16A3B2;\n"
                                  "border:None;\n"
                                  "}\n"
                                  "")
        self.change.setObjectName("change")

        #execution button
        self.hide = QtWidgets.QPushButton(self.encode_page)
        self.hide.setGeometry(QtCore.QRect(580, 320, 234, 45))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.hide.setFont(font)
        self.hide.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hide.setStyleSheet("QPushButton{\n"
                                "color:#f7fbfc;\n"
                                "background:#F6AE9F;\n"
                                "border-radius:22px;\n"
                                "letter-spacing:1.6px;\n"
                                "\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "border:None;\n"
                                "color:#F6AE9F;\n"
                                "border:2px solid #F6AE9F;\n"
                                "background:rgba(246,174,156,0.1);\n"
                                "}\n"
                                "QPushButton:pressed{\n"
                                "color:#f7fbfc;\n"
                                "background:#F6AE9F;\n"
                                "\n"
                                "}\n"
                                "")
        self.hide.setObjectName("hide")

        #editable line: shows the input path
        self.browse_line = QtWidgets.QLineEdit(self.encode_page)
        self.browse_line.setGeometry(QtCore.QRect(605, 98, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.browse_line.setFont(font)
        self.browse_line.setStyleSheet("background:#f7fbfc;\n"
                                       "border: None;\n"
                                       "color:rgba(17,23,71,0.5);\n"
                                       "letter-spacing:1.5px;")
        self.browse_line.setObjectName("browse_line")

        #editable line :shows the output path
        self.folder_line = QtWidgets.QLineEdit(self.encode_page)
        self.folder_line.setGeometry(QtCore.QRect(605, 198, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.folder_line.setFont(font)
        self.folder_line.setStyleSheet("background:#f7fbfc;\n"
                                       "border: None;\n"
                                       "color:rgba(17,23,71,0.5);\n"
                                       "letter-spacing:1.5px;")
        self.folder_line.setObjectName("folder_line")
        #adding the encode page to the stack
        self.stackedWidget.addWidget(self.encode_page)
        #------------------------------------------------------------------------------#

        #decode page
        self.decode_page = QtWidgets.QWidget()
        self.decode_page.setStyleSheet("background-image: url(:/img/img/pattern3.svg);")
        self.decode_page.setObjectName("decode_page")

        #text box: shows the hidden message
        self.msg_output = QtWidgets.QTextEdit(self.decode_page)
        self.msg_output.setGeometry(QtCore.QRect(574, 54, 369, 370))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.msg_output.setFont(font)
        self.msg_output.setStyleSheet("background:rgba(255,255,255,0.7);\n"
                                      "border: 5px solid rgba(246,174,156,1);\n"
                                      "border-radius:15px;\n"
                                      "color:#111747;\n"
                                      "letter-spacing:1px;\n"
                                      "padding:5px;")
        self.msg_output.setMarkdown("")
        self.msg_output.setObjectName("msg_output")

        #browse button
        self.browse2 = QtWidgets.QPushButton(self.decode_page)
        self.browse2.setGeometry(QtCore.QRect(427, 94, 99, 29))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.browse2.setFont(font)
        self.browse2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse2.setStyleSheet("QPushButton{\n"
                                   "color:#16A3B2;\n"
                                   "border:1px solid #16A3B2;\n"
                                   "border-radius:14.4px;\n"
                                   "letter-spacing:1.2px;\n"
                                   "background:None;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "color:#F7FBFC;\n"
                                   "background:#16A3B2;\n"
                                   "border:None;\n"
                                   "}\n"
                                   "")
        self.browse2.setObjectName("browse2")

        #ui component
        self.choose_img2 = QtWidgets.QLabel(self.decode_page)
        self.choose_img2.setGeometry(QtCore.QRect(151, 54, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.choose_img2.setFont(font)
        self.choose_img2.setStyleSheet("color:#111747;\n"
                                       "letter-spacing:0.7px;")
        self.choose_img2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.choose_img2.setObjectName("choose_img2")

        #ui component
        self.img_icon2 = QtWidgets.QLabel(self.decode_page)
        self.img_icon2.setGeometry(QtCore.QRect(151, 99, 24, 24))
        self.img_icon2.setStyleSheet("background-image: url(:/img/img/image.svg);")
        self.img_icon2.setText("")
        self.img_icon2.setObjectName("img_icon2")

        #editable line showing the path of the image to decode
        self.browse_line2 = QtWidgets.QLineEdit(self.decode_page)
        self.browse_line2.setGeometry(QtCore.QRect(180, 100, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.browse_line2.setFont(font)
        self.browse_line2.setStyleSheet("background:#f7fbfc;\n"
                                        "border: None;\n"
                                        "color:rgba(17,23,71,0.5);\n"
                                        "letter-spacing:1.5px;")
        self.browse_line2.setObjectName("browse_line2")
        #ading the decode page to the stack
        self.stackedWidget.addWidget(self.decode_page)
        #---------------------------------------------------------------------#

        MainWindow.setCentralWidget(self.centralwidget)

        #connecting the navbar buttons to the specific pages
        for w in self.frame.findChildren(QtWidgets.QPushButton):
            w.clicked.connect(self.apply_but_style)
        self.encode.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.encode_page))
        self.home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home_page))
        self.decode.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.decode_page))

        #connecting the buttons to their functions
        self.browse1.clicked.connect(self.input_file)
        self.change.clicked.connect(self.output_folder)
        self.hide.clicked.connect(self.code_img)
        self.browse2.clicked.connect(self.decode_image)
        self.clear.clicked.connect(self.open_webbrowser)

        #animating the pages
        self.stackedWidget.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stackedWidget.setTransitionSpeed(500)
        self.stackedWidget.setTransitionEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.stackedWidget.setSlideTransition(True)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def apply_but_style(self):#this functions is used to customize the navbar buttons and switching between the states
        for w in self.frame.findChildren(QtWidgets.QPushButton):
            if w.objectName() != self.frame.sender().objectName():
                ff = w.styleSheet()[:-15] + 'color:#111747;}'
                w.setStyleSheet(ff)
        d = self.frame.sender().styleSheet()[:-15] + 'color:#06818E;}'
        self.frame.sender().setStyleSheet(d)
        return
    
    def code_img(self):#this function communicate with the code_img file
        img=self.browse_line.text()
        folder=self.folder_line.text()
        msg=self.msg_input.toPlainText()
        f = coding(msg,img,folder)
        self.console.setText(f)
        QtTest.QTest.qWait(3000)
        self.console.setText('')

    def input_file(self):#get to path of the input image
        i_name = QtWidgets.QFileDialog.getOpenFileName(directory=os.environ['USERPROFILE'],filter="Images (*.jpe *.png *.jpg *.jpeg *.webp)")
        self.browse_line.setText(i_name[0])

    def output_folder(self):#set the path of the output folder
        f_name = QtWidgets.QFileDialog.getExistingDirectory(directory=os.environ['USERPROFILE'])
        self.folder_line.setText(f_name)
    
    def decode_image(self):#communicate with the decode_img file
        self.msg_output.setText('Wait . . .')
        i_name = QtWidgets.QFileDialog.getOpenFileName(directory=os.environ['USERPROFILE'],filter="Images (*.png *.jpg)")
        self.browse_line2.setText(i_name[0])
        msg=decoding(i_name[0])
        try:
            self.msg_output.setText(msg)
        except:
            self.msg_output.setText("I can't read this")
        return 'Hmm interesting!!!'

    def open_webbrowser(self):
        webbrowser.open('http://www.google.com')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stegano"))
        self.stegano.setText(_translate("MainWindow", "STEGAN"))
        self.decode.setText(_translate("MainWindow", "Decode"))
        self.encode.setText(_translate("MainWindow", "Encode"))
        self.home.setText(_translate("MainWindow", "Home"))
        self.T1.setText(_translate("MainWindow", "BRING YOUR"))
        self.T2.setText(_translate("MainWindow", "MESSAGES"))
        self.T3.setText(_translate("MainWindow", "TO THE NEXT LEVEL"))
        self.b1.setText(_translate("MainWindow", "Hide your message inside an"))
        self.b2.setText(_translate("MainWindow", "image by using the power of"))
        self.cr.setText(_translate("MainWindow", "Copyright (c) 2021 Ilyas Khiat"))
        self.b4.setText(_translate("MainWindow", "crush, your best friend … or"))
        self.b31.setText(_translate("MainWindow", "steganography"))
        self.b32.setText(_translate("MainWindow", ". Send it to your"))
        self.b61.setText(_translate("MainWindow", "maybe, your"))
        self.b62.setText(_translate("MainWindow", "secret agent"))
        self.b63.setText(_translate("MainWindow", "!!!"))
        self.msg_input.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal; letter-spacing:1.5px;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.msg_input.setPlaceholderText(_translate("MainWindow", "Write something here ;)"))
        self.choose_img.setText(_translate("MainWindow", "Choose an image ."))
        self.console.setText(_translate("MainWindow", ""))
        self.choose_folder.setText(_translate("MainWindow", "Change the output folder ."))
        self.browse1.setText(_translate("MainWindow", "Browse"))
        self.change.setText(_translate("MainWindow", "Change"))
        self.hide.setText(_translate("MainWindow", "Hide the message"))
        self.msg_output.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal; letter-spacing:1px;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.msg_output.setPlaceholderText(_translate("MainWindow", "You can see the hidden code here."))
        self.browse2.setText(_translate("MainWindow", "Browse"))
        self.choose_img2.setText(_translate("MainWindow", "Choose the image you want to decode . "))
        self.folder_line.setText(_translate("MainWindow", os.environ['USERPROFILE']))


import files.resc

def start():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    QtGui.QFontDatabase.addApplicationFont("Roboto-bold.ttf")
    QtGui.QFontDatabase.addApplicationFont("OpenSans-SemiBold.ttf")
    QtGui.QFontDatabase.addApplicationFont("OpenSans-Regular.ttf")
    #print(QtGui.QFontDatabase().families())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        

