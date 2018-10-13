import sys

def perms(x, A, B, done):
    for i in range(1, len(x)):
        n = x[i:] + x[:i]
        if int(n) >= A and int(n) <= B and n != x:
            yield n


            #from collections import defaultdict

def solve(A, B):
    t = 0


    for ix in xrange(A, B + 1):
        x = str(ix)
        l = len(x)
        xx = x + x
        done = set()
        for i in xrange(1, l):
            n = xx[i:i + l]

            #print x, n
            nn = int(n)
            if n not in done and nn >= A and nn <= B and nn != ix:
                t += 1
                done.add(n)

        #for n in perms(x, A, B):
            #print x, n
            #t += 1
    assert t % 2 == 0
    return t/2
    print 'total', t/2



for i,l in enumerate(sys.stdin.readlines()[1:]):
    l = l.strip()

    A,B = l.split()
    A = int(A)
    B = int(B)

    #print A, B
    print 'Case #%s: %s' % (i + 1, solve(A, B))

    #solve(1, 2000000)