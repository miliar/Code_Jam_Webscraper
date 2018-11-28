import sys

def retidy(A):
    R = A[::-1]
    for i in xrange(1, len(R)):
        d1 = int(R[i-1])
        d2 = int(R[i])
        if d1-1>0 and d1-1>=d2:
            result = "9"*(len(R)-i-1)+str(d1-1)+R[i:]
            return result[::-1]
    if A[0]=='1':
        return "9"*(len(R)-1)
    return str(int(A[0])-1)+"9"*(len(R)-1)

def tidy(N):
    A = str(N)
    for i in xrange(1, len(A)):
        if int(A[i])<int(A[i-1]):
            return retidy(A[0:i])+'9'*(len(A)-i)
    return A
    
def brute(A):
    for i in xrange(0, A):
        if (A-i)==int(tidy(A-i)):
            return A-i

T = int(sys.stdin.readline())
for n, testcase in enumerate(sys.stdin.readlines(), 1):
    N = int(testcase)
    r = tidy(N)
    print "Case #"+str(n)+": "+str(r)
    