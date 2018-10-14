import sys

def line():
    return sys.stdin.readline().strip()

def ints(s):
    return [int(t) for t in s.split()]


def solve(d, ps):
    m = None
    for (k,s) in ps:
        if not m:
            m = (d - k)/ float(s)
        else:
            m = max(m, (d - k)/ float(s))
    return d / m

def main():
    tc = int(line())
    for i in range(1,tc+1):
        s = ints(line())
        d, n = s
        ps = []
        for k in range(n):
            ps.append(ints(line()))

        print 'Case #%s: %s' % (i, solve(d, ps))

main()
