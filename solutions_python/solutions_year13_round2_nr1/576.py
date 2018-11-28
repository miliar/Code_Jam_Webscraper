'''
Created on May 4, 2013

@author: Tin Franovic
'''
import sys
class GCJSolver:
    def __init__(self, inFile):
        self.inFile=open(inFile)
        self.outFile=open(inFile.split('.')[0]+'_r.'+inFile.split('.')[1],'w+')
        self.T=int(self.inFile.readline().rstrip())
    def run(self):
        out=''
        for t in range(1,self.T+1):
            out+='Case #' + str(t) + ": " + self.solve() + "\n"
        self.outFile.write(out.rstrip())
        self.inFile.close()
        self.outFile.close()
    def getNextData(self):
        l=self.inFile.readline().rstrip().split(' ')
        if len(l)==1:
            return l[0]
        return l
    def solve(self):
        raise NotImplementedError
        
class Osmos(GCJSolver):
    def playGame(self, A, motes):
        for i in range(len(motes)):
            if A>motes[i]:
                A+=motes[i]
                motes[i]=0
        motes=[x for x in motes if x>0]
        if len(motes)==0:
            return 0
        if A==1:
            return 1+self.playGame(A, motes[:-1])
        return 1+min(self.playGame(A+A-1, motes[:]),self.playGame(A, motes[:-1]))
    def solve(self):
        l=self.getNextData()
        A=int(l[0])
        N=int(l[1])
        ll=self.getNextData()
        if N==1:
            motes=[int(ll)]
        else:
            motes=[int(x) for x in ll]
            motes.sort()
        return str(self.playGame(A,motes[:]))
solver=Osmos(sys.argv[1])
solver.run()