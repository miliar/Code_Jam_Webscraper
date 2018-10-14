from heapq import *
from collections import deque
infile = open("B-small-attempt2.in")
outfile = open("B-small-attempt2.out", 'w')

def nextmin(state):
    nextstates = []
    v1 = ([],state[1]+1)
    v1 = ([x+1 for x in state[0] if x != 0], state[1]+1)
    heapify(v1[0])
    #for x in state[0]:
    #    if x!= 0:
    #        heappush(v1[0], x+1)
    most = -heappop(state[0])
    for i in range(1, (most/2)+1):
        nextstates.append((state[0][:], state[1]+1))
        heappush(nextstates[-1][0], -i)
        heappush(nextstates[-1][0], -(most-i))
    nextstates.append(v1)
    return nextstates
    
def BFS(state):
    queue = deque()
    queue.append(state)
    while queue:
        state = queue.popleft()
        if set(state[0]) == set([0]):
            return state[1]
        for s in nextmin(state):
            queue.append(s)

cases = int(infile.readline().strip())

for i in range(cases):
    infile.readline()
    diners = map(int, infile.readline().strip().split())
    diners = [-x for x in diners]
    heapify(diners)
    result = "Case #%d: %d" %(i+1, BFS((diners, 0)))
    #print result
    outfile.write(result + '\n')

infile.close()
outfile.close()
