#!/usr/bin/env python

f = open('A-large.in','r')
o = open('A-large.out','w')

N = int(f.readline())

for i in xrange(N):
    o.write('Case #' + str(i+1) + ': ')
    
    P = f.readline().split()
    
    n = int(P[0])
    
    t  = 0
    O  = 1
    Ot = 0
    B  = 1
    Bt = 0
    step = None
    
    for j in xrange(n):
        if P[2*j+1] == 'O':
            if Ot > abs(int(P[2*(j+1)]) - O):
                step = 1
            else :
                step = abs(int(P[2*(j+1)]) - O) + 1 - Ot
            t += step
            Bt += step
            Ot = 0
            O = int(P[2*(j+1)])
        else :
            if Bt > abs(int(P[2*(j+1)]) - B):
                step = 1
            else :
                step = abs(int(P[2*(j+1)]) - B) + 1 - Bt
            t += step
            Ot += step
            Bt = 0
            B = int(P[2*(j+1)])
         
    o.write('%i\n' % t) 
