#fly swatter
from math import *

def solve(A, B, t):
    paths = [1, 0]
    timetable = []
    for dep, arr in A:
        #from, arrival
        timetable.append([dep, 0, arr + t])
    for dep, arr in B:
        timetable.append([dep, 1, arr + t])
    timetable.sort()
    prepared = [[],[]]
    ntrains = [0, 0]
    for t, depcity, arr in timetable:
        act_trains = filter(lambda arr: arr <= t, prepared[depcity])
        if act_trains:
            #there is train prepared to departure
            print 'train from %d' % act_trains[0]
            prepared[depcity].remove(act_trains[0])
        else:
            #we need new train
            ntrains[depcity] += 1
            print 'new train'
        print 'train from %d at %d:%02d arrival at %d:%02d' % (depcity, t/60, t%60, arr/60, arr%60)
        prepared[paths[depcity]].append(arr)        
    return ntrains

#loading input
fin = open('B-large.in')
fout = open('output.txt','w')
N = int(fin.readline())
for en in xrange(N):
    #read data
    turnaround = int(fin.readline())
    data = fin.readline().split()
    NA, NB = map(lambda x: int(x), data)
    A = []
    for x in xrange(NA):
        dep, arr = fin.readline().split(' ')
        h,m = map(lambda x: int(x), dep.split(':'))
        dep = h*60 + m
        h,m = map(lambda x: int(x), arr.split(':'))
        arr = h*60 + m
        A.append([dep, arr])
    B = []
    for x in xrange(NB):
        dep, arr = fin.readline().split(' ')
        h,m = map(lambda x: int(x), dep.split(':'))
        dep = h*60 + m
        h,m = map(lambda x: int(x), arr.split(':'))
        arr = h*60 + m
        B.append([dep, arr])        
    ta, tb = solve(A, B, turnaround)
    print ta, tb
    fout.write( 'Case #%d: %d %d\n' % (en+1, ta, tb) )
fin.close()
fout.close()
