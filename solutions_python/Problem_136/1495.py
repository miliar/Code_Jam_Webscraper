import sys

def line():
    return sys.stdin.readline().strip()

def ints(s):
    return [int(t) for t in s.split()]

def floats(s):
    return [float(t) for t in s.split()]



def kahan(rs):
    res = 0.0
    c = 0.0
    for r in rs:
        y = r - c
        t = res + y
        c = (t - res) - y
        res = t
    return res

def calc(c,f,x):
    if x <= c*2:
        return x/2
    n = int(( (x-c)*f - 2*c ) / ( c*f ))
    rs = []
    for i in range(n + 1):
        rs.append( c / (2 + f*i) )
    rs.append(x / (2 + f*(n+1)))
    r = kahan(rs)
    return r


def main():
    tc = int(line())
    for i in range(1,tc+1):
        c,f,x = floats(line())

        r = 0.0
        f1 = 2.0
        while x / (f1 + f) < (x - c) / f1:
            r += c / f1
            f1 += f
        r += x / f1

        print 'Case #%s: %s' % (i, '{:.7f}'.format(r))

main()
