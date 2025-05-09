from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
import os
import subprocess

shows_folder_path= '//liv1/shows'
folders_to_remove = ['Home','ingest','lib','bid','publish']
rv_path = 'C:\\Program Files\\ShotGrid\\RV-2021.1.0\\bin\\rv.exe'
# rv_path ='C:\\Program Files\\Shotgun\\RV-2021.0.0\\bin\\rv.exe'

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file = QFile("plate_select_tool.ui")
        ui_file.open(QFile.ReadOnly)
        self.loader = QUiLoader()
        self.ui = self.loader.load(ui_file)

        # singal
        self.ui.show_le.returnPressed.connect(self.get_show_name)

        # Q Complete
        wordList = [x for x in os.listdir(shows_folder_path)]
        completer = QCompleter(wordList, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.show_le.setCompleter(completer)
        self.ui.show()  

    def get_show_name(self):
        # print(self.ui.show_le.text())
        shot_path = os.path.join(shows_folder_path, self.ui.show_le.text())
        shots = [x for x in os.listdir(shot_path)]
        self.ui.shot_lw.clear()
        self.ui.in_lw.clear()
        self.ui.plate_lw.clear()
        self.ui.shot_lw.addItems(list(set(shots) - set(folders_to_remove)))
        # singal
        self.ui.shot_lw.itemClicked.connect(self.get_plates_folder)
        

    def get_plates_folder(self,item):
        # print('get_plates_folder')
        in_path = os.path.join(shows_folder_path,self.ui.show_le.text(),self.ui.shot_lw.currentItem().text(),'in','plates')
        ins = [x for x in os.listdir(in_path)]
        self.ui.in_lw.clear()
        self.ui.plate_lw.clear()
        self.ui.in_lw.addItems(ins)
        # singal
        self.ui.in_lw.itemClicked.connect(self.get_plates)

    def get_plates(self, item):
        # print('get_plates')
        plates_path_scan = os.path.join(shows_folder_path,self.ui.show_le.text(),self.ui.shot_lw.currentItem().text(),'in','plates',item.text())

        plates_path=[]
        for root,folders,files in os.walk(plates_path_scan):
            # print(root,folders,files)
            if files:
                print(root)
                # plates_path.append(os.path.join(root,files[0]))
                file_list =[]
                for f in files:
                	file_list.append(os.path.join(root,f))

                plates_path.extend(file_list)
                # os.path.join(root)
        print(plates_path)
        # os.walk(plates_path)
        # plates = [x for x in os.listdir(plates_path[0])]
        # print(plates)
        self.ui.plate_lw.clear()
        self.ui.plate_lw.addItems(plates_path)
        # # singal
        self.ui.plate_lw.itemDoubleClicked.connect(self.open_rv_file)

    def open_rv_file(self,item):
        file_path = os.path.join(shows_folder_path,self.ui.show_le.text(),self.ui.shot_lw.currentItem().text(),self.ui.plate_lw.currentItem().text())
        print('file_path',file_path)
        try:
        	subprocess.Popen([rv_path, file_path])
        except Exception as e:
        	raise e


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MyMainWindow()
    sys.exit(app.exec_())