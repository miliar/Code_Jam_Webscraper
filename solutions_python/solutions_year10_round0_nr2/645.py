import sys
import fractions


def GCD(S):
    t = S[0]
    for s in S:
        t = fractions.gcd(t,s)
    return t


C = int(raw_input() )
for c in range(C):
    dt = 0
    d = 10**50
    T = map(int,(sys.stdin.readline()).split(' ')[1:])
    T.sort()

    D = [(T[len(T)-1]-x) for x in T ][:len(T)-1]   

    d = GCD(D)
    #print(d)
    
    y = -T[0] + d
    while y <0 :
        y += d
 
    
    sys.stdout.write('Case #%d: %d\n' %  (c+1,y))

#pyhon B.py < B-small.in > B-small.out