import sys
import collections

T = int(raw_input())
for t in xrange(1, T + 1):
    N, X = map(int, raw_input().split())
    S = map(int, raw_input().split())
    
    S.sort()
    head = 0
    tail = len(S) -1
    
    result = 0
    while head <= tail:
        if S[head] + S[tail] <= X:
            head += 1
            tail -= 1
            result += 1
        else:
            tail -= 1
            result += 1
    
    print "Case #{0}: {1}".format(t, result)

