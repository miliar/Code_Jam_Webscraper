data = open('C.txt').readlines()

T = int(data.pop(0))

for i in range(T):
    (R, k, N) = map(int, data.pop(0).split(' '))
    g = map(int, data.pop(0).split(' '))
    money = 0
    for j in range(R):
        free = k
        for l in range(N):
            if free >= g[0]:
                money += g[0]
                free -= g[0]
                g.append(g.pop(0))

    print 'Case #%d: %d' % (i+1, money)