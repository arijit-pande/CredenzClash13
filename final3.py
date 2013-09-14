#client file to be run through cmd/terminal with 3 command line arguments-server ip,server port number and
#set number

import sys,os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import math
import sys
import sqlite3
import socket
import respage2,login_3,cl134

answer=0

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class myclass(QtGui.QWidget):
    total_questions=30	
    score=0
    index=0
    count=-1
    questions=[]
    timer_val=1200
    skips=3
    name=""
    credcode=""
    Number=0
    host=sys.argv[1]
    port=int(sys.argv[2])        
    import sqlite3
    timer=QtCore.QTimer()

    def update_skip(self):
        print self.index
        if self.skips==0:
                #self.ui2.pushButton_2.setEnabled(False)
                return
        else:
                self.skips=self.skips-1
                self.ui2.lcdNumber_3.display(self.skips)
                if self.skips==0:		
                        self.ui2.pushButton_2.setEnabled(False)
                self.total_questions=self.total_questions+1
                #self.index=self.index+1
                if(self.index < self.total_questions):	
                        self.index=self.index+1

                #self.total_questions=self.total_questions-1
                self.ui2.radioButton.setAutoExclusive(0)	
                self.ui2.radioButton.setChecked(0)	
                self.ui2.radioButton_2.setAutoExclusive(0)	
                self.ui2.radioButton_2.setChecked(0)
                self.ui2.radioButton_3.setAutoExclusive(0)	
                self.ui2.radioButton_3.setChecked(0)
                self.ui2.radioButton_4.setAutoExclusive(0)
                self.ui2.radioButton_4.setChecked(0)	
                #self.ui2.textEdit.setText(self.questions[self.index][0])
                self.show_question()		
		'''self.show_question(1)
		self.show_question(2)
		self.show_question(3)
		self.show_question(4)
		#self.show_question(5)'''
		self.ui2.textEdit_2.setText(self.questions[self.index][1])
                self.ui2.textEdit_3.setText(self.questions[self.index][2])
                self.ui2.textEdit_4.setText(self.questions[self.index][3])
                self.ui2.textEdit_5.setText(self.questions[self.index][4])
                self.ui2.radioButton.setAutoExclusive(1)
                self.ui2.radioButton_2.setAutoExclusive(1)	
                self.ui2.radioButton_3.setAutoExclusive(1)	
                self.ui2.radioButton_4.setAutoExclusive(1)

    def update_score(self):			
        if self.ui2.radioButton.isChecked()==0 and self.ui2.radioButton_2.isChecked()==0 and self.ui2.radioButton_3.isChecked()==0 and self.ui2.radioButton_4.isChecked()==0:
                return ;
        else:
                print self.index
		#self.ui2.pushButton_3.clicked.connect(self.show_res_page)
                self.count=self.count+1
                #print self.count
                if self.ui2.radioButton.isChecked()==1:
                        answer='1'
                elif self.ui2.radioButton_2.isChecked()==1:
                        answer='2'
                elif self.ui2.radioButton_3.isChecked()==1:
                        answer='3'
                elif self.ui2.radioButton_4.isChecked()==1:
                        answer='4'
                #print self.questions[self.index][5],answer,self.index	
        if answer==self.questions[self.index][5]:		
                self.score=self.score+4
                if self.count==0 :		
                        self.ui2.L1.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==1 :		
                        self.ui2.L2.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==2 :		
                        self.ui2.L3.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==3 :		
                        self.ui2.L4.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==4 :		
                        self.ui2.L5.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==5 :		
                        self.ui2.L6.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==6 :		
                        self.ui2.L7.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==7 :		
                        self.ui2.L8.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==8 :		
                        self.ui2.L9.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==9 :		
                        self.ui2.L10.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==10 :		
                        self.ui2.L11.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==11 :		
                        self.ui2.L12.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==12 :		
                        self.ui2.L13.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==13 :		
                        self.ui2.L14.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==14:		
                        self.ui2.L15.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==15 :		
                        self.ui2.L16.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==16 :		
                        self.ui2.L17.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==17 :		
                        self.ui2.L18.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==18 :		
                        self.ui2.L19.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==19 :		
                        self.ui2.L20.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==20 :		
                        self.ui2.L21.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==21:		
                        self.ui2.L22.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==22 :		
                        self.ui2.L23.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==23 :		
                        self.ui2.L24.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==24 :		
                        self.ui2.L25.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==25 :		
                        self.ui2.L26.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==26 :		
                        self.ui2.L27.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==27 :		
                        self.ui2.L28.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==28 :		
                        self.ui2.L29.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
                if self.count==29 :		
                        self.ui2.L30.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))	
        
        else:
                #print self.questions[self.index][5],answer,self.index
                self.score=self.score-2
                if self.count==0 :		
                        self.ui2.L1.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==1 :		
                        self.ui2.L2.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==2 :		
                        self.ui2.L3.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==3 :		
                        self.ui2.L4.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==4 :		
                        self.ui2.L5.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==5 :		
                        self.ui2.L6.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==6 :		
                        self.ui2.L7.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==7 :		
                        self.ui2.L8.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==8 :		
                        self.ui2.L9.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==9 :		
                        self.ui2.L10.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==10 :		
                        self.ui2.L11.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==11 :		
                        self.ui2.L12.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==12 :		
                        self.ui2.L13.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==13 :		
                        self.ui2.L14.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==14:		
                        self.ui2.L15.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==15 :		
                        self.ui2.L16.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==16 :		
                        self.ui2.L17.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==17 :		
                        self.ui2.L18.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==18 :		
                        self.ui2.L19.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==19 :		
                        self.ui2.L20.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==20 :		
                        self.ui2.L21.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==21:		
                        self.ui2.L22.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==22 :		
                        self.ui2.L23.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==23 :		
                        self.ui2.L24.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==24 :		
                        self.ui2.L25.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==25 :		 	
                        self.ui2.L26.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==26 :		
                        self.ui2.L27.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==27 :		
                        self.ui2.L28.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==28 :		
                        self.ui2.L29.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
                if self.count==29 :		
                        self.ui2.L30.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))	
        

        self.ui2.lcdNumber.display(self.score)		
        if(self.index < (self.total_questions-1)):	
                self.index=self.index+1
        else:
                self.ui2.pushButton.setEnabled(False)
                self.ui2.pushButton_2.setEnabled(False)
                self.ui2.pushButton_3.setEnabled(True)
                self.show_res_page(1)
