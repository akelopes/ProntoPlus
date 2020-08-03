from .main_vhandler import MainVHandler
from .patients_page_vhandler import PatientsPageVHandler
from .patients_form_page_vhandler import PatientFormPageVHandler
from .record_writer_vhandler import RecordWriterVHandler
from .options_page_vhandler import OptionsPageVHandler

import PySide2.QtWidgets as qtW
import sys


def start():
    app = qtW.QApplication(sys.argv)
    window = main_vhandler.MainVHandler()
    window.show()
    sys.exit(app.exec_())

