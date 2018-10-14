import sys

def ok(t, p):
    for a in xrange(0,11):
        for b in xrange(a,a+2):
            for c in xrange(b,a+2):
                if a + b + c == t and c >= p:
                    return True
    return False

def wow_ok(t, p):
    for a in xrange(0,11):
        for b in xrange(a,a+3):
            for c in xrange(b,a+3):
                if a + b + c == t and c >= p:
                    return True
    return False

sys.stdin.readline()
case = 1
for line in sys.stdin:
    input = map(int, line.strip().split())
    n, s, p = input[0:3]
    t = input[3:]
    dp = dict()
    for i in xrange(0, n+1):
        for j in xrange(0, s + 1):
            dp[i,j] = 0
    for i in xrange(0, n):
        for j in xrange(0, s + 1):
            if ok(t[i], p):
                dp[i+1,j] = max(dp[i+1,j], dp[i,j] + 1)
            else:
                dp[i+1,j] = max(dp[i+1,j], dp[i,j])
            if j < s and wow_ok(t[i], p):
                dp[i+1,j+1] = max(dp[i+1,j+1], dp[i,j] + 1)
            elif j < s and t[i] > 1 and t[i] < 29:
                dp[i+1,j+1] = max(dp[i+1,j+1], dp[i,j])
    print "Case #%d: %d" % (case, dp[n, s])
    case += 1

