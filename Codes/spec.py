import sys
from PyQt4 import QtCore, QtGui,uic
from PyQt4.QtCore import *
import spectral.io.envi as envi
import matplotlib.pyplot as plt
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

class MyApp3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(440, 670)
        self.menubar = QtGui.QMenuBar(Dialog)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        
        self.actionSpectral_Library_File = QtGui.QAction(self.menuFile)
        self.actionSpectral_Library_File.setObjectName(_fromUtf8("actionSpectral_Library_File"))
        self.actionSpectral_Library_File.triggered.connect(self.open_file)
        
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20,20,400,540))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(0,0,400,540))
        self.widget.setObjectName(_fromUtf8("Widget"))
        self.listview = QtGui.QListWidget(self.widget)
        self.listview.setGeometry(QtCore.QRect(10,20,380,500))
        self.listview.setObjectName(_fromUtf8("listview"))
        self.listview.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        
        self.groupBox1 = QtGui.QGroupBox(Dialog)
        self.groupBox1.setGeometry(QtCore.QRect(20,580,400,70))
        self.groupBox1.setTitle(_fromUtf8(""))
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.widget1 = QtGui.QWidget(self.groupBox1)
        self.widget1.setGeometry(QtCore.QRect(0,0,400,70))
        self.widget1.setObjectName(_fromUtf8("Widget1"))
        self.Select_All = QtGui.QPushButton(self.widget1)
        self.Select_All.setGeometry(QtCore.QRect(20,20,71,30))
        self.Select_All.setObjectName(_fromUtf8("Select_All"))
        self.Select_All.clicked.connect(self.select_all)
        
        self.Plot = QtGui.QPushButton(self.widget1)
        self.Plot.setGeometry(QtCore.QRect(319,20,41,30))
        self.Plot.setObjectName(_fromUtf8("Plot"))
        self.Plot.clicked.connect(self.plot_map)
        self.menuFile.addAction(self.actionSpectral_Library_File)
        self.menubar.addMenu(self.menuFile)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.retranslateUi(Dialog)
        lib='foo'
    def open_file(self):
        self.name = QtGui.QFileDialog.getOpenFileName(None, 'Open File')
        global lib
        lib = envi.open(str(self.name))
        collection = lib.names
        for x in collection:
            self.listview.addItem(x)
    def select_all(self):
            allitems=self.listview.findItems("*",Qt.MatchWrap|Qt.MatchWildcard)
            for item in allitems:
                item.setSelected(True)
    def plot_map(self):
        indexlist = self.listview.selectedItems()
        for item in indexlist:
            x=lib.names[QModelIndex.row(self.listview.indexFromItem(item))]
            y=str(x)
            plt.plot(lib.spectra[QModelIndex.row(self.listview.indexFromItem(item))],label = y)
        plt.legend(bbox_to_anchor=(1.00,1.10),loc=0,prop={'size':9}).draggable()
        plt.xlabel("Band Value")
        plt.ylabel('Reflectance')
        plt.title('Spectral Profile')
        plt.show()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Spectral Library Viewer", None))
        self.menuFile.setTitle(_translate("Dialog","File",None))
        self.actionSpectral_Library_File.setText(_translate("Dialog", "Spectral Library File", None))
        self.Select_All.setText(_translate("Dialog", "Select All", None))
        self.Plot.setText(_translate("Dialog", "Plot", None))
class spectral (QtGui.QDialog, MyApp3):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = MyApp3()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        
app = QtGui.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('Icon\hydas.png'))
myapp = spectral()
myapp.show()
app.exec_()
__author__ = 'Keshav Goswami and Akriti'
