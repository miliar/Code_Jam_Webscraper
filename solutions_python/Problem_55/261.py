lines = open('C-small.in', 'r').readlines()
out = open('C-small.out', 'w')

from collections import deque

T = int(lines[0])
t = 1

while t <= T:

    line = [lines[t * 2 - 1], lines[t * 2]]

    st = i = 0
    while line[0][i] != ' ' : i = i + 1
    R = int(line[0][st:i])
    
    st = i = i + 1
    while line[0][i] != ' ' : i = i + 1
    k = int(line[0][st:i])

    st = i = i + 1
    while line[0][i] != '\n' : i = i + 1
    N = int(line[0][st:i])

    g = deque()

    st = i = 0
    for x in xrange(N):
        while True:
            if line[1][i] == ' ' or line[1][i] == '\n':
                g.append(int(line[1][st:i]))
                st = i = i + 1
                break
            i = i + 1

    ans = 0
    for x in xrange(R):
        Sum = 0
        temp = []
        while len(g) != 0:
            if Sum + g[0] <= k:
                temp.append(g[0])
                Sum += g.popleft()
            else : break
        ans += Sum
        g.extend(temp)

    out.write('Case #%d: ' % t)
    out.write('%d\n' % ans)
    
    #print R, k, N
    #for x in g: print x,
    #print

    t = t + 1
