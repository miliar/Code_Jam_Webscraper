#!/usr/bin/python2
from collections import deque
for t in range(int(raw_input())):
    inp = raw_input().split()
    N, inp = inp[0], inp[1:]
    ans = 0

    order = deque()
    for i in range(0, len(inp), 2):
        order.append((1 if inp[i+0]=='O' else 0, int(inp[i+1])))

    pos = [1, 1]
    lastMovedAt = [0,0]
    time =0

    while order:
        cur = order.popleft()
        d = abs(pos[cur[0]] - cur[1])
        extra=(time-lastMovedAt[cur[0]])
        #If we have moved into position already just press the button
        if extra > d:
            time += 1
        else:
            time += d-extra+1

        pos[cur[0]] = cur[1]
        lastMovedAt[cur[0]] = time


    print 'Case #%d: %d' % (t+1, time)
