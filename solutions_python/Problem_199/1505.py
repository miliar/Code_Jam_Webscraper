import sys
from collections import deque

T = sys.stdin.readline()
case = 0
for line in sys.stdin:
    case += 1
    [S, K] = line.split(" ")
    flip = deque([False]*int(K))
    r = len(S)
    f = 0
    for c in S:
        #print flip, r, K
        if (flip[0]) != (c == '-'):
            if r < int(K):
                break
            flip2 = deque()
            for i in xrange(int(K)):
                flip2.append(not flip[i])
            flip = flip2
            f += 1
        flip.popleft()
        flip.append(False)
        r -= 1
    if r > 0:
        print "Case #"+str(case)+": IMPOSSIBLE"
    else:
        print "Case #"+str(case)+": " + str(f)
