import math

def gcdList(T):
    GCD = T[0]
    for i in xrange(1, len(T)):
        GCD = gcd(T[i], GCD)
    return GCD

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def solve(f):
    N, T = f.readline().split(" ", 1)
    N = int(N)
    T = map(int, T.split())
    D = []
    
    for i in xrange(len(T)):
        D.append(abs(T[i-1]-T[i]))

    gcd = gcdList(D)
    minT = min(T)
    difference = gcd*( int(math.ceil(float(minT) / gcd)) ) - minT
    
    #verify
    if gcdList( [ t+difference for t in T ] ) != gcd:
        print "Verification error!"
        
    return difference

with open('B-small.in', 'r') as f:
    C = int(f.readline())
    results = [solve(f) for i in xrange(C) ]
    for i in xrange(C):
        print "Case #%d: %s" % (i+1, results[i])