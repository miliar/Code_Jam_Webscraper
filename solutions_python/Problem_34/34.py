import sys, re

def lin(): return sys.stdin.readline()

(L, D, N) = [int(s) for s in lin().split()]
#print L, D, N

words = [lin() for i in range(D)]
got   = [lin() for i in range(N)]
for i in range(N):
    s = got[i]
    poss = 0
    for w in words:
        sr = s.replace('(','[').replace(')',']')
        if re.match(sr, w):
            poss += 1
        else:
            #print "%s does not match %s" % (s, wr)
            pass
    print "Case #%d: %d" % (i+1, poss)
