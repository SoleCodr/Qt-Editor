import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, None)
        self.initUI()


    def initUI(self):

        new = QAction(QIcon("D://b.png"), "New", self)
        new.setStatusTip("Create a new document.")
        new.triggered.connect(self.New)

        open = QAction(QIcon("D://d.png"), "Open file", self)
        open.setStatusTip("Open a document")
        open.triggered.connect(self.Open)

        save = QAction(QIcon("D://c.png"), "Save", self)
        save.setStatusTip("Save document")
        save.triggered.connect(self.Save)

        exit = QAction(QIcon("D://e.png"), 'Exit', self)
        exit.setStatusTip('Exit application')
        exit.triggered.connect(self.Exit)

        cut = QAction(QIcon("D://f.png"), "Cut", self)
        cut.setStatusTip("Delete and copy text to clipboard")
        cut.triggered.connect(self.Cut)

        copy = QAction(QIcon("D://g.png"), "Copy", self)
        copy.setStatusTip("Copy text to clipboard")
        copy.triggered.connect(self.Copy)

        paste = QAction(QIcon("D://j.png"), "Paste", self)
        paste.setStatusTip("Paste text from clipboard")
        paste.triggered.connect(self.Paste)

        undo = QAction(QIcon("D://h.png"), "Undo", self)
        undo.setStatusTip("Undo last action")
        undo.triggered.connect(self.Undo)

        redo = QAction(QIcon("D://i.png"), "Redo", self)
        redo.setStatusTip("Redo last undone thing")
        redo.triggered.connect(self.Redo)

        info = QAction(QIcon("D://k.png"), "About Qt Editor", self)
        info.setStatusTip("Information by Developer")
        info.triggered.connect(self.Info)

        self.text = QTextEdit(self)
        self.text.setTabStopWidth(20)
        self.setCentralWidget(self.text)

        self.setGeometry(100, 150, 600, 500)
        self.setWindowTitle("Qt Editor")
        self.setWindowIcon(QIcon("D://a.png"))
        self.show()

        # ------- Menubar --------------------------------------

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
        self.text.clear()

    def Open(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        f = open(filename, 'r')
        file = f.read()
        self.text.setText(file)
        f.close()

    def Save(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        f = open(filename, 'w')
        file = f.write()
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
            Main.Save()
        elif f == QMessageBox.Yes:
            Main.close()
        else:
            Main.destroy()
        self.show()

    def Info(self):
         f = QMessageBox.about(self, "About","Qt Editor \n\n Version 1 \n\n A simple text editor made using python3 "
                                             "and PyQt5 \n\n Developed by Kuldeep Sharma")

def main():
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()