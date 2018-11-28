#!/usr/bin/python
import sys

import random
randint = random.Random().randint

def solveslow(R, K, groups):
    p = 0
    for i in xrange(R):
        s = 0
        for g in xrange(len(groups)):
            if s + groups[g] > K: 
                groups = groups[g:] + groups[0:g]
                break
            s += groups[g]
        assert s <= K
        p += s
    return p

ERR = -10**8
def solve(R, K, groups):
    N = len(groups)
    next = [ERR for i in xrange(N)]
    amount = [ERR for i in xrange(N)]
    for i in xrange(N):
        s = 0
        for j in xrange(N):
            if s + groups[(i+j)%N] > K:
                next[i] = (i+j)%N
                amount[i] = s
                break
            s += groups[(i+j)%N]
        else:
            next[i] = i
            amount[i] = s

    state = 0
    p = 0

    r = R
    am = [amount]
    n = [next]
    while r != 0:
        if r % 2 != 0:
            p += am[-1][state]
            state = n[-1][state]
        am.append([am[-1][j] + am[-1][n[-1][j]] for j in xrange(N)])
        n.append([n[-1][n[-1][j]] for j in xrange(N)])
        r /= 2
    
#    while R != 0:
#        if R % 2 != 0:
#            p += amount[state]
#            state = next[state]
#        
#        amount = [amount[i] + amount[next[i]] for i in xrange(N)]
#        next = [next[next[state]] for i in xrange(N)]
#
#        R /= 2

#    for x in xrange(R):
#        p += amount[state]
#        state = next[state]

    return p



def rand():
    n = 0
    while 1:
        r,k = randint(1,10000), randint(1,1000)
        g = [randint(1,1000) for x in xrange(randint(1,500))]
        if solve(r,k,g) != solveslow(r,k,g):
            open("badcase", "w").write("1\n%d %d %d\n%s\n" % (r,k,len(g)," ".join(map(str,g))))
            return
        n += 1
        if n % 10 == 0: sys.stderr.write(str(n) +  " cases correct\n")


def big():
    n = 0
    while 1:
        r,k = randint(10**7,10**8), randint(10**8, 10**9)
        g = [randint(10**6, 10**7) for x in xrange(randint(800,1000))]
        solve(r,k,g)
        n += 1
        if n % 10 == 0: sys.stderr.write(str(n) +  " cases done\n")
        
        
if len(sys.argv) >= 2 and sys.argv[1] == "rand":
    rand()
    sys.exit(1)
if len(sys.argv) >= 2 and sys.argv[1] == "big":
    big()


getline = lambda: [int(x) for x in raw_input().split()]

T = getline()[0]
for i in xrange(T):
    R,k,n = getline()
    groups = getline()
#    sol = solveslow(R,k,groups)
    sol2 = solve(R, k, groups)
#    if sol != sol2:
#        print "Error: ", sol, sol2
    print "Case #%d: %d" % (i+1, sol2)
