#!/usr/bin/python
import sys
import copy

szfile = './A-large.in.txt'
szfile_output = './A-large.output.txt'
##szfile = './B-large.in.txt'
##szfile_output = './B-large.output.txt'

class SavingTheUnivers:
    def __init__(self):
        pass

    def RunFile(self) :
# using file set
        f = open(szfile,'rb')
        s = f.read()
# ---
        l_s = s.splitlines()
        ncase = int(l_s[0])
        l_s = l_s[1:]
        l_output = []
        for i in xrange(ncase):
            S = []
            Q = []
            nsearch = int(l_s[0])
            l_s = l_s[1:]
            for j in xrange(nsearch):
                S.append(l_s[j])
            l_s = l_s[nsearch:]

            nquary = int(l_s[0])
            l_s = l_s[1:]
            for j in xrange(nquary):
                Q.append(l_s[j])
            l_s = l_s[nquary:]

            minch = self.GetMinChange(S, Q)
            num = i + 1
            l_output.append('Case #%(num)d: %(minch)d' %locals())
# using file set
        f = open(szfile_output,'wb')
        f.write('\n'.join(l_output))
# ----


    def GetMinChange(self, S, Q):
##        print S
##        print Q
        p = 0
        k = 0
        while( p < len(Q) ) :
            p = self.GetLongWord(S, Q, p)
            k += 1

        if(k > 0):
            return k-1;
        else:
            return k

    def GetLongWord(self, S, Q, st) :
        ns = len(S)
        m_s = {}
        k = 0
        p = st
        for x in Q[st:]:
            if(not (x in m_s)):
                m_s[x] = 1
                k += 1
                if(k == ns):
                    return p
            p += 1
        return p


if __name__ == "__main__":
    cm = SavingTheUnivers()

    cm.RunFile()

