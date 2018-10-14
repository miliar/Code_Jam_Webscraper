def gen_primes(lim):
    ar = list(range(lim))
    for i in range(2, lim-1):
        if ar[i] == 0:
            continue
        x = 2*i
        while x < lim:
            ar[x] = 0
            x += i
    ar.pop(0)
    ar.pop(0)
    for x in ar:
        if x:
            yield(x)

def init_factors(limit):
    primes = tuple(gen_primes(limit))
    factors = [0 for _ in range(limit)]

    for p in primes:
        factors[p] = 1

    for i in range(2, limit):
        for p in primes:
            pro = p * i
            if pro >= limit:
                break
            factors[pro] = i
    return factors

def get_factors(factors, n, m):
    while n != 1:
        x = n // factors[n]
        if x >= m:
            yield x
        n = factors[n]

def merge(a, b, sets):
    set1 = None
    set2 = None
    for s in sets:
        if a in s:
            set1 = s
        if b in s:
            set2 = s
    if set1 == set2:
        return
    set1.update(set2)
    sets.remove(set2)
    

factors = init_factors(10000)
def run_case():
    A, B, P = map(int, input().split())
    sets = [set((x,)) for x in range(A, B+1)]
    for i in range(A, B):
        for j in range(i+1, B+1):
            sa = set(get_factors(factors, i, P))
            sb = set(get_factors(factors, j, P))
            if sa.isdisjoint(sb):
                continue
            merge(i, j, sets)
    return len(sets)

    

def main():
    
    N = int(input())
    for i in range(N):
        r = run_case()
        print('Case #%d: %s' % (i+1, r))


main()
