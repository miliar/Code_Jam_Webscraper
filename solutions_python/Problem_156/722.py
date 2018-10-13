from math import log

def rec(s, t=0):
    n = max(s)
    s.remove(n)
    if n <= 3:
        return n + t
    r = min(rec(s + [x, n-x], t+1) for x in xrange(2, n/2+1))
    return min(r, n + t)

def solve(s):
    return rec(s)


def parse(fname):
    with open(fname) as f:
        next(f), next(f)
        for line in f:
            yield [int(x) for x in line.split()]
            next(f)

        
def display(i, r):
    print "Case #{}: {}".format(i, r)


def solve_file(fname):
    for i, s in enumerate(parse(fname), 1):
        display(i, solve(s))

 
if __name__ == "__main__":
    import sys
    solve_file(sys.argv[1])




