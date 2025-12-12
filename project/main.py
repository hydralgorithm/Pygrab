# PyGrab
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("resource/Icons/PyGrab_icon.png"))
        self.setWindowTitle("PyGrabber")
        self.setGeometry(700, 300, 600, 600)
        self.setStyleSheet("background-color: black")

        self.iniUI()

    def iniUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # ---- Main vertical layout ----
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop | Qt.AlignHCenter)   # <--- THIS centers and keeps top
        central_widget.setLayout(vbox)

        # ---- Add title label ----
        intro_label = QLabel("Welcome to PyGrab 🐍▶️", self)

        # Load custom font
        font_id = QFontDatabase.addApplicationFont("resource/Fonts/ByteBounce.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 30)   # <--- Much better size

        intro_label.setFont(my_font)

        intro_label.setStyleSheet("""
            color: #a0ff7a;
            padding-top: 20px;
            padding-bottom: 20px;
        """)

        vbox.addWidget(intro_label)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()