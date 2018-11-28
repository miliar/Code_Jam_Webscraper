import collections
import heapq

T = input()

for t in xrange(T):
    L, X = map(int, map(int, raw_input().split()))
    
    S = raw_input()
    
    goal = 'ijz'
    goal_index = 0
    
    cur = 1
    sign = 1
    for c in S * X:
        if cur == 1:
            cur = c
        elif cur == c:
            sign = -sign
            cur = 1
        elif cur == 'i' and c == 'j':
            cur = 'k'
        elif cur == 'i' and c == 'k':
            cur = 'j'
            sign = -sign
        elif cur == 'j' and c == 'i':
            cur = 'k'
            sign = -sign
        elif cur == 'j' and c == 'k':
            cur = 'i'
        elif cur == 'k' and c == 'i':
            cur = 'j'
        elif cur == 'k' and c == 'j':
            cur = 'i'
            sign = -sign
        
        if sign == 1 and cur == goal[goal_index]:
            goal_index += 1
            cur = 1
    if goal_index == 2 and cur == 'k' and sign == 1:
        print 'CASE #{}: {}'.format(t + 1, 'YES')
    else:
        print 'CASE #{}: {}'.format(t + 1, 'NO')
