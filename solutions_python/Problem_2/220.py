from __future__ import with_statement
from copy import copy

#import sys
#sys.setrecursionlimit(20000)


class tempo(object):
    def __init__(self, s):
        self.a = s.split(':')
        self.x = [int(i) for i in self.a]
        self. Tempo = self.x[0]*60 + self.x[1]
    def getMin(self):
        return self.Tempo
    def getHr(self):
        return '%s:%s' % (self.a[0],self.a[1])

    m = property(getMin)
    h = property(getHr)

class Trip(object):
    def __init__(self,start,end):
        self.start = tempo(start)
        self.end = tempo(end)
        self.duration = self.end.m - self.start.m
        self.busy = False
    def __cmp__(self,x):
        return cmp(self.start.m,x.start.m)
    def use(self):
        self.busy = True
    def isfree(self):
        return self.busy == False

    is_free = property(isfree)
    def __repr__(self):
        return '%s->%s(%d)' % (self.start.h,self.end.h,self.is_free)
    

class Train(object):
    def __init__(self,Time):
        self.Time = tempo(Time)
        self.init = False
    def TripTrough(self, trip, turnaround):
        'Returns True if the train can trip (and it does)'
        if (trip.is_free and self.Time.m+turnaround <= trip.start.m) or self.init ==False:
            self.init = True
            self.Time = trip.end
            trip.use()
            return True
        else:
            return False
    def __repr__(self):
        if 'Time' in dir(self):
            return self.Time.h
        else:
            return 'TmpNone'
            
        

class Table(object):
    def __init__(self,A,B,T): # trip lists...
        self.A = A
        self.B = B
        self.T = T # turnaraund
    def solver(self, starting,ending,train):
        starting.sort()
        s = starting
        for i in s:
            if train.TripTrough(i,self.T):
                return self.solver(ending,starting,train)
        # else...
        return train
        
            
    def solve(self):
        tfa = []
        tfb = []
        
        check = True
        while check:
            freeA = [i for i in self.A if i.is_free]
            freeB = [i for i in self.B if i.is_free]
            #print freeA, freeB
            if len(freeB) > 0 and len(freeA)>0:
                mins = min(freeA),min(freeB)
            elif len(freeB) == len(freeA) == 0:
                break
            if len(freeA)>0 and (len(freeB) == 0 or mins[0]<mins[1]): #start from A
                tfa.append(self.solver(freeA,freeB,Train('00:00')))
            else:
                tfb.append(self.solver(freeB,freeA,Train('00:00')))
        return len(tfa),len(tfb)
            
        
def eatFile(path_in,path_out):
    with file(path_in,'r') as f_in:
        N = int(f_in.readline().replace('\n',''))     
        with file(path_out, 'w') as f_out:
            for i in xrange(0,N):
                T  = int(f_in.readline().replace('\n',''))

                ab = f_in.readline().replace('\n','').split(' ')
                a,b = [int(k) for k in ab]

                A = []
                B = []
                for j in xrange(0,a):
                    ab = f_in.readline().replace('\n','').split(' ')
                    #print ab
                    cur_trip = Trip(ab[0],ab[1])
                    A.append(cur_trip)
                for j in xrange(0,b):
                    ab = f_in.readline().replace('\n','').split(' ')
                    cur_trip = Trip(ab[0],ab[1])
                    B.append(cur_trip)

                #print '\n\n\n\n',A,'\n',B,'\n',T

                na,nb = Table(A,B,T).solve()
                #print int(i)+1

                s = 'Case #%d: %d %d' % (i+1,na,nb)
                print s
                f_out.write(s+'\n')

                

eatFile('B-large.in','blarge.txt')
                    
                    












                
