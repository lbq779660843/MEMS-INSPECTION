'''
Author:         BQ Long
Data:           2019/11/11
IDE/env:        Anaconda/base(python 3.6.5)
'''
import socket
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2
import sys
import logging
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QApplication
from Logining import Ui_Dialog
from MSG_BOX import Ui_MSG
from decimal import Decimal

###预定义的参数###
panel_path = ''             #panel文件夹路径
color_para = []             #颜色参数list
STATUS = ''                 #Local/Shared
BISDATA = ''                #BISDATA文件夹路径
BISLOG = ''                 #BISLOG文件夹路径
BISMODEL = ''               #BISMODEL文件夹路径
File_Format = ''            #文件的格式，对应着三个那三个文件夹

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.form = MainWindow#实例化MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 150)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.HongKong))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.Panel_SN = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Panel_SN.sizePolicy().hasHeightForWidth())
        self.Panel_SN.setSizePolicy(sizePolicy)
        self.Panel_SN.setMinimumSize(QtCore.QSize(10, 0))
        self.Panel_SN.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Panel_SN.setFont(font)
        self.Panel_SN.setStyleSheet("background-color: rgb(170, 255, 0);\n"
                                   "font: 8pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(157, 157, 157);")
        self.Panel_SN.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.HongKong))
        self.Panel_SN.setCheckable(False)
        self.Panel_SN.setChecked(False)
        self.Panel_SN.setDefault(False)
        self.Panel_SN.setFlat(False)
        self.Panel_SN.setObjectName("Panel SN")
        self.horizontalLayout.addWidget(self.Panel_SN)

        self.INPUTING = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy\
            (QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INPUTING.sizePolicy().hasHeightForWidth())
        self.INPUTING.setSizePolicy(sizePolicy)
        self.INPUTING.setMinimumSize(QtCore.QSize(10, 0))
        self.INPUTING.setMaximumSize(QtCore.QSize(100, 16777215))
        self.INPUTING.setObjectName("INPUTING")
        self.horizontalLayout.addWidget(self.INPUTING)
        spacerItem = QtWidgets.QSpacerItem\
            (10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.LOADING = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy\
            (QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LOADING.sizePolicy().hasHeightForWidth())
        self.LOADING.setSizePolicy(sizePolicy)
        self.LOADING.setMinimumSize(QtCore.QSize(10, 0))
        self.LOADING.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LOADING.setFont(font)
        self.LOADING.setStyleSheet("background-color: rgb(170, 255, 0);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(157, 157, 157);")
        self.LOADING.setLocale\
            (QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.HongKong))
        self.LOADING.setCheckable(False)
        self.LOADING.setChecked(False)
        self.LOADING.setDefault(False)
        self.LOADING.setFlat(False)
        self.LOADING.setObjectName("LOADING")
        self.horizontalLayout.addWidget(self.LOADING)

        spacerItem1 = QtWidgets.QSpacerItem\
            (10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Settings = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy\
            (QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.Settings.setMinimumSize(QtCore.QSize(10, 0))
        self.Settings.setMaximumSize(QtCore.QSize(50, 16777215))
        self.Settings.setObjectName("Settings")
        self.horizontalLayout.addWidget(self.Settings)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.IMGLABEL = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy\
            (QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IMGLABEL.sizePolicy().hasHeightForWidth())
        self.IMGLABEL.setSizePolicy(sizePolicy)
        self.IMGLABEL.setObjectName("IMGLABEL")
        self.verticalLayout.addWidget(self.IMGLABEL)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.LOADING.clicked.connect(self.LOADING_click)                    ###SETTING和LOADING_click是不属于MainWindow的
        self.Settings.clicked.connect(self.SETTING)                         ###因此将Mainwindow改为self
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.LOADING.setShortcut(QtCore.Qt.Key_Return)                      ###将该文本框关联回车

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon('cat.ico'))                    ###设置该界面左上图标
        MainWindow.setWindowTitle\
            (_translate("MainWindow", "MEMS BISVIEW FINAL INSPECTION"))
        self.INPUTING.setPlaceholderText(_translate("MainWindow", "Input the id"))
        self.LOADING.setText(_translate("MainWindow", "Loading"))
        self.Settings.setText(_translate("MainWindow", "Settings"))
        self.IMGLABEL.setText(_translate("MainWindow", "TextLabel"))
        self.Panel_SN.setText(_translate("MainWindow", "Panel SN:"))        ###无效按钮，为了布局

    def LOADING_click(self):                                                ###Loading按钮对应的槽函数
        global panel_id
        panel_id = self.INPUTING.text()                                     ###获取文本框的输入信息
        blankspace = '                      '                               ###统一需要记录的消息为blankspace的长度
        msg_line = panel_id + blankspace[len(panel_id):]                    ###panel_id过长的异常没有处理
        try:
            if len(panel_id) == 10:                                         ###工人输入时导数第三位可能没有.
                list_1 = [BISDATA, '/', panel_id[:8], '.', panel_id[-2:]]
                panel_name = ''.join(list_1)
            else:
                list_1 = [BISDATA, '/', panel_id]
                panel_name = ''.join(list_1)
            try:
                src = open(panel_name, 'r')                                 ###读取file
                data = []
                x = []
                y = []
                color_label = []
                try:
                    for line in src:
                        data.append(line)
                    src.close()
                    row = int(data[1][:2])                                  ###所有文件第二行就给出了对应图的尺寸
                    clo = int(data[1][-3:])
                    total = row * clo                                       ###文件有效信息行的行数
                    if File_Format == 'Origin':                             ###按照demo中最后一列的信息(File_Format)读取
                        for i in range(4, total*5 +4, 5):
                            comma_offset = []
                            for j in range(len(data[i])):
                                if data[i][j] is ',':                       ###用逗号切
                                    comma_offset.append(j)
                            comma_1 = comma_offset[0]
                            comma_2 = comma_offset[1]
                            firt_info = data[i][0:comma_1]
                            second_info = data[i][comma_1 + 1:comma_2]
                            third_info = data[i][comma_2 + 1:]
                            x.append(firt_info)                             ###x坐标,y坐标以及颜色标签
                            y.append(second_info)
                            color_label.append(third_info)
                    elif File_Format == 'Input':                            ###根据每种文件的数据格式进行遍历
                        for i in range(4, total + 4):
                            comma_offset = []
                            for j in range(len(data[i])):
                                if data[i][j] is ',':
                                    comma_offset.append(j)
                            comma_1 = comma_offset[0]
                            comma_2 = comma_offset[1]
                            firt_info = data[i][0:comma_1]
                            second_info = data[i][comma_1 + 1:comma_2]
                            third_info = data[i][comma_2 + 1:]
                            x.append(firt_info)
                            y.append(second_info)
                            color_label.append(third_info)
                    else:                                                    ###'TEST_RESULT'文件第三个逗号后面还有数据，所以不能按第二种切法切
                        for i in range(4, total + 4):
                            comma_offset = []
                            for j in range(len(data[i])):
                                if data[i][j] is ',':
                                    comma_offset.append(j)
                            comma_1 = comma_offset[0]
                            comma_2 = comma_offset[1]
                            comma_3 = comma_offset[2]
                            firt_info = data[i][0:comma_1]
                            second_info = data[i][comma_1 + 1:comma_2]
                            third_info  = data[i][comma_2 + 1:comma_3]
                            x.append(firt_info)
                            y.append(second_info)
                            color_label.append(third_info)

                    serial_name = panel_id[:2]                              ###前两位是文件序列号,代表某类产品
                    list_2 = ['./bg/', serial_name, '.bmp']                 ###读取相应的背景图
                    bg_name = ''.join(list_2)
                    img = cv2.imread(bg_name)
                    for j in range(total):
                        ic = int(color_label[j])
                        x_offset = int(x[j])
                        y_offset = int(y[j])
                        co =[]
                        for m in range(len(color_para[ic])):
                            if color_para[ic][m] is ',':                    ###根据颜色标签,遍历该标签下RGB三通道对应的数值
                                co.append(m)
                        co_1 = co[0]
                        co_2 = co[1]
                        blue = int(color_para[ic][1:co_1])
                        green = int(color_para[ic][co_1 + 1:co_2])
                        red = int(color_para[ic][co_2 + 1:-1])
                        img[y_offset * 2+4:(y_offset + 1) * 2+4, x_offset * 2+4:(x_offset + 1) * 2+4] = (red, green, blue)###赋值
                    img[(clo-1)*2 + 4:clo*2 + 4, (row-1)*2+4:row*2+4] = (20, 100, 255)###我的背景图实际上放大了2*2倍所有都*2；最有一个统一为该颜色
                    height, width = img.shape[:2]
                    bytesPerLine = 3 * width                                        ###这行和下行几乎是固定的写法，不知道为什么
                    qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    pix = QPixmap(qImg)
                    self.IMGLABEL.setPixmap(pix)                                    ###在IMGLABEL中显示图像
                    self.IMGLABEL.setScaledContents(True)                           ###让IMGLABEL自适应周围控件大小
                    log_write(BISLOG, panel_id, ' successfully!')
                except:
                    log_write(BISLOG, msg_line, ' File Not Found -> MessageToUser: [ '+ msg_line +' MAP File is in a wrong format!]')
                    self.form.hide()                                                ###弹出警告前隐藏当前界面
                    new_form = QtWidgets.QDialog()
                    self.msg = Ui_MSG()                                             ###实例化消息界面
                    self.msg.setupUi(new_form)
                    new_form.show()
                    self.msg.message_box.setText(msg_line, ' File Not Found -> MessageToUser: [ '+ msg_line +' MAP File is in a wrong format!]')
                    new_form.exec_()                                                ###退出消息界面
                    self.form.show()
            except :
                log_write(BISLOG, msg_line, ' File Not Found -> MessageToUser: [ Please check '+ msg_line + ' whether exits!]')
                self.form.hide()
                new_form = QtWidgets.QDialog()
                self.msg = Ui_MSG()
                self.msg.setupUi(new_form)
                new_form.show()
                self.msg.message_box.setText(msg_line + ' File Not Found -> MessageToUser: [ Please check '+ msg_line + ' whether exits!]')
                new_form.exec_()
                self.form.show()
        except:
            path = os.getcwd().replace('\\', '/') + '/Log'
            log_write(path, msg_line, r' File Not Found -> MessageToUser: [ '+ msg_line +' MAP File Not Found, please check your input or call Line Support.]')
            self.form.hide()
            new_form = QtWidgets.QDialog()
            self.msg = Ui_MSG()
            self.msg.setupUi(new_form)
            new_form.show()
            self.msg.message_box.setText(msg_line + ' File Not Found -> MessageToUser: [ '+ msg_line +' MAP File Not Found, please check your input or call Line Support.]')
            new_form.exec_()
            self.form.show()

    def SETTING(self):                                          ###SETTING槽函数
        # self.form.hide()
        new_form = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(new_form)
        new_form.show()
        ###回传读取到的demo信息到Settings上
        if STATUS != 'True':
            self.ui.box_2.setChecked(True)
        else:
            self.ui.box_1.setChecked(True)
        if File_Format == 'Origin':
            self.ui.box_3.setChecked(True)
        elif File_Format == 'Input':
            self.ui.box_4.setChecked(True)
        else:
            self.ui.box_5.setChecked(True)
        self.ui.CS_0.setText(color_para[0])
        self.ui.CS_1.setText(color_para[1])
        self.ui.CS_2.setText(color_para[2])
        self.ui.CS_3.setText(color_para[3])
        self.ui.CS_4.setText(color_para[4])
        self.ui.CS_5.setText(color_para[5])
        self.ui.CS_6.setText(color_para[6])
        self.ui.CS_7.setText(color_para[7])
        self.ui.CS_8.setText(color_para[8])
        self.ui.CS_9.setText(color_para[9])
        self.ui.CS_10.setText(color_para[10])
        self.ui.CS_11.setText(color_para[11])
        self.ui.CS_12.setText(color_para[12])
        self.ui.CS_13.setText(color_para[13])
        self.ui.CS_14.setText(color_para[14])
        self.ui.CS_15.setText(color_para[15])
        self.ui.CS_16.setText(color_para[16])
        self.ui.CS_17.setText(color_para[17])
        self.ui.CS_18.setText(color_para[18])
        self.ui.CS_19.setText(color_para[19])
        self.ui.CS_20.setText(color_para[20])
        self.ui.CS_21.setText(color_para[21])
        self.ui.CS_22.setText(color_para[22])
        self.ui.CS_23.setText(color_para[23])
        self.ui.CS_24.setText(color_para[24])
        self.ui.CS_25.setText(color_para[25])
        self.ui.CS_26.setText(color_para[26])
        self.ui.CS_27.setText(color_para[27])
        self.ui.CS_28.setText(color_para[28])
        self.ui.CS_29.setText(color_para[29])
        self.ui.CS_30.setText(color_para[30])
        self.ui.CS_31.setText(color_para[31])
        self.ui.CS_32.setText(color_para[32])
        self.ui.CS_33.setText(color_para[33])
        self.ui.CS_34.setText(color_para[34])
        self.ui.CS_35.setText(color_para[35])
        self.ui.CS_36.setText(color_para[36])
        self.ui.CS_37.setText(color_para[37])
        self.ui.CS_38.setText(color_para[38])
        self.ui.CS_39.setText(color_para[39])
        self.ui.CL_0.setStyleSheet("background-color: rgb" + color_para[0] + ";")
        self.ui.CL_1.setStyleSheet("background-color: rgb" + color_para[1] + ";")
        self.ui.CL_2.setStyleSheet("background-color: rgb" + color_para[2] + ";")
        self.ui.CL_3.setStyleSheet("background-color: rgb" + color_para[3] + ";")
        self.ui.CL_4.setStyleSheet("background-color: rgb" + color_para[4] + ";")
        self.ui.CL_5.setStyleSheet("background-color: rgb" + color_para[5] + ";")
        self.ui.CL_6.setStyleSheet("background-color: rgb" + color_para[6] + ";")
        self.ui.CL_7.setStyleSheet("background-color: rgb" + color_para[7] + ";")
        self.ui.CL_8.setStyleSheet("background-color: rgb" + color_para[8] + ";")
        self.ui.CL_9.setStyleSheet("background-color: rgb" + color_para[9] + ";")
        self.ui.CL_10.setStyleSheet("background-color: rgb" + color_para[10] + ";")
        self.ui.CL_11.setStyleSheet("background-color: rgb" + color_para[11] + ";")
        self.ui.CL_12.setStyleSheet("background-color: rgb" + color_para[12] + ";")
        self.ui.CL_13.setStyleSheet("background-color: rgb" + color_para[13] + ";")
        self.ui.CL_14.setStyleSheet("background-color: rgb" + color_para[14] + ";")
        self.ui.CL_15.setStyleSheet("background-color: rgb" + color_para[15] + ";")
        self.ui.CL_16.setStyleSheet("background-color: rgb" + color_para[16] + ";")
        self.ui.CL_17.setStyleSheet("background-color: rgb" + color_para[17] + ";")
        self.ui.CL_18.setStyleSheet("background-color: rgb" + color_para[18] + ";")
        self.ui.CL_19.setStyleSheet("background-color: rgb" + color_para[19] + ";")
        self.ui.CL_20.setStyleSheet("background-color: rgb" + color_para[20] + ";")
        self.ui.CL_21.setStyleSheet("background-color: rgb" + color_para[21] + ";")
        self.ui.CL_22.setStyleSheet("background-color: rgb" + color_para[22] + ";")
        self.ui.CL_23.setStyleSheet("background-color: rgb" + color_para[23] + ";")
        self.ui.CL_24.setStyleSheet("background-color: rgb" + color_para[24] + ";")
        self.ui.CL_25.setStyleSheet("background-color: rgb" + color_para[25] + ";")
        self.ui.CL_26.setStyleSheet("background-color: rgb" + color_para[26] + ";")
        self.ui.CL_27.setStyleSheet("background-color: rgb" + color_para[27] + ";")
        self.ui.CL_28.setStyleSheet("background-color: rgb" + color_para[28] + ";")
        self.ui.CL_29.setStyleSheet("background-color: rgb" + color_para[29] + ";")
        self.ui.CL_30.setStyleSheet("background-color: rgb" + color_para[30] + ";")
        self.ui.CL_31.setStyleSheet("background-color: rgb" + color_para[31] + ";")
        self.ui.CL_32.setStyleSheet("background-color: rgb" + color_para[32] + ";")
        self.ui.CL_33.setStyleSheet("background-color: rgb" + color_para[33] + ";")
        self.ui.CL_34.setStyleSheet("background-color: rgb" + color_para[34] + ";")
        self.ui.CL_35.setStyleSheet("background-color: rgb" + color_para[35] + ";")
        self.ui.CL_36.setStyleSheet("background-color: rgb" + color_para[36] + ";")
        self.ui.CL_37.setStyleSheet("background-color: rgb" + color_para[37] + ";")
        self.ui.CL_38.setStyleSheet("background-color: rgb" + color_para[38] + ";")
        self.ui.CL_39.setStyleSheet("background-color: rgb" + color_para[39] + ";")
        self.ui.BISData.setText(BISDATA)
        self.ui.LEFT.setValue(self.form.geometry().x())
        self.ui.TOP.setValue(self.form.geometry().y())
        self.ui.WIDTH.setValue(self.form.geometry().width())
        self.ui.HEIGHT.setValue(self.form.geometry().height())
        self.ui.BISLog.setText(BISLOG)
        self.ui.Model_2.setText(BISMODEL)
        new_form.exec_()
        self.form.show()

def new_report(test_report):###找出某个文件夹下最新的一个文件
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))
    file_new = os.path.join(test_report, lists[-1])
    return file_new

