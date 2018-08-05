import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, None)
        self.initUI()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        app.aboutToQuit.connect(self.closeEvent)

    def closeEvent(self, event):

        f = QMessageBox.question(self, 'Qt Editor', "Do you want to Exit?", QMessageBox.Save | QMessageBox.Yes |
                                                                               QMessageBox.No, QMessageBox.Save)
        if f == QMessageBox.Save:
            Main.Save(self)
        elif f == QMessageBox.Yes:
            event.accept()
        elif f == QMessageBox.No:
            event.ignore()

    def initUI(self):

        text = QTextEdit(self)
        text.setTabStopWidth(20000)
        self.setCentralWidget(text)

        self.setGeometry(100, 150, 600, 500)
        self.setWindowTitle("Qt Editor")
        self.setWindowIcon(QIcon("icons/a.png"))
        self.show()

        new = QAction(QIcon("icons/b.png"), "New", self)
        new.setStatusTip("Create a new document.")
        new.triggered.connect(self.New)

        open = QAction(QIcon("icons/d.png"), "Open file", self)
        open.setStatusTip("Open a document")
        open.triggered.connect(self.Open)

        save = QAction(QIcon("icons/c.png"), "Save", self)
        save.setStatusTip("Save document")
        save.triggered.connect(self.Save)

        exit = QAction(QIcon("icons/e.png"), 'Exit', self)
        exit.setStatusTip('Exit application')
        exit.triggered.connect(self.Exit)

        cut = QAction(QIcon("icons/f.png"), "Cut", self)
        cut.setStatusTip("Delete and copy text to clipboard")
        cut.triggered.connect(self.Cut)

        copy = QAction(QIcon("icons/g.png"), "Copy", self)
        copy.setStatusTip("Copy text to clipboard")
        copy.triggered.connect(self.Copy)

        paste = QAction(QIcon("icons/j.png"), "Paste", self)
        paste.setStatusTip("Paste text from clipboard")
        paste.triggered.connect(self.Paste)

        undo = QAction(QIcon("icons/h.png"), "Undo", self)
        undo.setStatusTip("Undo last action")
        undo.triggered.connect(self.Undo)

        redo = QAction(QIcon("icons/i.png"), "Redo", self)
        redo.setStatusTip("Redo last undone thing")
        redo.triggered.connect(self.Redo)

        info = QAction(QIcon("icons/k.png"), "About Qt Editor", self)
        info.setStatusTip("Information by Developer")
        info.triggered.connect(self.Info)
        
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        help = menubar.addMenu("Help")

        file.addAction(new)
        file.addAction(open)
        file.addAction(save)
        file.addAction(exit)

        edit.addAction(undo)
        edit.addAction(redo)
        edit.addAction(cut)
        edit.addAction(copy)
        edit.addAction(paste)
        
        help.addAction(info)

    def New(self):
        self.new = Main()
        self.new.show()

    def Open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.*)All Files")[0]
        if filename == '':
            Main()
        else:
            f = open(filename, 'r')
            file = f.read()
            self.text.setText(file)
            f.close()

    def Save(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', ".", "(*.*)All Files")[0]
        if filename == '':
            Main()
        else:
            f = open(filename, 'w')
            file = self.text.toPlainText()
            f.write(file)
            f.close()

    def Undo(self):
        self.text.undo()

    def Redo(self):
        self.text.redo()

    def Cut(self):
        self.text.cut()

    def Copy(self):
        self.text.copy()

    def Paste(self):
        self.text.paste()

    def Exit(self):
        f = QMessageBox.question(self, 'Qt Editor', "Do you want to Exit?", QMessageBox.Save | QMessageBox.Yes |
                                 QMessageBox.No, QMessageBox.Save)
        if f == QMessageBox.Save:
            Main.Save(self)
        elif f == QMessageBox.Yes:
            QMainWindow.close(self)
        elif f == QMessageBox.No:
            QMainWindow.destroy(self, destroyWindow=False)

    def Info(self):
         f = QMessageBox.about(self, "About","Qt Editor \n\n Version 1 \n\n A simple text editor made using python3 "
                                             "and PyQt5 \n\n Developed by Kuldeep Sharma")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
