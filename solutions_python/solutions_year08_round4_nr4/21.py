#!/usr/bin/python
import sys
import copy

szfile = './D-small-attempt0.in.txt'
szfile_output = './D-small.output.txt'

##szfile = './D-large.in.txt'
##szfile_output = './D-large.output.txt'
##szfile = './B-small.in.txt'
##szfile_output = './B-small.output.txt'


class PRLE:
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
            szline = f.readline().strip()
            k = int(szline);
            szline = f.readline().strip()
            S = szline
            val = self.Proc(k, S)
            num = i+1
            l_output.append('Case #%(num)d: %(val)d'%locals())
        fw.write('\n'.join(l_output))
# using file set
# ----

    def Proc(self, k, S):
        self.P = self.MP(k)
        
        l_s = []
        p = len(S)/k;

        ret = 10000000
        for x in self.P:
            T = ''
            for j in xrange(p):
                for m in xrange(k):
                    T += S[j*k+x[m]]
            val = 1
            for j in xrange(1, len(T)):
                if(T[j] != T[j-1]):
                    val += 1
            ret = min(ret, val)
        return ret



    def MP(self, n):
        self.P = []
        U = [False] * n
        
        for i in xrange(n):
            D = []
            D.append(i)
            U[i] = True
            self.Solve(n, U, D)
            U[i] = False
        return self.P
        
    def Solve(self, n, U, D):
        if(len(D) == n):
            self.P.append(D)
            return
        
        for i in xrange(n):
            if(U[i] == False):
                T = copy.copy(D)
                T.append(i)
                U[i] = True
                self.Solve(n, U, T)
                U[i] = False
        return

if __name__ == "__main__":
    cm = PRLE()
##    print cm.MP(3)
##    print cm.Proc(4, 'abcabcabcabc')    #7
##    print cm.Proc(3, 'abcabcabcabc')    #12
    cm.RunFile()
