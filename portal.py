import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from PyQt4 import QtCore, QtGui

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.central_widget = QStackedWidget()
		self.setCentralWidget(self.central_widget)
		#first_window = FirstWindow(self)
		#self.central_widget.addWidget(first_window)
		self.widget = MyWidget()
		self.widget.setMouseTracking(True)
		self.setFixedSize(800, 700)
		self.setWindowTitle('Farmers Portal')
		self.menpage = MainPage(self)
		self.beed = BeedDistrict(self)
		self.pune = PuneDistrict(self)
		self.ahmednagar = AhmednagarDistrict(self)
		self.buldhana = BuldhanaDistrict(self)
		self.jalna = JalnaDistrict(self)
		self.nagpur = NagpurDistrict(self)
		self.aurangabad = AurangabadDistrict(self)
		self.thane = ThaneDistrict(self)
		self.ratnagiri = RatnagiriDistrict(self)
		self.raigad = RaigadDistrict(self)
		self.sindhudurg = SindhudurgDistrict(self)
		self.kolhapur = KolhapurDistrict(self)
		self.dhule = DhuleDistrict(self)
		self.jalgaon = JalgaonDistrict(self)
		self.nashik = NashikDistrict(self)
		self.nandurbar = NandurbarDistrict(self)
		self.bhandara = BhandaraDistrict(self)
		self.gondia = GondiaDistrict(self)
		self.latur = LaturDistrict(self)
		self.satara = SataraDistrict(self)
		self.sangli = SangliDistrict(self)
		self.solapur = SolapurDistrict(self)
		self.osmanabad = OsmanabadDistrict(self)	
		self.nanded = NandedDistrict(self)
		self.hingoli = HingoliDistrict(self)
		self.yewatmal = YewatmalDistrict(self)
		self.chandrapur = ChandrapurDistrict(self)
		self.gadchiroli = GadchiroliDistrict(self)
		self.parbhani = ParbhaniDistrict(self)
		self.washim = WashimDistrict(self)
		self.wardha = WardhaDistrict(self)
		self.amravti = AmravtiDistrict(self)
		self.akola = AkolaDistrict(self)
	
		self.central_widget.insertWidget(0, self.menpage)
		self.central_widget.insertWidget(34, self.widget)
		self.central_widget.insertWidget(1, self.beed)
		self.central_widget.insertWidget(2, self.pune)
		self.central_widget.insertWidget(3, self.ahmednagar)
		self.central_widget.insertWidget(4, self.buldhana)
		self.central_widget.insertWidget(5, self.jalna)
		self.central_widget.insertWidget(6, self.nagpur)
		self.central_widget.insertWidget(7, self.aurangabad)
		self.central_widget.insertWidget(8, self.thane)
		self.central_widget.insertWidget(9, self.ratnagiri)
		self.central_widget.insertWidget(10, self.raigad)
		self.central_widget.insertWidget(11, self.sindhudurg)
		self.central_widget.insertWidget(12, self.kolhapur)
		self.central_widget.insertWidget(13, self.dhule)
		self.central_widget.insertWidget(14, self.jalgaon)
		self.central_widget.insertWidget(15, self.nashik)
		self.central_widget.insertWidget(16, self.nandurbar)
		self.central_widget.insertWidget(17, self.bhandara)
		self.central_widget.insertWidget(18, self.gondia)
		self.central_widget.insertWidget(19, self.latur)
		self.central_widget.insertWidget(20, self.satara)
		self.central_widget.insertWidget(21, self.sangli)
		self.central_widget.insertWidget(22, self.solapur)
		self.central_widget.insertWidget(23, self.osmanabad)
		self.central_widget.insertWidget(24, self.nanded)
		self.central_widget.insertWidget(25, self.hingoli)
		self.central_widget.insertWidget(26, self.yewatmal)
		self.central_widget.insertWidget(27, self.chandrapur)
		self.central_widget.insertWidget(28, self.gadchiroli)
		self.central_widget.insertWidget(29, self.parbhani)
		self.central_widget.insertWidget(30, self.washim)
		self.central_widget.insertWidget(31, self.amravti)
		self.central_widget.insertWidget(32, self.akola)
		self.central_widget.insertWidget(33, self.wardha)
	
	def mouseReleaseEvent(self, event):
		if 1:
			x = event.pos().x()
			y = event.pos().y()
			if x > 0 and y > 0:
				if QToolTip.isVisible():
					self.widget.toolTipWidget.hide()
				c = QPixmap.grabWindow(self.widget.winId()).toImage().pixel(x, y)
				color = QColor(c).getRgb()[:-1]
				self.index = self.getIndex(color)
				if self.index > 0:
					self.central_widget.setCurrentIndex(self.index)
				#else :
				#	self.central_widget.setCurrentIndex(self.index)
	def getIndex(self, color):
		rgb = [(64, 224, 208),(60, 179, 113),(184, 134, 11),(255,105,180),(175, 238, 238),(205, 92, 92),(176, 224, 230),(49, 79, 79),(112, 138, 144),(105, 105, 105),(119, 136, 153),(107, 149, 35),(255, 215, 0),(238,  221, 130),(218, 165, 32),(255, 255, 0),(160, 82, 45),(205, 133, 63),(0, 255, 255),(50, 205, 50),(104, 205, 50),(34, 139, 34),(224, 255, 255),(0, 0, 200),(72, 209, 204),(219, 112, 147),(139, 69, 19),(222, 182, 135),(0, 206, 209),(255, 192, 203),(255, 20, 147),(255, 182, 193),(188, 143, 143)]
		for i in range(0, len(rgb)):
			if cmp(rgb[i], color) == 0:
				return i+1
		return 0

