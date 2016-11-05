
from Qt.QtTest import QTest
from Qt import QtWidgets
from unittest  import TestCase
import os


#QApp = QtWidgets.QApplication(sys.argv)



class TestButton( QtWidgets.QPushButton ):
    def __init__(self,*args,**kwds):
        super( TestButton, self ).__init__(*args,**kwds)
        self.clicked.connect( self.changetext )

    def changetext(self,event):
        self.setText( 'changed' )


class Test_Testing(TestCase):
    def test_testing(self):
        self.assertEqual( 42, 42 )

    def test_qtest(self):
        btn = QPushButton('nothing')
        QTest.mouseClick( btn, QtCore.Qt.LeftButton )
        self.assertEqual( btn.text(), 'changed')



