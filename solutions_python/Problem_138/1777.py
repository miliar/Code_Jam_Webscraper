import sys
import numpy as np

for case in xrange(int(sys.stdin.readline())):
    _ = sys.stdin.readline()
    A = sorted(map(float, sys.stdin.readline().strip().split()))
    B = sorted(map(float, sys.stdin.readline().strip().split()))
    
    
    def cheat(A, B):
        if len(A) == 1:
            return 1 if A[0] > B[0] else 0
    
        if A[0] > B[-1]:
            return len(A)
    
    
        return max(cheat(A[1:], B[1:]) + 1 if A[0]>B[0] else 0, cheat(A[1:], B[:-1]))
    
    

    def non_cheat(A, B):
        res = 0
        
        while len(A) > 0:
            if A[-1] > B[-1]:
                A.pop()
                B.pop(0)
                res += 1
            else:
                A.pop()
                B.pop()
    
        return res
    
    
        
    print "Case #"+str(case+1)+": " + str(cheat(A, B)) + " " + str(non_cheat(A, B))
