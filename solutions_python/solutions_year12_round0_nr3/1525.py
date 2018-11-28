import sys

num = [0 for i in xrange(10)]

A = 1111
B = 2222

def fact(x):
    p = 1
    for i in xrange(1,x+1):
        p*=i
    return p

def c(n, k):
    return fact(n)/(fact(k)*fact(n-k))

t = int(raw_input())

for case in xrange(t):
    #A = int(raw_input
    line = raw_input()
    sp = line.split(" ")
    A, B = int(sp[0]), int(sp[1])

    g = set()
    total = 0
    
    for i in xrange(A, B+1):
        m = map(str, str(i))
        size = len(m)-1

        s = set()

        s.add(i)
        for j in xrange(size):
            m.append(m.pop(0))
            new = int("".join(m))
            sz = len(str(new))

            if sz==size+1 and A<=new<=B:
                s.add(new)
        
        if len(s)>1 and s.intersection(g) == set():
            g = g.union(s)
            total += c(len(s), 2)
            
    print 'Case #%d:' % (case+1), total
