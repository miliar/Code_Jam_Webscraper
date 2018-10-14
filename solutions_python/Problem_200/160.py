T = int(raw_input())

def code():
    N = int(raw_input())
    s = str(N)
    best = 1
    maxc = 0
    for i, c in enumerate(s):
        if int(c) < maxc:
            break
        if i == len(s) - 1:
            val = int(s)
        else:
            if int(c)-1 >= maxc:
                val = int(s[:i] + str(int(c)-1) + ('9' * (len(s) - i-1)))
            else:
                val = 0
        maxc = max(maxc, int(c))
        best = max(val, best)
    return best

for i in xrange(1, T+1):
    print "Case #%d: %d" % (i, code())
