import sys

def gcd(a, b):
    return gcd(b, a%b) if b != 0 else a

input = [line.strip() for line in sys.stdin.read().split('\n')][1:]
for testno, line in enumerate(filter(None, input)):
    times = sorted(int(x) for x in line.split()[1:])
    deltas = [times[i]-times[i-1] for i in range(1, len(times))]
    T = reduce(gcd, filter(None, deltas))
    y = T - times[0] % T if times[0] % T != 0 else 0
    print 'Case #%d: %d' % (testno+1, y)
