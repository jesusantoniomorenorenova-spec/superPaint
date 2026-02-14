#pip install pyqt6 pyqt6-tools

from PyQt6 import QtWidgets, uic
import sys
import os
from controller import MainController
from canvas import Canvas


class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Obtener ruta correcta del archivo actual
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(base_dir, "views", "main_window.ui")

        uic.loadUi(ui_path, self)

        self.controller = MainController(self, self)


app = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec())

