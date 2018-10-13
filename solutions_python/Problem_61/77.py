def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

def choose(n, r):
    if r == 0:
        return 1
    if n == 0:
        return 0
    return fact(n)/(fact(r)*fact(n-r))

cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    sol = fib(n-1) + fib(n-2)
    cache[n] = sol
    return sol

def solve(n):
    if n in cache:
        return cache[n]
    if n <= 2:
        return [1]
    res = [1] + [0]*(n-2)
    for i in range(2, n):
        poss = solve(i)
        s = 0
        for j, p in enumerate(poss):
            s += p * choose(n-i-1, i - j - 2)
        res[i-1] = s
    cache[n] = res
    return res
    

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(1, n+1):
        N = int(raw_input())
        s = sum(solve(N))
        
        print "Case #%d: %d" % (i, s % 100003)


