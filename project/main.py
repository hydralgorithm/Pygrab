# PyGrab
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout,
    QWidget, QLineEdit, QPushButton, QComboBox
)
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtCore import Qt
from pytubefix import YouTube


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

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        vbox.setSpacing(25)
        central_widget.setLayout(vbox)

        # Title
        intro_label = QLabel("Welcome to PyGrab 🐍▶️", self)
        font_id = QFontDatabase.addApplicationFont("resource/Fonts/ByteBounce.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        intro_label.setFont(QFont(font_family, 30))
        intro_label.setStyleSheet("color: #a0ff7a; padding: 20px 0;")
        vbox.addWidget(intro_label)

        # Row 1 — URL, Input, Button
        hbox1 = QHBoxLayout()
        hbox1.setAlignment(Qt.AlignHCenter)
        hbox1.setSpacing(15)
        vbox.addLayout(hbox1)

        self.label_url = QLabel("Enter URL: ", self)
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Paste YouTube link here...")

        self.download_btn = QPushButton("Download", self)
        self.download_btn.setCursor(Qt.PointingHandCursor)
        self.download_btn.clicked.connect(self.download_video)

        hbox1.addWidget(self.label_url)
        hbox1.addWidget(self.url_input)
        hbox1.addWidget(self.download_btn)

        # Row 2 — Quality
        hbox2 = QHBoxLayout()
        hbox2.setAlignment(Qt.AlignHCenter)
        hbox2.setSpacing(15)
        vbox.addLayout(hbox2)

        self.label_quality = QLabel("Enter video quality: ", self)
        self.quality_dropdown = QComboBox(self)
        self.quality_dropdown.addItems(["720p", "480p", "360p", "240p", "144p"])
        self.quality_dropdown.setCurrentText("720p")

        hbox2.addWidget(self.label_quality)
        hbox2.addWidget(self.quality_dropdown)

        # Apply all CSS
        self.apply_styles()

    def apply_styles(self):
        self.label_url.setStyleSheet("font-size: 20px; color: #d0f7c1")
        self.label_quality.setStyleSheet("font-size: 20px; color: #d0f7c1")

        self.url_input.setStyleSheet("""
            font-size: 20px;
            padding: 10px;
            border-radius: 5px;
            background-color: #ddebd8;
            border: none;
        """)

        self.download_btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                padding: 10px 20px;
                background-color: #4caf50;
                color: white;
                border-radius: 5px;
                border: 2px solid transparent;
            }
            QPushButton:hover {
                background-color: #6fd66f;
            }
            QPushButton:pressed {
                border: 2px solid white;
                background-color: #45a049;
            }
        """)

        # FIXED DROPDOWN COLORS (Your previous bug fixed)
        self.quality_dropdown.setStyleSheet("""
            QComboBox {
                font-size: 20px;
                padding: 10px;
                border-radius: 5px;
                background-color: #ddebd8;
                border: none;
                min-width: 150px;
            }
            QComboBox:hover {
                background-color: #c9e3c3;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 8px solid #4caf50;
                margin-right: 10px;
            }
            QComboBox QAbstractItemView {
                background-color: #ddebd8;
                selection-background-color: #4caf50;
                selection-color: white;
                font-size: 18px;
                border: 1px solid #4caf50;
            }
        """)

    def clean_url(self, url):
        url = url.strip()

        # Handle youtu.be links (short links)
        if "youtu.be" in url:
            return url.split("?")[0]

        # Handle full YouTube links
        if "youtube.com" in url and "v=" in url:
            return url.split("&")[0]

        return url

    def download_video(self):
        url = self.clean_url(self.url_input.text())
        quality = self.quality_dropdown.currentText()

        print("Downloading:", url, "\nQuality:", quality)

        try:
            yt = YouTube(url)
            stream = yt.streams.filter(res=quality, progressive=True).first()

            if not stream:
                print("Selected quality not available!")
                return

            save_path = stream.download(output_path="G:/D DRIVE/Desktop/Pygrab/download")
            print("Download Complete!")
            print("Saved to:", save_path)

        except Exception as e:
            print("Error:", e)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
