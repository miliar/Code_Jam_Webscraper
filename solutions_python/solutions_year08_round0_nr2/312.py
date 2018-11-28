# train.py

import sys
from collections import defaultdict

def main(inputfile):
    f = open(inputfile)
    ncases = int(f.next())
    cases = [Case(f) for _ in range(ncases)]
    for i,case in enumerate(cases):
        print 'Case #%d: %d %d' % (i+1, case.A, case.B)

def t2i(t):
    h,m = map(int, t.split(':'))
    return h*60 + m

class Station:
    def __init__(self):
        self.N = 0
        self.min = 0
        #self.nAvail = 0
    def dep(self):
        self.N -= 1
        if self.N < self.min:
            self.min = self.N
    def arr(self):
        self.N += 1

class Case:
    def __init__(self, f):
        A = Station()
        B = Station()
        
        T = int(f.next())
        self.NAB, self.NBA = map(int, f.next().split())
        self.events = []
        for i in range(self.NAB):
            t_dep, t_arr = map(t2i, f.next().split())
            self.events.append( (t_dep, A, 'dep') )
            self.events.append( (t_arr+T, B, 'arr') )
        for i in range(self.NBA):
            t_dep, t_arr = map(t2i, f.next().split())
            self.events.append( (t_dep, B, 'dep') )
            self.events.append( (t_arr+T, A, 'arr') )
        self.events.sort()
        
        for time, stn, evt in self.events:
            if evt == 'dep':
                stn.dep()
            elif evt == 'arr':
                stn.arr()
        
        self.A = -A.min
        self.B = -B.min
            

if __name__ =='__main__':
    f = sys.argv[1] if len(sys.argv)>1 else 'B-sample.in'
    main(f)
