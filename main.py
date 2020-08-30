################################################################################
#
# BY: KIRAN.B.GANGAPPA
# PROJECT MADE WITH: Qt Designer, PyCharm
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
################################################################################
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from app_css import style_sheet


class UiMainWindow(object):

    def setup_ui(self, MainWindow):
        """Create UI for the app."""

        # Main Window UI
        MainWindow.setWindowTitle("Fat Burning Calculator")
        MainWindow.setWindowIcon(QtGui.QIcon('icons/fire.ico'))
        MainWindow.setFixedSize(350, 500)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.central_widget.setStyleSheet(style_sheet)

        # Header UI
        self.header_label = QtWidgets.QLabel(self.central_widget)
        self.header_label.setObjectName("header_label")
        self.header_label.setGeometry(QtCore.QRect(0, 0, 350, 60))
        self.header_label.setText("Fat Burning Calculator")
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_label.setStyleSheet(style_sheet)

        # Combobox label UI
        self.age_label = QtWidgets.QLabel(self.central_widget)
        self.age_label.setObjectName("app_label")
        self.age_label.setGeometry(QtCore.QRect(55, 100, 120, 60))
        self.age_label.setText("Select Age")
        self.age_label.setStyleSheet(style_sheet)

        # Combobox UI
        self.comboBox = QtWidgets.QComboBox(self.central_widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QtCore.QRect(230, 120, 70, 30))
        for age in range(1, 101):
            self.comboBox.addItem(str(age))
        self.comboBox.setStyleSheet(style_sheet)

        # Max Heart Rate label UI
        self.max_heart_rate_label = QtWidgets.QLabel(self.central_widget)
        self.max_heart_rate_label.setObjectName("app_label")
        self.max_heart_rate_label.setGeometry(QtCore.QRect(0, 190, 350, 40))
        self.max_heart_rate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.max_heart_rate_label.setText("Maximum Heart Rate")
        self.max_heart_rate_label.setStyleSheet(style_sheet)

        # Max Heart Rate value UI
        self.max_heart_rate_value = QtWidgets.QLabel(self.central_widget)
        self.max_heart_rate_value.setObjectName("app_value")
        self.max_heart_rate_value.setGeometry(QtCore.QRect(0, 250, 350, 40))
        self.max_heart_rate_value.setAlignment(QtCore.Qt.AlignCenter)
        self.max_heart_rate_value.setText("0 bpm")
        self.max_heart_rate_value.setStyleSheet(style_sheet)

        # Fat Burning Heart Rate label UI
        self.fat_burn_rate_label = QtWidgets.QLabel(self.central_widget)
        self.fat_burn_rate_label.setObjectName("app_label")
        self.fat_burn_rate_label.setGeometry(QtCore.QRect(0, 320, 350, 40))
        self.fat_burn_rate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fat_burn_rate_label.setText("Fat Burning Heart Rate")
        self.fat_burn_rate_label.setStyleSheet(style_sheet)

        # Fat Burning Heart Rate value UI
        self.fat_burn_rate_value = QtWidgets.QLabel(self.central_widget)
        self.fat_burn_rate_value.setObjectName("app_value")
        self.fat_burn_rate_value.setGeometry(QtCore.QRect(0, 400, 350, 40))
        self.fat_burn_rate_value.setAlignment(QtCore.Qt.AlignCenter)
        self.fat_burn_rate_value.setText("0 bpm")
        self.fat_burn_rate_value.setStyleSheet(style_sheet)

        MainWindow.setCentralWidget(self.central_widget)

        # Calculate upon change in age
        self.comboBox.activated.connect(self.age_selected)

    def age_selected(self):
        """Calculate max heart rate and fat burning heart rate in bpm(beats per minute) using age."""

        age = int(self.comboBox.currentText())
        max_heart_rate = round(206.9 - (0.67 * age))
        fat_burn_heart_rate = round(0.65 * max_heart_rate)

        self.max_heart_rate_value.setText(f"{max_heart_rate} bpm")
        self.fat_burn_rate_value.setText(f"{fat_burn_heart_rate} bpm")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/CenturyGothicRegular.ttf')
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