#Since all questions have been answered. The page should automatically show up.
#QtGui.QMessageBox.about(self,'Info','You have answered all questions. Press End Button to terminate')
                return;
        self.ui2.radioButton.setAutoExclusive(0)	
        self.ui2.radioButton.setChecked(0)	
        self.ui2.radioButton_2.setAutoExclusive(0)	
        self.ui2.radioButton_2.setChecked(0)
        self.ui2.radioButton_3.setAutoExclusive(0)	
        self.ui2.radioButton_3.setChecked(0)
        self.ui2.radioButton_4.setAutoExclusive(0)
        self.ui2.radioButton_4.setChecked(0)	
        self.show_question()	
        self.ui2.textEdit_2.setText(self.questions[self.index][1])
        self.ui2.textEdit_3.setText(self.questions[self.index][2])
        self.ui2.textEdit_4.setText(self.questions[self.index][3])
        self.ui2.textEdit_5.setText(self.questions[self.index][4])
        self.ui2.radioButton.setAutoExclusive(1)
        self.ui2.radioButton_2.setAutoExclusive(1)	
        self.ui2.radioButton_3.setAutoExclusive(1)	
        self.ui2.radioButton_4.setAutoExclusive(1)	
 
    def show_login (self):
        self.mainWindow=QtGui.QWidget()
        self.Form1=QtGui.QWidget()
        self.Form2=QtGui.QWidget()
        self.ui=login_3.Ui_Form()
        self.ui.setupUi(self.Form1)
        self.Form1.showFullScreen()
        self.ui.lineEdit_3.setMaxLength(10)
        self.ui.pushButton.clicked.connect(self.next_page)
        
        #self.s1.send(self.credcode)
    def show_res_page_2(self):
        self.mainWindow.hide()
        self.tick=1
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ui3=respage2.Ui_Form()
        self.ui3.setupUi(self.Form2)
        self.Form2.show()
        self.ui3.lcdNumber.display(self.score)
        self.mainstring=str(self.Category)+self.credcode+'+'+self.name+'+'+self.phone+'+'+ str(self.score)+ '+' +str(self.tick)
	print "user-name:",self.name
	print "score:",self.score
	print "timeleft:",self.timer_val
        try:        
                self.s.connect((self.host,self.port))        	        	
                print "connecting to:",self.host,self.port
                #self.s.send("Connection incoming...")
                #print self.mainstring,len(self.mainstring)		
                self.s.send(self.mainstring) 	
                self.s.close()
                self.ui3.label_3.setText('Your score has been uploaded.Thank you for being a part of Clash')	
                #self.ui2.timer2.stop()
        except:	        
                print self.mainstring        
                self.ui3=respage2.Ui_Form()
                self.ui3.setupUi(self.Form2)
                self.Form2.showFullScreen()
                #self.ui3.label_3.setText('Your score has not been uploaded. Report to the nearest volunteer')
                self.ui3.lcdNumber.display(self.score)                
                #self.ui2.timer2.stop()
                
    def show_res_page(self, autoend = 0):
        print 'Value of autoend : ',autoend   
        if autoend!=1:
                print self.total_questions,"Quiz is being terminated."
                text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter "FINISH" (No Quotes) to Finish Clash Round 1 :')
                if ok:
                        if str(text).lower()!="finish":
                                return
                else:
                        return;
	print "user-name:",self.name
	print "score:",self.score
	print "timeleft:",self.timer_val        
	self.mainWindow.hide()
        self.tick=1
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ui3=respage2.Ui_Form()
        self.ui3.setupUi(self.Form2)
        self.Form2.show()
        self.ui3.lcdNumber.display(self.score)
        self.mainstring=str(self.Category)+self.credcode+'+'+self.name+'+'+self.phone+'+'+ str(self.score)+ '+' +str(self.tick)
        try:        
                self.s.connect((self.host,self.port))        	        	
                print "connecting to:",self.host,self.port
                #self.s.send("Connection incoming...")
                #print self.mainstring,len(self.mainstring)		
                self.s.send(self.mainstring) 	
                self.s.close()
                self.ui3.label_3.setText('Your score has been uploaded.Thank you for being a part of Clash')	
                #self.ui2.timer2.stop()
        except:	        
                print self.mainstring        
                self.ui3=respage2.Ui_Form()
                self.ui3.setupUi(self.Form2)
                self.Form2.showFullScreen()
                #self.ui3.label_3.setText('Your score has not been uploaded. Report to the nearest volunteer')
                self.ui3.lcdNumber.display(self.score)                
                #self.ui2.timer2.stop()
        
    def next_page(self):
        self.name=str(self.ui.lineEdit.text())
        self.credcode=str(self.ui.lineEdit_2.text())
        self.phone=str(self.ui.lineEdit_3.text())
        print self.name,self.credcode,self.phone
        l=len(self.name)
        number = str(self.ui.lineEdit_3.text())
        self.ui.lineEdit_3.setMaxLength(10)
        import random,string	
        try:
           numberx = int(number)
        except Exception:
                QtGui.QMessageBox.about(self, 'Error','Invalid phone number. Please Re-Enter.')
                return;
        if len(number)<10:
                QtGui.QMessageBox.about(self, 'Error','Invalid phone number. Please Re-Enter.')
                return;
	if self.credcode=='':
                QtGui.QMessageBox.about(self, 'Error','Blank CredCode!!')
                return;        
	if self.name=='':
                QtGui.QMessageBox.about(self,'Error','Empty names are not allowed.')
                return;
        else:    
                for i in range(0,l):
                        if self.name[i].isalpha()==False and self.name[i]!=' ':
                                QtGui.QMessageBox.about(self,'Error','Name contains invalid characters.')
                                return;    	
        if self.ui.radioButton.isChecked()==0 and self.ui.radioButton_2.isChecked()==0:
                        QtGui.QMessageBox.about(self,'Error','Please select your level (Junior or Senior)')
                        return
        QuestionDatabase = sqlite3.connect('DB.db')
        Database_Cursor = QuestionDatabase.cursor()
        global setnumber
        if self.ui.radioButton.isChecked()==1:	
            if(setnumber>5 or setnumber<0):
                exit
            self.Number=setnumber
            self.Category=0
        if self.ui.radioButton_2.isChecked()==1:
                self.Number=setnumber
                if setnumber<11 or setnumber>13:
                    exit
                self.Category=1
        '''self.s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s1.connect((self.host,self.port))
        self.s1.send('$'+str(credcode)+'$')
        self.s1.close()'''	

        self.TableName='TABLE'+str(self.Number)
        self.questions = Database_Cursor.execute("SELECT * from "+self.TableName+";");
        self.questions = self.questions.fetchall()
                        
        self.Form1.hide()
        self.ui2=cl134.Ui_Form()
        self.ui2.setupUi(self.mainWindow)
        self.mainWindow.showFullScreen()
        self.ui2.lcdNumber.display(self.score)
        self.ui2.lcdNumber_2.display(1200)
        self.timer.start(1000)
        self.ui2.lcdNumber_3.display(self.skips)
        self.timer.timeout.connect(self.update_timer)
        self.show_question()	
        self.ui2.textEdit_2.setText(self.questions[0][1])
        self.ui2.textEdit_3.setText(self.questions[0][2])
        self.ui2.textEdit_4.setText(self.questions[0][3])
        self.ui2.textEdit_5.setText(self.questions[0][4])
        self.ui2.radioButton.setChecked(False)
        self.ui2.radioButton_2.setChecked(False)
        self.ui2.radioButton_3.setChecked(False)
        self.ui2.radioButton_4.setChecked(False)		
        self.ui2.pushButton_3.clicked.connect(self.show_res_page)        
        self.ui2.pushButton.clicked.connect(self.update_score)
        self.ui2.pushButton_2.clicked.connect(self.update_skip)
        
    def update_timer(self):
        self.timer_val=self.timer_val-1
        self.ui2.lcdNumber_2.display(self.timer_val)
        if(self.timer_val<=0):
                self.timer.stop()
                self.show_res_page_2()

        
    def show_question(self):  
        QuestionParts=self.questions[self.index][0]  
        self.ui2.textEdit.setText("")
        x=list(QuestionParts)
        
        limit=len(x)
        escaped=['\n', '\x07', '\x08', '\r', '\t', '\x0b']
        unescaped=['n', 'a', 'b', 'r', 't', 'v']


        for i in range(0,limit):
            try:
                if x[i]=='\\':
                    if x[i] != '\\':
                        del x[i]
                        limit-=1

                        
                    if x[i] in escaped:
                        print "Escape Character : ",repr(escaped[i])
                        pass
                    elif x[i] in unescaped:
                        x[i]=escaped[unescaped.index(x[i])]
            except IndexError:
                pass

        
        left=0
        foobar=''
        flag=0

        i=0
        while i < len(x):
  #          print i
          
            if x[i]=='"':
                foobar+=x[i]
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=0
                i+=1
          
            try:
                if flag==1:
                    if x[i] in escaped:              
                        foobar+='\\'
                        
                        if x[i]=='\x07': #for a
                            foobar+='a'
                        elif x[i]=='\x08': #for b
                            foobar+='b'
                        elif x[i]=='x0b': #for v
                            foobar+='v'                    
                        elif x[i]=='\n':
                            foobar+='n'
                        elif x[i]=='\t':
                            foobar+='t'
                        elif x[i]=='\r':
                            foobar+='r'
                    
         #               print "Appending Character  : ",repr(x[i])," At Index :",i
                        i+=1
                    
                        
                    else:#flag==1
                        foobar+=x[i]
                        i+=1
        
            #Flag !=1 for the following 
                else:
                    if x[i]=='\n':
                        self.ui2.textEdit.append(foobar)
                        foobar=''
                        i+=1
                    else:    
                        foobar+=x[i]
                        i+=1
                        #if 1<0:
            except IndexError:
                pass
        #if(indicator==0):
        self.ui2.textEdit.append(foobar)      
        return

if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    if len(sys.argv)<4:
        print "usage: python final.py <ip of server> <port number> <number>"	
        exit()
    global setnumber
    setnumber = int(sys.argv[3])
    if(setnumber<1 or (setnumber<11 and setnumber>6) or setnumber>14):
        print 'Invalid Setnumber!.'
        sys.exit()
    print "setnumber:",setnumber
    x=myclass()
    x.show_login()
    sys.exit(app.exec_())
