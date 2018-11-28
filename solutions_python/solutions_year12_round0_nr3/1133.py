# Problem C
import sys, os

def ComputePairs(a, b):
    pairs = 0
    for n in range(a, b+1):
        p = 0
        for d in MixDigits(n):
            if a <= d and d < n: continue
            if a <= d and d <= b: pairs += 1
        #pairs += newton(p+1, 2)
    return pairs

def MixDigits(n):
    l = []
    if n < 10: return l
    sn = str(n)
    for i in range(len(sn)-1):
        sn = sn[1:]+sn[0]
        if int(sn) == n: continue
        if sn[0] == '0': continue
        
        l.append(int(sn))
        
        
    return set(l)

def fact(n):
    if n < 2: return 1
    f = 1
    for x in range(2,n+1):
        f *= x
    return f

def newton(n,k):
    return int(fact(n) / (fact(k) * fact(n-k)))




T = int(sys.stdin.readline())

for t in range(T):
    AB = list(map(int, sys.stdin.readline().split()))
    A = AB[0]; B = AB[1]
    c = ComputePairs(A,B)

    print ("Case #{case}: {ans}".format(case = t+1, ans=c))

    

