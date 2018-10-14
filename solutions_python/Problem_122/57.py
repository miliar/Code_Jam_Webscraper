from collections import defaultdict

def all_possible(n,m):
    result = []
    if n <= 1:
        for i in range(2,m+1):
            result.append([i])
        return result
    for r in all_possible(n-1,m):
        for i in range(2,m+1):
            x = r[:]
            x.append(i)
            result.append(x)
    return result

primes = [2,3,5,7,11]

def factors(product, m):
    i = 0
    result = defaultdict(int)
    while primes[i] <= m and product > 1:
        if product % primes[i] == 0:
            product /= primes[i]
            result[primes[i]] += 1
        else:
            i += 1
    return result

def all_product_factors(products, m):
    result = defaultdict(int)
    for p in products:
        f = factors(p, m)
        for k,v in f.items():
            result[k] = max(v, result[k])
    return result
    
def fits(bases, f):
    f = f.copy()
    for b in reversed(sorted(bases)):
        bf = factors(b, 11)
        for k,v in bf.items():
            if f[k] - v < 0:
                continue
            f[k] -= v
    return sum(f.values()) == 0
        

def solve(n,m,products):
    f = all_product_factors(products, m)
    for sol in all_possible(n,m):
        if fits(sol, f):
            return sol
    return [2]*n

if __name__ == "__main__":
    raw_input()
    R,N,M,K = map(int, raw_input().split())
    print "Case #1:"
    for i in range(R):
        products = map(int, raw_input().split())
        print "".join(map(str, solve(N,M,products)))
