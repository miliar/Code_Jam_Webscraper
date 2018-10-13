import sys, string

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

cases = int(sys.stdin.readline().strip())

for case in xrange(1, cases+1):

    s = sys.stdin.readline().strip()
    x = string.split(s, " ")
    n = int(x[0])
    m = int(x[1])
    c = int(x[2]) - int(x[1])
    if c < 0:
        c = -c

    for i in xrange(1,n+1):
        for j in xrange(i+1,n+1):
            d = int(x[i]) - int(x[j])
            if d < 0:
                d = -d
            c = gcd(c, d)

    if (m % c) > 0:
        c = c - (m % c)
    else:
        c = 0
    print "Case #" + str(case) + ": " + str(c)


