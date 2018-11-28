from math import sqrt

def primes(n): 
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def prime_factors(n, prime_list):
    n_root = sqrt(n)
    factors = []
    for p in prime_list:
        if n%p == 0:
            factors.append(p)
    return set(factors)

for case in range(int(input())):
    A, B, P = map(int, raw_input().split())
    prime_list = [p for p in primes(B) if p >= P]
    sets = [prime_factors(A, prime_list)]
    for n in range(A+1, B+1):
        factors = prime_factors(n, prime_list)
        for s in sets[:]:
            if s.intersection(factors):
                factors.update(s)
                sets.remove(s)
        sets.append(factors)
    answer = len(sets)
    print 'Case #%d: %s' % (case+1, answer)
