from sys import stdin

for case in range(1, int(stdin.readline()) + 1):
    inp = stdin.readline().split()
    n = int(inp[0])
    rob = []
    pos = []
    for i in range(1, 2*n, 2):
        rob.append(inp[i])
        pos.append(int(inp[i+1]))

    rpos = {'O': 1, 'B': 1}
    t = 0
    t1 = 0
    i = 0
    while True:
        delta = abs(rpos[rob[i]] - pos[i]) + 1
        t += delta
        t1 += delta
        rpos[rob[i]] = pos[i]

        i += 1
        if i == n: break
        if rob[i] != rob[i-1]:
            abs_step = abs(rpos[rob[i]] - pos[i])
            sign_step = -1 if rpos[rob[i]] > pos[i] else 1
            rpos[rob[i]] = rpos[rob[i]] + sign_step*t1 if t1 < abs_step else pos[i]
            t1 = 0

    print "Case #%d: %d" % (case, t)
