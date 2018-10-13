import sys
from pprint import pprint

def circular_perms(n):
    s = str(n)
    return (int(''.join(s[i:]+s[:i])) for i in xrange(len(s)))

def binomialCoefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - (k - (i+1)))
        c = c // (i+1)
    return c

def solve(A, B):
    #print A, B
    allperms = set()
    for n in xrange(A,B+1):
        validperms = set()
        for x in circular_perms(n):
            if A <= x <= B:
                validperms.add(x)
        if len(validperms) > 1:
            allperms.add(frozenset(validperms))

    #pprint(allperms)
    return sum(binomialCoefficient(len(p),2) for p in allperms)

def main():
    with open(sys.argv[1]) as f:
        f.readline()
        for i, line in enumerate(f):
            vals = [int(x) for x in line.strip().split()]
            res = solve(vals[0], vals[1])
            print 'Case #%d: %d' % (i+1, res)

if __name__ == "__main__":
    main()
