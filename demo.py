# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QImage
import cv2
import numpy as np 
import logging
import sys
import math
import time
from collections import OrderedDict


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(ch)

def imresize_bilinear(original_img, new_h, new_w):
    '''
    This is custom implementation of image resize operation.
    For citation, refer to references in README
    '''

    logger.info("using custom resize function")
    old_h, old_w, ch = original_img.shape
    
    resized = np.zeros((new_h, new_w, ch))
    
    w_scale_factor = (old_w ) / (new_w ) if new_h != 0 else 0
    h_scale_factor = (old_h ) / (new_h ) if new_w != 0 else 0
    
    for i in range(new_h):
        for j in range(new_w):
            
            x = i * h_scale_factor
            y = j * w_scale_factor
            
            x_floor = math.floor(x)
            x_ceil = min( old_h - 1, math.ceil(x))
            y_floor = math.floor(y)
            y_ceil = min(old_w - 1, math.ceil(y))

            if (x_ceil == x_floor) and (y_ceil == y_floor):
                q = original_img[int(x), int(y), :]
            elif (x_ceil == x_floor):
                q1 = original_img[int(x), int(y_floor), :]
                q2 = original_img[int(x), int(y_ceil), :]
                q = q1 * (y_ceil - y) + q2 * (y - y_floor)
            elif (y_ceil == y_floor):
                q1 = original_img[int(x_floor), int(y), :]
                q2 = original_img[int(x_ceil), int(y), :]
                q = (q1 * (x_ceil - x)) + (q2    * (x - x_floor))
            else:
                v1 = original_img[x_floor, y_floor, :]
                v2 = original_img[x_ceil, y_floor, :]
                v3 = original_img[x_floor, y_ceil, :]
                v4 = original_img[x_ceil, y_ceil, :]

                q1 = v1 * (x_ceil - x) + v2 * (x - x_floor)
                q2 = v3 * (x_ceil - x) + v4 * (x - x_floor)
                q = q1 * (y_ceil - y) + q2 * (y - y_floor)

            resized[i,j,:] = q
    return resized.astype(np.uint8)


