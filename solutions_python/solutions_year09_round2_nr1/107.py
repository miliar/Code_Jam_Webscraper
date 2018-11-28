#!/usr/bin/python
import sys
import copy
import math

##szfile = './test.txt'
##szfile_output = './test.output.txt'
##szfile = './A-small-attempt0.in'
##szfile_output = './A-small.output.txt'
szfile = './A-large.in'
szfile_output = './A-large.output.txt'

class GCJ:
    def __init__(self):
        pass

    def RunFile(self) :
# using file set
        f = open(szfile,'rb')
        fw = open(szfile_output,'wb')
# ---
        szline = f.readline()
        ncase = int(szline)
        l_output = []
        for i in xrange(0, ncase):
            l_syntex = []
            l_input = []
            szline = f.readline()
            nsyntex = int(szline)
            for j in xrange(nsyntex):
                l_syntex.append(f.readline())
            szline = f.readline()
            ninput = int(szline)
            for j in xrange(ninput):
                l_input.append(f.readline())

            l_val = self.GetProb(l_syntex, l_input)
            num = i+1
            l_output.append('Case #%(num)d: '%locals())
            for v in l_val:
                l_output.append('%.8f' % v)
        print '\n'.join(l_output)
        fw.write('\n'.join(l_output))


    def GetProb(self, l_syntex, l_data):
##        print l_syntex
        self.l_syntex = l_syntex
        m_syntex = self.MakeMap()
##        print m_syntex
        l_prob = []
##        sys.exit(0)
        for szline in l_data:
            l_content = szline.split()[2:]
            fprob = self.Trace(l_content, m_syntex)
            l_prob.append(fprob)
        return l_prob

    def Trace(self, l_content, m_syntex):
        szkey = m_syntex['szkey']
        ret = 0.0
        if(szkey == ''): return m_syntex['fprob']
        if(szkey in l_content):
            ret = m_syntex['fprob'] * self.Trace(l_content, m_syntex['left'])
        else:
            ret = m_syntex['fprob'] * self.Trace(l_content, m_syntex['right'])
        return ret;

    def MakeMap(self):
        szline = ''
        while(szline.strip() == '') :
            szline = self.l_syntex[0]
            self.l_syntex = self.l_syntex[1:]
            szline = szline.replace('(', ' ').replace(')', ' ')
##        print szline
        m_syntex = {}
        if(len(szline.split()) == 1) :
            m_syntex['szkey'] = ''
            m_syntex['fprob'] = float(szline)
            m_syntex['left'] = 0
            m_syntex['right'] = 0
        elif(len(szline.split()) > 1) :
            szprob, szkey = szline.split()
            m_syntex['szkey'] = szkey
            m_syntex['fprob'] = float(szprob)
            m_syntex['left'] = self.MakeMap()
            m_syntex['right'] = self.MakeMap()
        return m_syntex

import time
if __name__ == "__main__":
    cm = GCJ()
    cm.RunFile()
##    print cm.GetCount(7, 10, [[1,2], [7,1]])
##    print cm.GetCount(4, 4, [[3,2]])


