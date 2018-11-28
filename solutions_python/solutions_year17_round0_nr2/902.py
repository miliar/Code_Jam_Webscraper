import math

def tidy_digit(N):
    S = str(N)
    count = 0
    n = len(S)
    for i in xrange(n-1):
        if S[i] > S[i+1]:
            return n-i-1
    return 0

def solve(N):
    n = 0
    M = math.log10(N)
    D = tidy_digit(N)
    while n < D:
        d = 10**n
        N -= N%(10*d) - N%d + d
        n+=1
        D = tidy_digit(N)
    return N


for i in xrange(1, input()+1):
    l = input()
    print "Case #%d: %s"%(i, solve(l))