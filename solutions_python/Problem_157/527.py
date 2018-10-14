import math
from functools import reduce
inf = open("in.in", "r")
ouf = open('out.out','w')

def close_files():
    inf.close()
    ouf.close()

def precount():
    pass

printcounter = 0
def printstr(a):
    global printcounter
    printcounter +=1
    print ('Case #%d: %s' % (printcounter,a), file=ouf)

class Quater:
    e=0
    i=0
    j=0
    k=0
    def __init__(self, e,i = 0,j = 0,k = 0):
        if isinstance(e,str):
            if e == '1':
                self.e = int(1)
            elif e == 'i':
                self.i = int(1)
            elif e == 'j':
                self.j = int(1)
            elif e == 'k':
                self.k = int(1)
        else:
            self.e = e
            self.i = i
            self.j = j
            self.k = k
    def __repr__(self):
        return str(self.e)+str(self.i)+str(self.j)+str(self.k)
    def __mul__(self,other):
        return Quater(
            e = self.e*other.e-self.i*other.i-self.j*other.j-self.k*other.k,
            i = self.e*other.i+self.i*other.e+self.j*other.k-self.k*other.j,
            j = self.e*other.j-self.i*other.k+self.j*other.e+self.k*other.i,
            k = self.e*other.k+self.i*other.j-self.j*other.i+self.k*other.e)
    def __eq__(self,other):
        if other=='1':
            return self.e==1
        elif other == 'i':
            return self.i==1
        elif other == 'j':
            return self.j == 1
        elif other == 'k':
            return self.k == 1
    def __neg__(self):
        return Quater(-self.e,
                      -self.i,
                      -self.j,
                      -self.k)
def multy(str):
    return reduce(Quater.__mul__,map(Quater,str))   

def solvetest():
    l, x = map(int, inf.readline().split())
    s = inf.readline().strip()
    s1 = s*min(20,x)
    bbbb = x - min(20,x)
    t = multy(s)
    if bbbb:
        if t == '1':
            tttt = t
        elif -t == '1':
            if bbbb % 2:
                tttt = t
            else:
                tttt = Quater('1')
        else:
            if bbbb % 4 == 0:
                tttt = Quater(1,0,0,0)
            elif bbbb % 4 == 1:
                tttt = t
            elif bbbb % 4 == 2:
                tttt = Quater(-1,0,0,0)
            elif bbbb % 4 == 3:
                tttt = -t
    else:
        tttt = Quater('1')
    t = Quater('1')
    i = 0
    N = len(s1)
    while not(t=='i') and i<N:
        t = t*Quater(s1[i])
        i += 1
    t = Quater(1)
    while not(t == 'j') and i<N:
        t = t*Quater(s1[i])
        i += 1
    if i == N:
        printstr('NO')
        return
    t = Quater(1)
    while i<N:
        t = t*Quater(s1[i])
        i += 1
    t = t*tttt
    if t == 'k':
        printstr('YES')
    else:
        printstr('NO')
#precount()
testnum = int(inf.readline())
for test in range(testnum):
    solvetest()
close_files()

