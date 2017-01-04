#coding:utf-8
import Orange
import sys,codecs

from PyQt4 import QtCore, QtGui, uic
qtCreatorFile = "Tasarla.xml"


Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.urlSecButton.clicked.connect(self.urlSec)
        self.hesaplaButton.clicked.connect(self.hesapla)
        self.hesaplamaAlan.setVisible(False)

    def urlSec(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Dosya Aç')
        self.textEdit.setText(fileName)
        dosyaAc=codecs.open(fileName,encoding='utf8').read()
        self.plainTextEdit.setPlainText(dosyaAc)
        #print fileName
        #DosyaYolu=os.path.basename(str(fileName))

    def hesapla(self):
        self.hesaplamaAlan.setVisible(True)
        urlAl= self.textEdit.toPlainText()
        data = Orange.data.Table(urlAl)
        rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.1)
        #print "%5s   %5s" % ("supp", "conf")
        self.hesaplamaAlan.insertPlainText(str("%5s   %5s" "\n" % ("supp", "conf")))
        for r in rules:
            #print "%5.3f   %5.3f   %s" % (r.support, r.confidence, r)
            self.hesaplamaAlan.insertPlainText(str("%5.3f   %5.3f   %s" "\n" % (r.support, r.confidence, r)))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())