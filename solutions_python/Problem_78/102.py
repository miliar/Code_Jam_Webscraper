import sys

if sys.argv[1:]:
    file_name = sys.argv[1]
    if file_name.endswith('.in'):
        file_name = file_name[:-3]
    elif file_name.endswith('.'):
        file_name = file_name[:-1]
    sys.stdin = open(file_name + '.in')
    sys.stdout = open(file_name + '.out', 'w')

YES='Possible'
NO='Broken'

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def solve():
    N, Pd, Pg = map(long, sys.stdin.readline().split())
    if Pg == 0:
        if Pd > 0:
            return NO
        else:
            return YES
    if Pg == 100:
        if Pd < 100:
            return NO
        else:
            return YES
    Ud = 100 / gcd(100, Pd)
    # Ug = 100 / gcd(100, Pg)
    if Ud <= N:
        return YES
    else:
        return NO

ccc = int(sys.stdin.readline())
for cc in range(1, ccc + 1):
    print "Case #%d: %s" % (cc, solve())
