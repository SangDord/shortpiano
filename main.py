import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import Qt
from PianoWindow import Ui_MainWindow


def get_media(filename):
    media = QtCore.QUrl.fromLocalFile(filename)
    content = QtMultimedia.QMediaContent(media)
    return content


def key_play(player):
    if player.mediaStatus() == 6:
        player.stop()
        player.play()
    else:
        player.play()


class ShortPiano(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        current_dir = os.path.abspath(__file__)
        program_dir = os.path.dirname(current_dir)

        files = ['{}/data/keys/key{}.mp3'.format(program_dir, i) for i in range(1, 13)]

        self.key1 = QtMultimedia.QMediaPlayer()
        self.key1.setMedia(get_media(files[0]))

        self.key2 = QtMultimedia.QMediaPlayer()
        self.key2.setMedia(get_media(files[1]))

        self.key3 = QtMultimedia.QMediaPlayer()
        self.key3.setMedia(get_media(files[2]))

        self.key4 = QtMultimedia.QMediaPlayer()
        self.key4.setMedia(get_media(files[3]))

        self.key5 = QtMultimedia.QMediaPlayer()
        self.key5.setMedia(get_media(files[4]))

        self.key6 = QtMultimedia.QMediaPlayer()
        self.key6.setMedia(get_media(files[5]))

        self.key7 = QtMultimedia.QMediaPlayer()
        self.key7.setMedia(get_media(files[6]))

        self.key8 = QtMultimedia.QMediaPlayer()
        self.key8.setMedia(get_media(files[7]))

        self.key9 = QtMultimedia.QMediaPlayer()
        self.key9.setMedia(get_media(files[8]))

        self.key10 = QtMultimedia.QMediaPlayer()
        self.key10.setMedia(get_media(files[9]))

        self.key11 = QtMultimedia.QMediaPlayer()
        self.key11.setMedia(get_media(files[10]))

        self.key12 = QtMultimedia.QMediaPlayer()
        self.key12.setMedia(get_media(files[11]))

        for btn in self.pianokey.buttons():
            btn.clicked.connect(self.sound)

    def sound(self):
        if self.sender().text() == '1':
            key_play(self.key1)
        if self.sender().text() == '2':
            key_play(self.key2)
        if self.sender().text() == '3':
            key_play(self.key3)
        if self.sender().text() == '4':
            key_play(self.key4)
        if self.sender().text() == '5':
            key_play(self.key5)
        if self.sender().text() == '6':
            key_play(self.key6)
        if self.sender().text() == '7':
            key_play(self.key7)
        if self.sender().text() == '8':
            key_play(self.key8)
        if self.sender().text() == '9':
            key_play(self.key9)
        if self.sender().text() == '0':
            key_play(self.key10)
        if self.sender().text() == '-':
            key_play(self.key11)
        if self.sender().text() == '=':
            key_play(self.key12)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            key_play(self.key1)
        if event.key() == Qt.Key_2:
            key_play(self.key2)
        if event.key() == Qt.Key_3:
            key_play(self.key3)
        if event.key() == Qt.Key_4:
            key_play(self.key4)
        if event.key() == Qt.Key_5:
            key_play(self.key5)
        if event.key() == Qt.Key_6:
            key_play(self.key6)
        if event.key() == Qt.Key_7:
            key_play(self.key7)
        if event.key() == Qt.Key_8:
            key_play(self.key8)
        if event.key() == Qt.Key_9:
            key_play(self.key9)
        if event.key() == Qt.Key_0:
            key_play(self.key10)
        if event.key() == Qt.Key_Minus:
            key_play(self.key11)
        if event.key() == Qt.Key_Equal:
            key_play(self.key12)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShortPiano()
    ex.show()
    sys.exit(app.exec_())
