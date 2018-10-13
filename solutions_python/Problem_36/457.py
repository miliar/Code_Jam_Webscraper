
# -*- coding: cp949 -*-

import sys, copy

global retv
def go(q,s,qi,si):
    global retv
    
    if(qi == len(q)):
        retv = retv+1
    else:
        k = si
        while 1:
            k = s.find(q[qi],k)
            if(k != -1):
                go(q,s,qi+1,k+1)
            else:
                break
            k = k+1
        
##    n = s.count(q[qi],si)
##    if(n == 0):
##        return
##    elif(qi == len(q)-1):
###        print("yes")
##        retv = retv+1
##    else:
##        k = si
##        for i in range(n):
##            k = s.find(q[qi],k)
##            go(q,s,qi+1,k+1)
##            k = k+1
##        go(q,s,qi+1,k)

if(len(sys.argv) == 1):
    fin = open("ex3.in", 'r')
    fout = open("ex3.out", 'w')
else:
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')

N = fin.readline().rstrip('\r\n')
N = int(N)

for i in range(N):
    retv = 0
    l = fin.readline().rstrip('\r\n')
    go("welcome to code jam",l,0,0)
    fout.write("Case #%d: %04d\n" % (i+1, retv))

fin.close()
fout.close()
