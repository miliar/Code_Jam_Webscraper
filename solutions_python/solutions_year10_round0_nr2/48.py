import sys

if sys.argv[1:]:
    sys.stdin = open(sys.argv[1] + '.in')
    sys.stdout = open(sys.argv[1] + '.out', 'w')

def gcd(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a

def solve():
    a = map(long, sys.stdin.readline().split()[1:])
    t = 0
    for x in a[1:]:
        t = gcd(t, x - a[0])
    if t < 0: t = -t
    y = -a[0] % t
    if y < 0: y += t
    return str(y)

ccc = int(sys.stdin.readline())
for cc in range(1, ccc + 1):
    print "Case #%d: %s" % (cc, solve())