def log_write(path, ifm, state):###LOG的撰写
    local_time = time.strftime('%Y%m%d', time.localtime(time.time()))
    AppName = 'MEMS-INSPECTION'
    Hostname = socket.gethostname()
    log_name = local_time + '_' + AppName + '_' + Hostname + '.log'###文件名的格式
    log_file = path +'/'+ log_name
    logging.basicConfig(filename=log_file,
                        format='[%(asctime)s: %(message)s]',
                        level=logging.DEBUG,
                        filemode='a',
                        datefmt='%Y-%m-%d %I:%M:%S ')
    msg = [ifm,  state]
    log_msg = ''.join(msg)
    logging.info(log_msg)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     start_time = cv2.getTickCount()
     splash = QtWidgets.QSplashScreen(QtGui.QPixmap("MEMS_cat.jpg"))    ###设置开机图片
     splash.show()
     font = QtGui.QFont()
     font.setPointSize(20)                                              ###提示语的字体颜色
     #font.setBold(True)
     font.setWeight(15)
     splash.setFont(font)
     form = QtWidgets.QMainWindow()                                     ###启动主界面
     window = Ui_MainWindow()
     window.setupUi(form)
     form = QtWidgets.QMainWindow()
     window = Ui_MainWindow()
     window.setupUi(form)
     for i in range(2):
         splash.showMessage("Starting.", QtCore.Qt.AlignCenter| QtCore.Qt.AlignBottom, QtCore.Qt.red)
         cv2.waitKey(1000)
         splash.showMessage("Starting..", QtCore.Qt.AlignCenter| QtCore.Qt.AlignBottom, QtCore.Qt.green)
         cv2.waitKey(1000)
         splash.showMessage("Starting...", QtCore.Qt.AlignCenter| QtCore.Qt.AlignBottom, QtCore.Qt.blue)
         cv2.waitKey(1000)
     splash.finish(form)                                                ###关闭启动界面

     path = os.getcwd().replace('\\', '/')+'/Models'                    ###读取model文件
     file_newest = new_report(path)
     data = []
     src = open(file_newest, 'r')
     for line in src:
         data.append(line.rstrip("\n"))

     STATUS  = data[0]
     BISDATA=   data[41]
     X      =   int(data[42])
     Y      =   int(data[43])
     W      =   int(data[44])
     H      =   int(data[45])
     BISLOG =   data[46]
     BISMODEL = data[47]
     File_Format = data[48]
     for i in range(1, 41):
        color_para.append(data[i])
     dispaly_time = cv2.getTickCount()
     tic_1 = (dispaly_time - start_time) / cv2.getTickFrequency()
     tic_1_2 = Decimal(tic_1).quantize(Decimal('0.00'))###计算启动时间
     log_write(BISLOG, 'MEMS-INSPECTION starts, it takes ', str(tic_1_2) + 's.')
     if STATUS != 'True':
         log_write(BISLOG, 'File status:', ' Local setting')
     else:
         log_write(BISLOG, 'File status:', ' Shared setting')
     log_write(BISLOG, 'BISData_Path    =  ', BISDATA)
     log_write(BISLOG, 'BISLog_Path     =  ', BISLOG)
     log_write(BISLOG, 'BISModel_Path   =  ', BISMODEL)
     log_write(BISLOG, 'Test_File_Format   =  ', File_Format)
     log_write(BISLOG, 'Offset:            ', 'X= ' + data[42] +', Y= ' + data[43] +  ', W= ' + data[44] + ', H = ' + data[45]  )
     log_write(BISLOG, 'COLOR_0-4       =  ', data[1] + ', ' + data[2] + ', ' + data[3] + ', ' + data[4] + ', ' + data[5])
     log_write(BISLOG, 'COLOR_5-9       =  ', data[6] + ', ' + data[7] + ', ' + data[8] + ', ' + data[9] + ', ' + data[10])
     log_write(BISLOG, 'COLOR_10-14     =  ', data[11] + ', ' + data[12] + ', ' + data[13] + ', ' + data[14] + ', ' + data[15])
     log_write(BISLOG, 'COLOR_15-19     =  ', data[16] + ', ' + data[17] + ', ' + data[18] + ', ' + data[19] + ', ' + data[20])
     log_write(BISLOG, 'COLOR_20-24     =  ', data[21] + ', ' + data[22] + ', ' + data[23] + ', ' + data[24] + ', ' + data[25])
     log_write(BISLOG, 'COLOR_25-29     =  ', data[26] + ', ' + data[27] + ', ' + data[28] + ', ' + data[29] + ', ' + data[30])
     log_write(BISLOG, 'COLOR_30-34     =  ', data[31] + ', ' + data[32] + ', ' + data[33] + ', ' + data[34] + ', ' + data[35])
     log_write(BISLOG, 'COLOR_35-39     =  ', data[36] + ', ' + data[37] + ', ' + data[38] + ', ' + data[39] + ', ' + data[40])

     window.form.move(X, Y)
     window.form.resize(W, H)
     panel_path = BISDATA

     img = cv2.imread('./bg/whiteground_init.jpg')
     height, width = img.shape[:2]
     bytesPerLine = 3 * width
     qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
     pix = QPixmap(qImg)
     window.IMGLABEL.setPixmap(pix)
     window.IMGLABEL.setScaledContents(True)
     form.show()

     app.exec_()###先退出界面在计算结束时间
     end_time = cv2.getTickCount()
     tic_2 = (end_time - start_time) / cv2.getTickFrequency()
     tic_2_2 = Decimal(tic_2).quantize(Decimal('0.00'))
     log_write(BISLOG, 'MEMS-INSPECTION ends, it takes ', str(tic_2_2) + 's totally.\n')
     sys.exit()###退出整个程序

