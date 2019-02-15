# coding: utf-8

import os
import sys
import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import from_to_type


class kdYoudaoDictionary(QWidget):
    def __init__(self):
        super(kdYoudaoDictionary, self).__init__()
        loadUi("kdYoudaoDictionary.ui", self)
        for translate_type in from_to_type.translate_types:
            self.cb_from_to.addItem(translate_type[1])
        print(dir(self.le_word))

    def on_pb_translate_clicked(self):
        self._translate()

    def on_le_word_returnPressed(self):
        self._translate()

    def _translate(self):
        word = self.le_word.text().strip()
        if word == "":
            pass
        else:
            cur_type = self.cb_from_to.currentText()
            for translate_type in from_to_type.translate_types:
                if translate_type[1] == cur_type:
                    r = requests.get(
                        "http://fanyi.youdao.com/translate?&doctype=json&type={}&i={}".format(translate_type, word))
                    result = json.loads(r.text)
                    if result["errorCode"] == 0:
                        self.te_result.setText(
                            result["translateResult"][0][0]["tgt"])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = kdYoudaoDictionary()
    win.show()
    sys.exit(app.exec_())