'''QSignalMapper mapper = new QSignalMapper(); // don't forget to set the proper parent
mapper->setMapping(firstPageWidget->button1, 2); // 2 can be replaced with any int value
connect(firstPageWidget->button1, SIGNAL(clicked()), mapper, SLOT(map()));
connect(mapper, SIGNAL(mapped(int)), stackWidget, SLOT(setCurrentIndex(int)));	
'''
class BeedDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Beed District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/1.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/rice.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		
class PuneDistrict(QWidget):
	def __init__(self,obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Pune District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/2.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/urad.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/urad.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		
class AhmednagarDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Ahmednagar District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/3.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/sorghum.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/bajra.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/sorghum.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/bajra.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class BuldhanaDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Buldhana District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/4.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/cotton.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/cotton.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))

class JalnaDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Jalna District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/5.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/cotton.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/cotton.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class NagpurDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Nagpur District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/6.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/wheat.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		
class AurangabadDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Aurangabad District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/7.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/sorghum.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/bajra.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/sorghum.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/bajra.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class ThaneDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Thane District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/8.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/brinjal.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/brinjal.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))

class RatnagiriDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Ratnagiri District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/9.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/mango.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/mango.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class RaigadDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Raigad District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/10.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/ragi.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/ragi.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class SindhudurgDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Sindhudurg District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/11.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/ragi.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/mango.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/ragi.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/mango.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class KolhapurDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Kolhapur District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/12.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/ragi.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/ragi.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		
class JalgaonDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Jalgaon District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/14.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/wheat.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class NashikDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Nashik District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/15.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/sorghum.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/sorghum.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		
class DhuleDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Dhule District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/13.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/bajra.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/bajra.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class NandurbarDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Nandurbar District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/16.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/sorghum.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/bajra.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/sorghum.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/bajra.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class BhandaraDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Bhandara District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/4.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/sorghum.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/cotton.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/sorghum.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/cotton.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class GondiaDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Gondia District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/18.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/rice.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class LaturDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Latur District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/19.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/sorghum.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/sorghum.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class SataraDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Satara District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/20.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/ragi.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/ragi.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()	
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class SangliDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Sangli District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/21.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/mango.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/mango.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		
class SolapurDistrict(QWidget):
	def __init__(self,obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Solapur District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/22.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/cotton.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/cotton.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class OsmanabadDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Osmanabad District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/23.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/rice.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class NandedDistrict(QWidget):
	def __init__(self,obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Nanded District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/24.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/rice.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class HingoliDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Hingoli District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/25.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/rice.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class YewatmalDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Yewatmal District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/26.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/rice.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/sorghum.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/sorghum.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class ChandrapurDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Chandrapur District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/27.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/bajra.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/cotton.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/bajra.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/cotton.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class GadchiroliDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Gadchiroli District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/28.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/cotton.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/cotton.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()	
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class ParbhaniDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Parbhani District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/29.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/sorghum.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/forghum.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()	
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class WashimDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Washim District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/30.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/bajra.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/cotton.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/bajra.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/cotton.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class WardhaDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Wardha District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/33.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/sorghum.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/bajra.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/sorghum.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/bajra.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
		
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class AmravtiDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Amravti District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/32.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/rice.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		hbox3.addStretch()
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class AkolaDistrict(QWidget):
	def __init__(self, obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Akola District')
		self.layout(obj)
		
	def layout(self, obj):
		fp = open("info/31.txt", "r")
		str = fp.read()
		text = QLabel(str)
		fp.close()
		fp = open("crops/wheat.txt")
		str1 = fp.read()
		text1 = QLabel(str1)
		fp.close()
		fp = open("crops/rice.txt")
		str2 = fp.read()
		text2 = QLabel(str2)
		fp.close()
		text.setAlignment(Qt.AlignLeft)
		l1 = QLabel()
		pixmap = QPixmap('crops/wheat.png')
		l1.setPixmap(pixmap)
		l2 = QLabel()
		pixmap = QPixmap('crops/rice.png')
		l2.setPixmap(pixmap)
		vbox = QVBoxLayout()
		
		hbox0 = QHBoxLayout()
		hbox0.addWidget(text)
	
		hbox1 = QHBoxLayout()
		hbox1.addStretch()
		hbox1.addWidget(l1)
		hbox1.addStretch()
		hbox1.addStretch()
	
		hbox2 = QHBoxLayout()
		hbox2.addWidget(text1)
		
		hbox3 = QHBoxLayout()
		
		hbox3.addWidget(l2)
		hbox3.addStretch()
		hbox3.addStretch()
		
		hbox4 = QHBoxLayout()
		hbox4.addWidget(text2)
		
		hbox5 = QHBoxLayout()
		Btn = QPushButton("Back")
		hbox5.addWidget(Btn)

		vbox.addLayout(hbox0)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		vbox.addLayout(hbox3)
		vbox.addLayout(hbox4)
		vbox.addLayout(hbox5)
		#self.setTabText(0,"Contact Details")
		self.setLayout(vbox)
		Btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))
		

class MainPage(QWidget):
	def __init__(self,obj, parent = None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		self.setWindowTitle('Welcome')
		vbox = QVBoxLayout()
		l2 = QLabel()
		pixmap = QPixmap('crops/images1.jpg')
		l2.setPixmap(pixmap)
		ButtonIcon = QIcon(pixmap)
		btn = QPushButton()
		#btn.setGeometry(0, 0, 800,900)
		btn.setIcon(ButtonIcon)
		#btn.setFixedSize(800, 900);
		#btn.setIconSize(QSize(800, 900));
		btn.setIconSize(pixmap.rect().size())
		vbox.addWidget(btn)
		self.setLayout(vbox)
		btn.clicked.connect(lambda : obj.central_widget.setCurrentIndex(34))

class MyWidget(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.resize(800, 900)
		#self.setWindowTitle("Farmer's Portal")
		toolTipWidget = QLabel()
		toolTipWidget.setFrameShape(QFrame.StyledPanel)
		toolTipWidget.setWindowFlags(Qt.ToolTip)
		toolTipWidget.setAttribute(Qt.WA_TransparentForMouseEvents)
		toolTipWidget.hide()
		self.toolTipWidget = toolTipWidget
		
	def mouseMoveEvent(self, event):
		x = event.pos().x()
		y = event.pos().y()
		if x > 0 and y > 0:
			c = QPixmap.grabWindow(self.winId()).toImage().pixel(x, y)
			color = QColor(c).getRgb()[:-1]
			text = self.DistrictName(color)
			if text == 0:
				self.toolTipWidget.hide()
			else:
				self.toolTipWidget.setText(text)
				self.toolTipWidget.move(event.globalPos() + QPoint(5, 5))
				self.toolTipWidget.adjustSize()
				self.toolTipWidget.show()
		else:
			self.toolTipWidget.hide()

	def DistrictName(self, color):
		Names = ['Beed', 'Pune', 'Ahmednagar', 'Buldhana', 'Jalna', 'Nagpur', 'Aurangabad', 'Thane', 'Ratnagiri', 'Raigad', 'Sindhudurg', 'Kolhapur', 'Dhule', 'Jalgaon', 'Nashik', 'Nandurbar', 'Bhandara', 'Gondia', 'Latur', 'Satara', 'Sangli', 'Solapur', 'Osmanabad', 'Nanded', 'Hingoli', 'Yewetmal', 'Chandrapur', 'Gadchiroli', 'Parbhani', 'Washim', 'Akola', 'Amravati', 'Wardha']
		rgb = [(64, 224, 208),(60, 179, 113),(184, 134, 11),(255,105,180),(175, 238, 238),(205, 92, 92),(176, 224, 230),(49, 79, 79),(112, 138, 144),(105, 105, 105),(119, 136, 153),(107, 149, 35),(255, 215, 0),(238,  221, 130),(218, 165, 32),(255, 255, 0),(160, 82, 45),(205, 133, 63),(0, 255, 255),(50, 205, 50),(104, 205, 50),(34, 139, 34),(224, 255, 255),(0, 0, 200),(72, 209, 204),(219, 112, 147),(139, 69, 19),(222, 182, 135),(0, 206, 209),(255, 192, 203),(255, 20, 147),(255, 182, 193),(188, 143, 143)]
		if cmp((242, 241, 240), color) == 0:
			return 0
		for i in range(0, len(rgb)):
			if cmp(rgb[i], color) == 0:
				return Names[i]
		return 0

	def drawregion(self, clist, color):
		painter = QPainter(self)
		coordinates = []
		for i in range(0, len(clist), 2):
			coordinates.append(QPointF(clist[i], clist[i + 1]))
		polygon = QPolygonF(coordinates)
		painter.setPen(Qt.black)
		painter.setBrush(color)
		painter.drawPolygon(polygon)
		return polygon
	
	def paintEvent(self, event):
		Beed = [359, 318, 338, 313, 319, 309, 306, 307, 298, 308, 281, 296, 261, 306, 229, 283, 240, 279, 241, 270, 260, 273, 278, 270, 291, 270, 282, 260, 294, 246, 302, 243, 325, 245, 329, 251, 354, 254, 364, 258, 364, 272, 375, 271, 383, 283, 396, 298, 398, 304, 386, 308]
		self.polygon0 = self.drawregion(Beed, QColor(64, 224, 208))
		
		Pune = [109, 329, 99, 299, 117, 271, 136, 244, 182, 259, 178, 281, 201, 316, 254, 356, 254, 376, 153, 351, 140, 365, 126, 363]
		self.polygon1 = self.drawregion(Pune, QColor(60, 179, 113))
		
		Ahmednagar = [123,227 ,136,224, 146,213,159,220,168,221,182,211,190,209,180,195,199,191,218,197,212,209,224,211,230,222,248,224,266,226,277,233,276,241,288,241,294,251,284,259,288,271,278,271,272,273,274,281,267,277,258,277,250,273,254,266,240,270,240,279,229,283,246,294,256,307,265,305,274,301,282,295,292,303,292,309,282,317,274,319,262,321,254,323,244,329,229,337,222,329,220,325,212,329,206,325,202,314,198,301,188,294,172,276,183,262,166,258,160,249,149,249,134,247,127,239,130,234]
		polygon2 = self.drawregion(Ahmednagar, QColor(184, 134, 11))
		
		Buldhana = [397, 79, 384, 86, 376, 86, 367, 104, 347, 100, 334, 127, 338, 137, 330, 143, 329, 163, 344, 161, 352, 167, 331, 189, 343, 204, 375, 199, 384, 205, 389, 202, 393, 186, 390, 186, 408, 164, 397, 159, 396, 146, 401, 130, 399, 112, 405, 101]
		polygon3 = self.drawregion(Buldhana, QColor(255, 105, 180))
		Jalna = [326, 247, 314, 243, 302, 246, 301, 223, 304, 207, 306, 197, 298, 188, 307, 169, 314, 157, 325, 143, 329, 141, 329, 163, 342, 160, 352, 169, 330, 192, 345, 205, 372, 198, 380, 204, 372, 231, 360, 245, 354, 254, 337, 254, 337, 250, 328, 253]
		polygon5 = self.drawregion(Jalna, QColor(175, 238, 238))
		
		Nagpur = [623, 39, 604, 49, 592, 49, 593, 61, 562, 59, 552, 59, 530, 73, 562, 93, 590, 116, 621, 140, 635, 129, 644, 128, 649, 116, 657, 103, 644, 93, 644, 87, 654, 75, 636, 62, 646, 50, 644, 45, 626, 41]
		polygon4 = self.drawregion(Nagpur, QColor(205, 92, 92))
			
		Aurangabad = [207,209,221,183,218,172,228,170,241,178,236,167,245,161,256,159,260,149,274,137,282,145,295,138,307,133,314,138,318,138,328,141,336,135,338,143,330,146,322,146,310,153,314,159,308,164,304,175,298,188,306,196,302,211,298,224,303,227,299,246,284,243,276,241,271,235,262,227,250,227,236,224,228,219,217,215,211,212]
		polygon6 = self.drawregion(Aurangabad, QColor(176, 224, 230))
	
		Thane = [45, 239, 56, 249, 55, 257, 66, 264, 70, 275, 80, 262, 105, 265, 116, 268, 125, 261, 140, 244, 122, 222, 112, 209, 107, 198, 109, 193, 93, 179, 88, 185, 71, 185, 65, 174, 56, 171, 47, 186, 41, 204]
		polygon7 = self.drawregion(Thane, QColor(49, 79, 79))
		
		Ratnagiri = [73, 367, 91, 360, 129, 397, 132, 424, 135, 468, 144, 486, 99, 501, 98, 467]
		polygon8 = self.drawregion(Ratnagiri, QColor(112, 138, 144))
		
		Raigad = [63, 324, 57, 300, 63, 289, 74, 271, 80, 265, 99, 263, 115, 269, 112, 288, 105, 289, 109, 285, 105, 284, 105, 288, 98, 299, 100, 304, 100, 312, 101, 321, 104, 331, 100, 314, 97, 295, 100, 321, 126, 361, 112, 378, 90, 357, 73, 364]
		polygon9 = self.drawregion(Raigad, QColor(105, 105, 105))
		
		Sindhudurg = [125, 568, 98, 501, 140, 486, 146, 517, 162, 542, 168, 547, 164, 547, 162, 557, 169, 563, 172, 565, 170, 573, 157, 579, 146, 560]
		polygon10 = self.drawregion(Sindhudurg, QColor(119, 136, 153))
		
		Kolhapur = [138, 442, 219, 479, 212, 493, 200, 489, 183, 497, 186, 517, 200, 525, 197, 538, 186, 564, 170, 568, 138, 488]
		polygon11 = self.drawregion(Kolhapur, QColor(107, 149, 35))
		
		Dhule = [228, 51, 225, 62, 207, 63, 202, 73, 202, 80, 180, 80, 166, 89, 157, 93, 151, 100, 147, 100, 152, 116, 195, 118, 214, 118, 216, 130, 232, 135, 243, 129, 243, 112, 236, 98, 235, 96, 243, 84, 253, 84, 260, 66, 251, 54, 235, 48]
		polygon12 = self.drawregion(Dhule, QColor(255, 215, 0))
		
		Jalgaon = [338, 72, 263, 67, 255, 83, 242, 87, 235, 97, 245, 123, 234, 134, 228, 145, 237, 170, 253, 160, 270, 141, 280, 137, 280, 143, 293, 140, 304, 133, 318, 140, 326, 140, 335, 136, 334, 124, 350, 100, 364, 106, 370, 97, 351, 94, 344, 88, 350, 85, 341, 72]
		polygon13 = self.drawregion(Jalgaon, QColor(238,  221, 130))
		
		Nashik = [109, 129, 125, 136, 133, 140, 148, 131, 154, 117, 157, 116, 196, 116, 212, 118, 217, 130, 231, 135, 229, 145, 239, 167, 238, 176, 231, 171, 224, 175, 221, 191, 183, 193, 194, 206, 171, 219, 153, 219, 144, 211, 140, 222, 126, 226, 108, 202, 110, 191, 91, 181, 97, 172, 107, 174, 107, 157, 111, 145]
		polygon14 = self.drawregion(Nashik, QColor(218, 165, 32))
		
		Nandurbar = [120, 91, 141, 87, 148, 78, 157, 67, 178, 60, 188, 56, 177, 53, 144, 57, 140, 45, 143, 33, 139, 28, 169, 19, 182, 19, 193, 13, 207, 21, 203, 37, 217, 46, 230, 50, 224, 63, 206, 67, 202, 79, 176, 81, 161, 92, 147, 102]
		polygon15 = self.drawregion(Nandurbar, QColor(255, 255, 0))
		
		Bhandara = [679, 59, 666, 48, 645, 55, 639, 62, 654, 74, 643, 91, 659, 104, 644, 128, 670, 129, 683, 129, 675, 116, 683, 106, 695, 104, 696, 91, 688, 80, 672, 84, 672, 68]
		polygon16 = self.drawregion(Bhandara, QColor(160, 82, 45))
		
		Gondia = [745, 75, 727, 92, 725, 101, 729, 110, 735, 117, 716, 119, 710, 134, 686, 130, 676, 116, 684, 105, 695, 101, 696, 90, 689, 82, 676, 82, 672, 66, 682, 52, 695, 52, 706, 47, 719, 52, 722, 64, 724, 70]
		polygon17 = self.drawregion(Gondia, QColor(205, 133, 63))
		
		Latur = [422, 352, 416, 356, 413, 376, 402, 379, 388, 365, 362, 359, 363, 334, 352, 332, 359, 317, 396, 305, 399, 296, 421, 293, 428, 302, 426, 306, 438, 308, 447, 319, 445, 327, 437, 346, 431, 353]
		polygon18 = self.drawregion(Latur, QColor(0, 255, 255))
		
		#Greater Bombay = [120, 91, 141, 87, 148, 78, 157, 67, 178, 60, 188, 56, 177, 53, 144, 57, 140, 45, 143, 33, 139, 28, 169, 19, 182, 19, 193, 13, 207, 21, 203, 37, 217, 46, 230, 50, 224, 63, 206, 67, 202, 79, 176, 81, 161, 92, 147, 102]
		#polygon19 = self.drawregion(Greater Bombay, QColor(0, 125, 0))
		
		Satara = [171, 444, 179, 442, 180, 440, 181, 428, 183, 435, 179, 420, 204, 417, 220, 416, 236, 405, 215, 416, 177, 424, 182, 424, 178, 421, 203, 420, 227, 414, 240, 400, 212, 383, 215, 364, 155, 351, 150, 362, 130, 364, 118, 376, 132, 396, 129, 424, 159, 446, 167, 445, 175, 441]
		polygon20 = self.drawregion(Satara, QColor(50, 205, 50))
		
		Sangli = [226, 410, 237, 401, 249, 418, 233, 440, 265, 433, 299, 430, 305, 455, 284, 457, 262, 467, 244, 459, 243, 467, 221, 480, 138, 444, 144, 438, 171, 445, 182, 435, 180, 422]
		polygon21 = self.drawregion(Sangli, QColor(104, 205, 50))
		
		Solapur = [252, 325, 270, 318, 272, 331, 284, 348, 292, 355, 306, 341, 312, 330, 325, 336, 333, 354, 335, 363, 333, 368, 322, 368, 327, 378, 348, 392, 370, 395, 368, 403, 368, 426, 339, 425, 323, 422, 311, 420, 305, 414, 300, 425, 265, 434, 235, 438, 249, 416, 237, 400, 220, 383, 215, 367, 249, 374, 256, 374, 256, 356, 235, 344, 227, 341]
		polygon22 = self.drawregion(Solapur, QColor(34, 139, 34))
		
		Osmanabad = [389, 367, 367, 361, 360, 358, 362, 336, 354, 331, 358, 318, 299, 307, 280, 319, 272, 327, 292, 356, 309, 331, 327, 338, 337, 364, 323, 367, 329, 380, 343, 389, 372, 399, 382, 391, 391, 390, 393, 395, 403, 380, 394, 375]
		polygon23 = self.drawregion(Osmanabad, QColor(224, 255, 255))
		
		Nanded = [461, 220, 463, 242, 447, 249, 439, 258, 439, 269, 431, 273, 415, 286, 424, 295, 430, 307, 444, 315, 447, 329, 456, 332, 455, 342, 468, 346, 473, 320, 487, 318, 488, 307, 498, 294, 506, 293, 490, 276, 502, 250, 509, 251, 521, 257, 528, 253, 530, 242, 539, 230, 535, 217, 542, 208, 536, 202, 511, 199, 499, 209, 505, 214, 527, 222, 521, 232, 510, 238, 501, 235, 484, 239, 489, 233]
		polygon25 = self.drawregion(Nanded, QColor(0, 0, 200))
		
		Hingoli = [422, 191, 400, 200, 388, 200, 385, 206, 407, 219, 416, 226, 411, 235, 416, 244, 414, 252, 427, 259, 431, 274, 441, 266, 441, 254, 462, 243, 463, 225, 460, 213, 450, 199, 441, 196, 431, 195]
		polygon26 = self.drawregion(Hingoli, QColor(72, 209, 204))
		
		Yewetmal = [451, 200, 454, 184, 467, 183, 476, 189, 482, 169, 475, 158, 481, 142, 499, 139, 517, 134, 531, 130, 533, 142, 555, 145, 557, 151, 569, 155, 576, 166, 584, 169, 596, 173, 598, 181, 612, 197, 595, 211, 587, 212, 559, 207, 546, 203, 525, 199, 506, 199, 500, 208, 512, 219, 528, 226, 515, 240, 500, 234, 488, 238, 490, 232, 463, 222]
		polygon27 = self.drawregion(Yewetmal, QColor(219, 112, 147))
		
		Chandrapur = [618, 141, 610, 150, 593, 152, 584, 155, 578, 164, 597, 176, 609, 196, 599, 209, 587, 213, 589, 220, 596, 231, 620, 238, 621, 225, 640, 237, 666, 224, 665, 205, 666, 194, 674, 190, 680, 191, 681, 182, 683, 169, 681, 132, 659, 131, 631, 131]
		polygon28 = self.drawregion(Chandrapur, QColor(139, 69, 19))
		
		Gadchiroli = [735, 118, 716, 119, 709, 132, 684, 130, 682, 177, 682, 188, 672, 192, 666, 203, 668, 227, 682, 239, 685, 247, 682, 266, 674, 276, 682, 279, 683, 295, 681, 299, 705, 308, 717, 293, 712, 281, 720, 260, 736, 247, 748, 253, 760, 247, 760, 242, 769, 235, 745, 226, 749, 219, 730, 207, 722, 201, 727, 196, 734, 195, 735, 179, 724, 179, 721, 169, 738, 163, 740, 141, 730, 142, 731, 134, 737, 128]
		polygon29 = self.drawregion(Gadchiroli, QColor(222, 182, 135))
		
		Parbhani = [381, 205, 400, 216, 417, 225, 412, 237, 413, 250, 430, 263, 430, 274, 423, 292, 401, 297, 381, 283, 365, 263, 356, 251, 373, 227]
		polygon30 = self.drawregion(Parbhani, QColor(0, 206, 209))
		
		Washim = [436, 155, 446, 150, 455, 146, 457, 141, 475, 126, 481, 146, 476, 160, 481, 171, 478, 188, 455, 184, 454, 199, 429, 191, 388, 202, 394, 185, 400, 177, 409, 166, 426, 152]
		polygon31 = self.drawregion(Washim, QColor(255, 192, 203))
		
		Akola = [438, 83, 401, 86, 404, 109, 401, 132, 399, 158, 411, 164, 426, 152, 457, 148, 451, 141, 475, 125, 472, 114, 437, 116, 438, 86]
		polygon32 = self.drawregion(Akola, QColor(255, 20, 147))
		
		Amravati = [442, 35, 419, 45, 404, 51, 399, 63, 390, 75, 397, 80, 405, 85, 436, 84, 436, 116, 471, 116, 475, 130, 482, 143, 507, 138, 533, 130, 539, 123, 525, 109, 517, 72, 531, 72, 549, 66, 547, 50, 502, 67, 468, 70, 460, 54, 474, 54, 467, 37]
		polygon33 = self.drawregion(Amravati, QColor(255, 182, 193))
		
		Wardha = [608, 131, 545, 80, 529, 73, 516, 72, 519, 91, 524, 108, 537, 123, 532, 134, 532, 142, 555, 148, 571, 158, 580, 164, 590, 153, 612, 151, 618, 138, 604, 127, 588, 116, 584, 114]
		polygon34 = self.drawregion(Wardha, QColor(188, 143, 143))
		
		

if __name__ == '__main__':
	app = QApplication([]) 
	window = MainWindow()
	window.show()
	app.exec_()
