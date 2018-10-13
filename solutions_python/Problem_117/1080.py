'''
Created on Apr 12, 2013
@author: jean
'''
import itertools

TRUE = set([True,])
_DEBUG=False

class grass(object):
    
    def __init__(self, target):
        self.target = target
        nr = len(target)
        nc = len(target[0])
        self.nc=nc
        self.nr=nr
        mx = self.getMax()
        self.current=[[mx] * self.nc for l in range(self.nr)]
        # keep correct current cut (could test each time instead - easier to debug, track
        # could keep the step,direction where itt happened
        self.passed=[[False] * self.nc for l in range(self.nr)]
        for r in xrange(self.nr):
            for c in xrange(self.nc):
                if self.target[r][c] == mx:
                    self.passed[r][c]=True
        if _DEBUG: 
            print "INITIAL STATE",self.current 
            print "INITIAL CORRECT CUT",self.passed 
            print "TARGET",self.target 
            
    def getNCols(self):
        return self.nc

    def getNRows(self):
        return self.nr

    def getMax(self):
        m=max(itertools.chain(*self.target))
        #print "***MAX",m
        return m
    
    def getValues(self):
        vls=list(set(itertools.chain(*self.target)))
        #print "***VALUES",vls
        return vls

    # try to cut at h
#    def passAt(self, h):
#        for r in xrange(self.nr):
#            for c in xrange(self.nc):
#                if self.passed[r][c]: break
#            
#    for i in range(nc):
#        u = list(set([l[j][i] for j in range(nr)]))
#        print u
#        if len(u) == 1:
#            g.setCol(i)
 
    def passAtFromBottom(self, h):
        if _DEBUG: print "BOTTOM"
        for c in reversed(xrange(self.nc)):
            cutCol=True
            for r in xrange(self.nr):
                if self.passed[r][c] and self.current[r][c] > h: 
                    cutCol=False
                    break
            if _DEBUG: print "col",c,"cut=",cutCol
            if cutCol:
                for r in xrange(self.nr): # TODO optim
                    self.current[r][c]=h
                    if self.current[r][c] == self.target[r][c]:
                        self.passed[r][c] = True

    # itertools for col array? numPy?
    def passAtFromTop(self, h):
        if _DEBUG: print "TOP"
        for c in xrange(self.nc):
            cutCol=True
            for r in xrange(self.nr):
                if self.passed[r][c] and self.current[r][c] > h: 
                    cutCol=False
                    break
            if _DEBUG: print "col",c,"cut=",cutCol
            if cutCol:
                for r in xrange(self.nr): # TODO optim
                    self.current[r][c]=h
                    if self.current[r][c] == self.target[r][c]:
                        self.passed[r][c] = True

    
    def passAtFromRight(self, h):
        if _DEBUG: print "RIGHT"
        for r in reversed(xrange(self.nr)):
            cutRow=True
            for c in xrange(self.nc):
                if self.passed[r][c] and self.current[r][c] > h: 
                    cutRow=False
                    break
            if _DEBUG: print "row",r,"cut=",cutRow
            if cutRow:
                self.current[r]=[h for c in xrange(self.nc)]
                for c in xrange(self.nc):
                    if self.current[r][c] == self.target[r][c]:
                        self.passed[r][c] = True

    
    def passAtFromLeft(self, h):
        if _DEBUG: print "LEFT"
        for r in xrange(self.nr):
            cutRow=True
            for c in xrange(self.nc):
                if self.passed[r][c] and self.current[r][c] > h: 
                    cutRow=False
                    break
            if _DEBUG: print "row",r,"cut=",cutRow
            if cutRow:
                self.current[r]=[h for c in xrange(self.nc)]
                #print self.current
                for c in xrange(self.nc):
                    if self.current[r][c] == self.target[r][c]:
                        self.passed[r][c] = True
           
    def setRow(self, r):
        self.passed[r]=[True] * self.nc;
        #print "***R",i
        
    def setCol(self, c):
        for r in range(self.nr):
            self.passed[r][c]=True
        #print "***C",i

    def getStatus(self):
        if _DEBUG: print "CHECK",self.passed
        return set(itertools.chain(*self.passed)) == TRUE
#        for r in range(self.nr):
#            for c in range(self.nc):
#                if self.passed[r][c]==False: return False
#        return True

    
        

def game(l):
    if _DEBUG: print l
    g = grass(l)
    nr = g.getNRows()
    nc = g.getNCols()
    mxh=g.getMax()-1
    vals = sorted(g.getValues() ,reverse=True)
    if _DEBUG: print "NR,NC,MX,VALS",nr,nc, mxh, vals
    
    if g.getStatus(): return "YES"

    # try to cut from max to 1
    for h in vals:
        if _DEBUG: print "- try h=",h
        g.passAtFromLeft(h)
        if g.getStatus(): return "YES"
        # most likely useless
        g.passAtFromRight(h)
        if g.getStatus(): return "YES"
        g.passAtFromTop(h)
        if g.getStatus(): return "YES"
        # most likely useless
        g.passAtFromBottom(h)
        if g.getStatus(): return "YES"
    
    return "NO"

def main(inp,outp):
    N = int(inp.readline())
    for i in xrange(N):
        if _DEBUG: print "==========================================", i+1
        str = inp.readline().strip()
        sx,sy = str.split()
        x=int(sx)
        y=int(sy)
        l=[]
        for j in xrange(x):
            str = inp.readline().strip()
            ss=str.split()
            l.append([int(s.strip()) for s in ss])
        res = game(l)
        outp.write ("Case #%d: %s\n" % (i + 1, res))
        if _DEBUG: print "***************",res
        if _DEBUG: print

if __name__ == '__main__':
    import sys
    #main(sys.stdin,sys.stdout)
    #inf=open("B.in","rU")
    #ouf=open("B.out","w")
    #inf=open("B-small-attempt0.in","rU")
    #ouf=open("B-small-attempt0.out","w")
    inf=open("B-large.in","rU")
    ouf=open("B-large.out","w")
    main(inf,ouf)
    inf.close()
    ouf.close()

            