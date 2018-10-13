from collections import deque
from copy import copy

def future_cost(motes, A, d):
    cost = 99999
    mmotes = copy(motes)
    #print A, motes
    while len(mmotes) > 0 and mmotes[0] < A:
        A += mmotes.popleft()
        #print A, mmotes
    if not len(mmotes):
        return 0
    # A-1 is largest absorbable
    #print 'before motes', mmotes
    if A > 1:
        #print 'hit add'
        newmote = 1 + future_cost(mmotes, 2*A-1, d+1)
        cost = min(cost, newmote)
        #print 'add,', cost
    # remove
    #print 'midway motes', mmotes
    if len(mmotes) > 0:
        #print 'hit remove'
        mmotes.pop()
        remove = 1 + future_cost(mmotes, A, d+1)
        cost = min(cost, remove)
        #print 'remove,', cost
    return cost

for case in range(1,input()+1):
    A, N = map(int, raw_input().split())
    motes = map(int, raw_input().split())
    motes.sort()
    motes = deque(motes)
    mincost = future_cost(motes, A, 0)
    print('Case #{0}: {1}'.format(case, mincost))
