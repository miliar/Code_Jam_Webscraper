import fileinput
import math
import sys

# A SMALL
    
def cost(N, k):
    return k*(N+1) - (k*(k+1))/2

def getitem(i):
    return (lambda tup: tup[i])

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in xrange(T):
        N, M = map(int, sys.stdin.readline().split(" "))
        tups = []
        normalTotal = 0
        for j in xrange(M):
            o, e, p = map(int, sys.stdin.readline().split(" "))
            normalTotal += cost(N, e-o)*p
            tups.extend([(o,e)]*p)
        tups.sort() #Sort by first index
        os = []
        es = []
        total = 0
        #print tups
        for tup in tups:
            nextGood = 0
            done = False
            for j in xrange(len(es)):
                e = es[j]
                if tup[0] <= e:
                    nextGood = j
                    done = True
                    break
            if not done:
                nextGood = len(es)
            # Add done values
            done_es = es[:nextGood]
            done_os = os[:nextGood]
            for o,e in zip(done_os, done_es):
                total += cost(N, e-o)
            # Include tuple
            es = es[nextGood:]
            os = os[nextGood:]
            os.append(tup[0])
            os.sort(reverse=True)
            es.append(tup[1])
            es.sort()
        # Add the left-over values
        #print "os", os, "es", es
        for o,e in zip(os, es):
            total += cost(N, e-o)

        print "Case #{}: {}".format(i+1, normalTotal-total)
        #print "DEBUG:", normalTotal, total
