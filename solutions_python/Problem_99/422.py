from __future__ import division
import sys

rl = lambda: sys.stdin.readline().strip()

for k in range(int(rl())):
    A, B = map(int, rl().split())
    P = map(float, rl().split())
    
    hit = ['']*(2**A)
    prob = [1]*(2**A)
    
    for i in range(2**A):
        hit[i] = ('0'*len(format(A, 'b')) + format(i, 'b'))[-A:] 
        for j in range(A):
            if hit[i][j]=='1':
                prob[i] *= P[j]
            else:
                prob[i] *= 1-P[j]
    
    #1
    e1 = 0
    for i in range(2**A):
        c = B-A+1
        w = B-A+1+B+1
        if hit[i].find('0')==-1:
            e1 += prob[i]*c
        else:
            e1 += prob[i]*w
    
    #2all
    e2all = A+B+1
    
    #e2
    import sys
    e2 = sys.maxint
    for i in range(1, A):
        e2tmp=0
        c = i*2+B-A+1
        w = c + B+1
        for j in range(2**A):
            if hit[j][0:A-i].find('0')==-1:
                e2tmp += prob[j]*c
            else:
                e2tmp += prob[j]*w
        if e2>e2tmp:
            e2 = e2tmp
            
    #e3
    e3 = 1+B+1
    
    print "Case #%d: %f" % ((k+1), min([e1,e2all,e2,e3]))
    