class Ui_MainWindow(object):

    def __init__(self, path_, use_optimized):
        self.MAX_WIDTH = 512
        self.MAX_HEIGHT = 512
        self.use_optimized = use_optimized
        self.filename = None
        self.tmp = None
        self. scale_now = 1
        self.contrast_value_now = 1
        self.default_image_path = path_
        self.image = cv2.imread(default_image_path)
        img = self.image.copy()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.default_image = QImage(img, img.shape[1],img.shape[0],img.strides[0],QImage.Format.Format_RGB888)
        if use_optimized:
            logger.info("using OpenCV's optimized resize method")
        else:
            logger.info("using custom resize implementation, resize operation would be slower")

        self.cache = OrderedDict()
        self.cache_threshold = 5


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 640)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.default_image))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setValue(50)
        self.horizontalLayout.addWidget(self.verticalSlider)
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_2.setValue(50)
        self.horizontalLayout.addWidget(self.verticalSlider_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.gridLayout.addWidget(self.radioButton, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        self.verticalSlider.valueChanged['int'].connect(self.scale) # type: ignore
        self.verticalSlider_2.valueChanged['int'].connect(self.contrast_value) # type: ignore
        self.pushButton.clicked.connect(self.load_image) # type: ignore
        self.pushButton_2.clicked.connect(self.savePhoto) # type: ignore
        self.radioButton.toggled['bool'].connect(self.set_resize_modes) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_resize_modes(self, isChecked):
        '''
        This method sets the use_optimized flag that decides which method to use for image resize.
        OpenCV resize implementation is optimized one and hence runs faster faster compared to custom Python implementation
        '''
        if isChecked:
            logger.info("switched to OpenCV's optimized resize method")
            self.use_optimized = True
        else:
            logger.info("switched to custom resize implementation")
            self.use_optimized = False
        return


    def load_image(self):
        '''
        This method opens file explorer to load an image in qt window.
        '''

        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
        logger.info("loaded file: {}".format(self.filename))
        self.cache = OrderedDict()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.radioButton.setText(_translate("MainWindow", "use_optimized_opencv_resize"))

    def setPhoto(self,image):
        '''
        This method decides what specific region of image to show in the qt window.
        Since the images can be of any dimensions, for the sake of simplicity, 
        if image is bigger than (512, 512) pixels then I'm showing the center-cropped image.
        self.tmp has the copy of full-resolution processed image.
        '''

        self.tmp = image
        
        cropped_image = image
        if image.shape[0]> self.MAX_HEIGHT or image.shape[1] > self.MAX_WIDTH:
            if image.shape[1]>image.shape[0]:
                aspect_ratio = image.shape[1]/image.shape[0]
                crop_width = self.MAX_WIDTH
                crop_height = int(crop_width/aspect_ratio)
            else:
                aspect_ratio = image.shape[1]/image.shape[0]
                crop_height = self.MAX_HEIGHT
                crop_width = int(crop_height * aspect_ratio)

            r_, c_ = image.shape[:2]
            start_row = int(r_/2) - int(crop_height/2)
            end_row = start_row + crop_height
            start_col = int(c_/2) - int(crop_width/2)
            end_col = start_col + crop_width

            cropped_image = image[start_row:end_row, start_col:end_col]
        
        logger.info("original: {} \t cropped:  {}\n ----".format(image.shape[:2], cropped_image.shape[:2]))
        frame = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
        show_image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(show_image))

    def scale(self,value):
        '''
        This method converts slider value into a range of scale values for zoom
        slider value 50 belongs to scale = 1
        slider value 100 belongs to scale = 2
        slider value 0 belongs to scale = 0 [(1,1) size image ]
        '''

        if value>=50:
            value-=50
            self.scale_now = round(1 + value/50, 2)
        else:
            self.scale_now = round(value/50 + 0.001, 2)
        self.update()
        
        
    def contrast_value(self,value):
        '''
        This method converts slider values from 0-100 to -255 to +255 range.
        I have mentioned reference material in References section in README.md
        '''

        self.contrast_value_now = round((value - 50) * 5.1, 2)
        logger.info('Contrast: {}'.format(self.contrast_value_now))
        self.update()
    
    
    def changeScale(self,img,value):
        '''
        This function handles image resize related work
        '''

        dummy = self.cache.get(value, None)
        if dummy is not None:
            logger.info("found resized image in cache, re-using it, Yay!")
            return self.cache.get(value)

        logger.info("scale: {}".format(round(value, 2)))
        new_width = max(1, int(img.shape[1] * value))
        new_height = max(1, int(img.shape[0] * value))
        if self.use_optimized:
            time1 = time.time()
            tmp = cv2.resize(img, (new_width, new_height), cv2.INTER_AREA)
            time2 = time.time()
        else:
            time1 = time.time()
            tmp = imresize_bilinear(img, new_height, new_width)
            time2 = time.time()
        logger.info("time for resize : {}".format(round(time2 - time1, 4)))
        self.insert_in_cache(value, tmp)
        return tmp

    def insert_in_cache(self, key_, data):
        '''
        This method inserts image_at_specific_resolution in cache
        key is image_resolution
        value is resized image
        '''
        logger.info("len of cache : {}".format(len(self.cache)))
        if len(self.cache)>=self.cache_threshold:
            key_to_remove = list(self.cache.keys())[0]
            del self.cache[key_to_remove]
            logger.info("removed old data from cache")

        self.cache[key_] = data
        logger.info("inserted data in cache")
        return
        
    def changeContrast(self,img,value):
        '''
        This method implements contrast enhancement related code
        The implementation is from [2] reference in References in README.md
        '''
        tmp = img.copy()

        factor = 259 * (value + 255) / (255 * (259 - value) )
        for ch in range(tmp.shape[2]):
            channel = np.float32(tmp[:,:,ch])
            channel = factor * (channel - 128) + 128
            channel[channel<0] = 0
            channel[channel>255] = 255
            tmp[:, :, ch] = np.uint8(channel)
        return tmp
    
    def update(self):
        '''
        This method updates UI in qt
        '''
        img = self.changeScale(self.image,self.scale_now)
        img = self.changeContrast(img,self.contrast_value_now)
        self.setPhoto(img)
    
    def savePhoto(self):
        '''
        This method saves manipulated image to disk
        '''
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        if filename:
            cv2.imwrite(filename,self.tmp)
            logger.info('Image saved as: {}'.format(filename))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    default_image_path = "lena.png" if len(sys.argv)==1 else sys.argv[1]
    use_optimized = True
    ui = Ui_MainWindow(default_image_path, use_optimized)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
