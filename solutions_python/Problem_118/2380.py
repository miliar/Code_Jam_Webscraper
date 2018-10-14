import math

def parse(file):
    l = open(file, "r").readlines()
    l = l[1:]
    ll = []
    for r in l:
        r = r.split(' ')
        r = [int(x) for x in r]
        ll.append(r)
    return ll

def isPalyndrom(n):
    n = str(n)
    l = len(n)
    r = True
    for i in range(l/2):
        r = r and (n[i] == n[max((l-i-1), 0)])
    return r

def solve_tc((a, b)):
    c = int(math.ceil(math.sqrt(a)))
    d = int(math.floor(math.sqrt(b)))
    r  = 0
    for i in range(c, d+1):
        if isPalyndrom(i):
            h = i**2
            r += isPalyndrom(h)
    return r

def solve(filename):
    f = open("out", "w")
    l = parse(filename)
    for (i,tc) in enumerate(l):
        r = solve_tc(tc)
        f.write("Case #%d: %d\n" % (i+1, r))
    f.close()
