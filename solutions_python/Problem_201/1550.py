import sys
import math
import heapq

def h(N, K):
    spaces = [0]*(N+1)
    spaces[N] = 1
    #heapq.heappush(spaces, -N)
    for head in xrange(N, 0, -1):
        #print head, K, spaces
        if spaces[head] == 0: continue
        l = long(math.ceil((head - 1) / 2.))
        s = long(math.floor((head - 1) / 2.))
        #print l, s
        if spaces[head] >= K: return l, s
        spaces[l] += spaces[head]
        spaces[s] += spaces[head]
        K -= spaces[head]
        #for k in xrange(K):
        #if len(spaces) == 0: return 0, 0
        #head = -spaces[0] - 1
        #l = long(math.ceil(head / 2.))
        #s = long(math.floor(head / 2.))
        #if l > 0: heapq.heapreplace(spaces, -l)
        #else: heapq.heappop(spaces)
        #if s > 0: heapq.heappush(spaces, -s)
    return l, s

T = sys.stdin.readline()
case = 0
for line in sys.stdin:
    case += 1
    N, K = map(long, line.split(" "))
    l, s = h(N, K)
    print "Case #"+str(case)+": " + str(l) + " " + str(s)
