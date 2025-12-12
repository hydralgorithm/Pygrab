# PyGrab
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("resource/Icons/PyGrab_icon.png"))
        self.setWindowTitle("PyGrabber")
        self.setGeometry(700, 300, 600, 600)
        self.setStyleSheet("background-color: #363835")

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
        #----Internal horizontal layout 1
        hbox1 = QHBoxLayout()
        hbox1.setAlignment(Qt.AlignHCenter)
        vbox.addLayout(hbox1)

        # Row 1
        #url label
        label_url = QLabel("Enter URL: ", self)
        label_url.setStyleSheet("font-size: 20px;"
                                "color: #d0f7c1")
        #url input
        url_input = QLineEdit(self)
        url_input.setPlaceholderText("Paste youtube link here...")
        url_input.setStyleSheet("font-size: 20px;"
                                "padding: 10px;"
                                "border-radius: 5px;"
                                "background-color: #ddebd8;"
                                "border: none")
        #download button
        download_btn = QPushButton("Download", self)
        download_btn.setCursor(Qt.PointingHandCursor)
        download_btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                padding: 10px 20px;
                background-color: #4caf50;
                color: white;
                border-radius: 5px;
                border: 2px solid transparent;
            }

            QPushButton:hover {
                background-color: #6fd66f;   /* lighter green */
            }

            QPushButton:pressed {
                border: 2px solid #ffffff;   /* white outline on click */
                background-color: #45a049;   /* darker green click effect */
            }
        """)


        hbox1.addWidget(label_url)
        hbox1.addWidget(url_input)
        hbox1.addWidget(download_btn)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()