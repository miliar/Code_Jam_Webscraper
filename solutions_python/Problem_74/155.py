from sys import stdin
T = int(stdin.readline())
for t in range(1,T+1):
    input = stdin.readline().split()[1:]
    N = len(input)/2
    players = []
    actions = []
    for n in range(N):
        players.append(input[2*n])
        actions.append(int(input[2*n+1]))
    b, o = 1, 1
    players.append('B')
    players.append('O')
    actions.append(1)
    actions.append(1)
    time = 0
    for n in range(N):
        if players[n]=='B':
            bgoal = actions[n]
            m=n
            while players[m]!='O': m+=1
            ogoal = actions[m]
            while b != bgoal:
                time += 1
                if b < bgoal: b += 1
                if b > bgoal: b -= 1
                if o < ogoal: o += 1
                if o > ogoal: o -= 1
            time += 1
            if o < ogoal: o += 1
            if o > ogoal: o -= 1
        else:
            ogoal = actions[n]
            m=n
            while players[m]!='B': m+=1
            bgoal = actions[m]
            while o != ogoal:
                time += 1
                if b < bgoal: b += 1
                if b > bgoal: b -= 1
                if o < ogoal: o += 1
                if o > ogoal: o -= 1
            time += 1
            if b < bgoal: b += 1
            if b > bgoal: b -= 1
    print "Case #%d: %d" % (t,time)
