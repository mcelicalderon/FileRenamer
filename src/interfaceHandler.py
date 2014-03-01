from interface import *
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Wrapper(QtGui.QMainWindow):
    def __init__(self, ui):
        QtGui.QMainWindow.__init__(self)
        self.gui = ui

    def selectPath(self):
        dir = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.gui.lineEdit_path.setText(dir)
        dirStr = ""
        for file in os.listdir(dir):
            dirStr+="{file}\n".format(file=str(file))
        self.gui.textBrowser_display.setText(dirStr)

    def setListeners(self):
        QtCore.QObject.connect(self.gui.pushButton_selectPath, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectPath)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    wrapper = Wrapper(ui)
    wrapper.setListeners()
    sys.exit(app.exec_())
