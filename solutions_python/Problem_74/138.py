T = input()

for case in range(T):
    l = raw_input().split()
    points = {'O':[], 'B':[]}
    turn = []
    for i in range(int(l[0])):
        turn.append(l[2*i+1])
        points[turn[i]].append(int(l[2*i+2]))
    points['O'].append(0)
    points['B'].append(0)

    cp = {'O':1, 'B':1}

    ans = 0
    for a in turn:
        b = 'O' if a == 'B' else 'B'
        p = points[a].pop(0)
        time = abs(p - cp[a]) + 1
        cp[a] = p
        ans += time
        if abs(points[b][0] - cp[b]) <= time:
            cp[b] = points[b][0]
        else:
            cp[b] = cp[b] + time if (points[b][0] > cp[b]) else cp[b] - time
    print "Case #%i: %i" % ((case + 1), ans)
