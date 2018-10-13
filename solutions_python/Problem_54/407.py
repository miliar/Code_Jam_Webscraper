import sys
import fractions

num_cases = int(sys.stdin.readline())

cases = sys.stdin.readlines()

if num_cases != len(cases):
    raise Exception("num of cases don't match");

def get_y(n, t):
    
    diffs = []
    for i in xrange(n-1):
        for j in xrange(i+1, n):
            diffs.append(abs(t[i]-t[j]))

    diffs = list(set(diffs))

    gcd = diffs[0]

    for d in diffs[1:]:
        gcd = fractions.gcd(gcd, d)
    
    rem = t[0] % gcd
    
    if rem:
        return gcd - rem
    else:
        return rem


i = 1

for case in cases:
    input = [int(e) for e in case.split()]
    n = input[0]
    t = input[1:]
    
    if n != len(t):
        raise Exception("num of t's don't match");
    
    print "Case #%s: %s" % (i, get_y(n, t))
    i += 1
