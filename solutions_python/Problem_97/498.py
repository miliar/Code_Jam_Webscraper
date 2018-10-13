import sys

def solve(a, b):
    ans = 0
    f = str(b)
    for n in xrange(a,b):
        s = str(n)
        was = set()
        for c in xrange(1,len(s)):
            if s[c] >= s[0] and s[c] <= f[0]:
                t = s[c:] + s[:c]
                if s < t <= f and t not in was:
                    ans += 1
                    was.add(t)
    return ans


sys.stdin.readline()

case = 1

for line in sys.stdin:
    a,b = map(int, line.split()[:2])
    print "Case #%d: %d" % (case, solve(a,b))
    case += 1
