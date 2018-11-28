import math

def solved(A,B):
    a = len(A) - 1
    b = len(B) - 1
    while b >= 0:
        if (A[a] > B[b]):
            a = a-1; b = b-1
        else:
            b = b - 1
    return len(A) - a - 1 

def solve(A,B):
    a = 0
    b = 0
    while b < len(B):
        if (A[a] <  B[b]):
            a = a+1; b = b+1
        else:
            b = b + 1
    return len(A) - a 
for n in xrange(int(raw_input())):
        raw_input()
        A = sorted(map(float, raw_input().split(" ")))
        B = sorted(map(float, raw_input().split(" ")))
        print "Case #%d: %d %d" % (n+1, solved(A,B), solve(A,B))

