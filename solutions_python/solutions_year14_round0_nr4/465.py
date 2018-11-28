# -*- coding: UTF-8 -*-
import sys

f = open(sys.argv[1])
N = int(f.readline())

eps = 0.000001
def war(A,B):
    score = 0
    while A:
        a = A.pop()
        win = True
        for x in B:
            if x > a:
                B.remove(x)
                win = False
                break

        if win and B:
            score += 1
            B.pop(0)

    return score


def newwar(A,B):
    while A:
        maxb = B[-1]
        found = False
        for x in A:
            if x > maxb and not found:
                A.remove(x)
                B.pop(0)
                found = True
                score += 1
   
        if not found:
            A.pop(0)
            B.pop()



def decwar(A,B):
   ms = 0
   while A:
        if A[0] < B[0]:
           A.pop(0)
           B.pop()

        if A and A[0] > B[0]:
           A.pop(0)
           B.pop(0)
           ms += 1
   
   return ms

        



#    score = 0
#    if B[-1] > A[0]:
#        B.pop()
#        A.pop(0)
#
#    while A:
#        maxb = B[-1]
#        found = False
#        for x in A:
#            if x > maxb and not found:
#                A.remove(x)
#                B.pop(0)
#                found = True
#                score += 1
#                
#
#
#        if not found:
#            A.pop(0)
#            B.pop()
#
#    return score






                





for i in xrange(1, N+1):
    #print "Case #%d:" % i
    f.readline()
    Al = f.readline().strip("\n").split(" ")
    Bl = f.readline().strip("\n").split(" ")
    A = [ float(x) for x in Al ]
    B = [ float(x) for x in Bl ]

    A.sort()
    B.sort()

    W = war(A[:],B[:])
    D = decwar(A[:],B[:])
    print "Case #%d: %d %d" % (i, D, W)


    



        
    
