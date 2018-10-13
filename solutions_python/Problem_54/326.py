#A + T = N1 * D
#B + T = N2 * D
#C + T = N3 * D
#
#B - A = n1 * D
#C - B = n2 * D
#
#GCD of (B - A), (C - B), etc...
#GCD - (C - x * GCD) = GCD - C + x * GCD

def GCD_pair(a, b):
    #print (a, b)
    if b == 0:
        return a
    else:
        return GCD_pair(b, a % b)

def GCD_vector(L):
    acc = L[0]
    for n in xrange(1, len(L)):
        acc = GCD_pair(acc, L[n])
    return acc

def LCM_pair(a, b):
    v = (a / GCD_pair(a, b)) * b
    print "LCM(%d, %d) = %d" % (a, b, v)
    return v

def LCM_vector(L):
    acc = L[0]
    for n in xrange(1, len(L)):
        acc = LCM_pair(acc, L[n])
    return acc

infile = file("B-large.in")
C = int(infile.readline())
for c in xrange(C):
    line = map(int, infile.readline().split())
    N, t = line[0], line[1:]

    #import random
    #t = [X * int(1e40) + random.randint(1, int(1e45)) for X in t]
    
    t.sort()
    t_deltas = [t[n + 1] - t[n] for n in xrange(len(t)-1)]
    #print t
    #print t_deltas
    #LCM = LCM_vector(t_deltas)
    #print LCM
    GCD = GCD_vector(t_deltas)
    #print GCD
    if GCD == 1:
        next = 0
    else:
        most_recent_event = t[0]
        time_since_last_anniversary = most_recent_event % GCD
        next = (GCD - time_since_last_anniversary) % GCD
    print "Case #%d: %d" % (c + 1, next)
    #print (next, GCD)
    assert next < GCD
    for x in t:
    #    print (next, x, GCD)
        assert (next + x) % GCD == 0
