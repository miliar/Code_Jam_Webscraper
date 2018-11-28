import time
starttime = time.time()

f = open("A-large.in", "r")
f2 = open("A-large.out", "w")

##prime_max = 10000
##is_prime = [1] * prime_max
##is_prime[0] = is_prime[1] = 0
##
##for j in range(4, prime_max, 2):
##    is_prime[j] = 0
##i = 3
##while i < prime_max:
##    if is_prime[i]:
##        for j in range(2*i, prime_max, i):
##            is_prime[j] = 0
##    i += 2
##
##primes = [i for i in range(prime_max) if is_prime[i]]
##
##def frac(p, q):
##    if q == 0 and p == 0:
##        return 'undef'
##    if q == 0:
##        return 'inf'
##    if p == 0:
##        return (0, 1)
##    
##    for j in primes:
##        if j > p or j > q:
##            break
##        while p % j == q % j == 0:
##            p /= j
##            q /= j
##
##    return (p, q)

try:
    T = int(f.readline().strip())

    # intersect if not parallel, and ranges overlap properly
    for i in range(T):
        grad = {}
        
        n = int(f.readline().strip())
        a = [0] * n
        b = [0] * n
        
        for j in range(n):
            [a[j], b[j]] = map(int, f.readline().strip().split(" "))

        count = 0
        for j in range(n):
            for k in range(j+1, n):
                if (a[j] > a[k] and b[j] < b[k]) or (a[j] < a[k] and b[j] > b[k]):
                    count += 1

        s = "Case #%d: %d\n" % (i+1, count)
        print s,
        f2.write(s)        
        
    f2.flush()
    
finally:
    f.close()
    f2.close()

print (time.time() - starttime)
