#!/bin/env python
# Author: Xin-Xin Ma (maxx@ihep.ac.cn)
# Date:   2019-08-30
import sys
import os

class mailHelper:
    def __init__(self):
        self._subject = "Not defined yet"
        #choose who can receive this release mail
        self._recLsit = []
        self._options = {}
        self._tmpbodyFile = "__TMPBODYFILE__"
        self._announce = "Announce"
        self._mailList = ".mailList"
        self._addOpt = ""
    def _getsubject(self):
        for line in open(self._announce).readlines():
            if not '=' in line:
                continue
            ll = line.split("=")
            if len(ll) < 2:
                continue
            if ll[0] == "subject":
                self._subject = ll[1].split("\n")[0]
                continue
            self._options[ll[0]] = ll[1]
    def _getBody(self):
        s = ''
        for line in open(self._announce).readlines():
            if line.strip() == "":
                continue
            # strip: to remove the blanck before the #
            if '#' == line.strip()[0]:
                continue
            #remove the line 
            # subject= status | project
            if 'subject' == line.split("=")[0].strip():
                continue
            s += line
        f = open(self._tmpbodyFile, 'w')
        f.write(s)
        f.close()

    def setOpt(self, opt):
        self._addOpt
    def setMailList(self, mailList=".mailList"):
        self._mailList = mailList

    def _getMailList(self):
        for line in open(self._mailList):
            self._recLsit.append(line)

    def _clear(self):
        os.system("rm -rf " + self._tmpbodyFile)
        self._subject = "Not defined yet"
        self._mailList = []

    def sendmail(self):
        self._getsubject()
        self._getBody()
        self._getMailList()
        command = "cat %s|"%(self._tmpbodyFile)
        command += "mutt "
        for mailadd in self._recLsit:
            command += mailadd.split('\n')[0] + " "
        command += "-s '%s' "%(self._subject)
        command += self._addOpt
        #print command
        os.system(command)
        self._clear()
INIT='''This is not a ReleaseSys, do you want create one?
If so, please use
   ReleaseSys init
'''
USEGE='''Options
  init :
  send : release the Announce to all email in .mailList or in ~/.mailList
         The default is ~/.mailList, if .mailList not exist
  -L mailListFile
'''
CREATEMM='''We will create ~/.mailList, ...
   You can change it
'''

class ReleaseHelper(mailHelper):
    def __init__(self):
        mailHelper.__init__(self)
        # check the system status
        # the file Announce and .mailList must be exist
        self._status = False
    def _checkStatue(self):
        if not os.path.isfile(self._announce):
            print(INIT)
            sys.exit()
        if not os.path.isfile(self._mailList):
            print(INIT)
            sys.exist()
        return
    def _init(self):
        f = open(self._announce, 'w')
        f.write('#Please set the subject as "statue | project"\n')
        f.write('#the "status" should be "Draft", "Publish", "Discuss", "Update", or others\n')
        f.write('#the project should be the name of the repository, or others"\n')
        f.write('subject= Not Defined yet\n')
        f.write('Put the E-mail content here\n')
        f.close()
        homemailFile =  os.path.expanduser("~/"+self._mailList)
        if not os.path.isfile(homemailFile):
            print(CREATEMM)
            f = open(homemailFile, 'w')
            f.write("sunhk@ihep.ac.cn\n")
            f.write("maxx@ihep.ac.cn\n")
            f.close()
        if not os.path.isfile(self._mailList):
            #print "copy ~/%s ."%(self._mailList)
            os.system("cp -rf ~/%s %s"%(self._mailList, self._mailList))
    def getAddOpt(self):
        addopt = ""
        for opt in sys.argv[1:]:
            if "-L" in opt or "send" in opt or  "init" in opt:
                aa = False
                continue
            if "-" == opt[0]:
                aa = True
                addopt += opt + ' '
                continue
            if aa:
                addopt += opt + ' '
        self._addOpt = addopt


    def run(self):
        if "init" in sys.argv:
            self._init()
            return
        if "send" in sys.argv:
            self._checkStatue()
            if "-L" in sys.argv:
                i = sys.argv.index("-L")
                self.setMailList(sys.argv[i+1])
            self.getAddOpt()
            self.sendmail()
            return
        if "-h" in sys.argv or "-help" in sys.argv:
            print(USEGE)
            return
        self._checkStatue()
        print(USEGE)
        return


