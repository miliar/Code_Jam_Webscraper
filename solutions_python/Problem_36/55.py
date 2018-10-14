#!/usr/bin/python
import sys
import copy

#2009 GCJ qual B
##szfile = './C-test.in.txt'
##szfile_output = './C-test.output.txt'
##szfile = './C-small-attempt0.in'
##szfile_output = './C-small.output.txt'
szfile = './C-large.in'
szfile_output = './C-large.output.txt'

str_codejam = 'welcome to code jam'

class Price:
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
        for c in xrange(ncase):
            num = c+1
            str_line = l_s[0]
            l_s = l_s[1:]
            value = self.GetCount(str_line)
            l_output.append('Case #%(num)d: %(value)04d' %locals())
        print l_output

# using file set
        f = open(szfile_output,'wb')
        f.write('\n'.join(l_output))
# ----

    def GetCount(self, str_input):
        ninput = len(str_input)
        ncj = len(str_codejam)
        D = [ [0] * ninput for i in xrange(ncj) ]
        ncount = 0
        for i in xrange(ninput):
            if(str_input[i] == str_codejam[0]): ncount += 1
            D[0][i] = ncount % 10000
        for i in xrange(1, ncj):
            for j in xrange(i, ninput):
                if(str_codejam[i] == str_input[j]):
                    D[i][j] = (D[i][j-1] + D[i-1][j-1]) % 10000
                else:
                    D[i][j] = D[i][j-1]
##        print D
        return D[ncj-1][ninput-1]

if __name__ == "__main__":
    cm = Price()
    cm.RunFile()



