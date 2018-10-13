
opp = {'-':'+', '+':'-'}

def pan(s, k):
    p = list(s)
    c=0
    for i in xrange(0, len(p) - k + 1):
        if p[i] == '-':
            # flip
            for j in xrange(i, i + k):
                p[j] = opp[p[j]]
            c += 1

    if '-' in p:
        return "IMPOSSIBLE"
    else:
        return str(c)



for i in xrange(input()):
    s, k = raw_input().split(" ")
    print "Case #%d: %s" % (i+1, pan(s, int(k)))