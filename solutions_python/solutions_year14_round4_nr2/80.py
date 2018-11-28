#!/usr/bin/python

        

def doit():
    #print repr(st)
    N = input()
    at = raw_input().split()
    A = []
    for aa in at:
        A.append(int(aa))
        
    As = A[:]
    As.sort()
    su=0
        
    for i in range(N):
        v = As[i]
        ii = A.index(v)
        li = len(A)
        li -=1
        A.remove(v)
        
        p1 = ii
        p2 = li - ii
        if p1 < p2:
            su += p1
        else:
            su += p2
            
    print su
    

    

cases = input()
for case in range(1, cases+1):
    
    print ("Case #" + str(case) + ":"),
    doit()
    
        
