def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

n_cases = input()

for case in xrange(1, n_cases + 1):
    n, pd, pg = map(int, raw_input().split())
    
    good = False

    d = 100 / gcd(100, pd)

    if d <= n:
        wd = d * pd / 100
        wg = pg * 10000
        if wg >= wd and wg <= 1000000 - (d - wd):
            good = True
            
    print "Case #%d:" % case, "Possible" if good else "Broken"
