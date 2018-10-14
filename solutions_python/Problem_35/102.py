# N = test cases
f = file('sample.in','r')
(N,) = map(int,f.readline().split(' '))

global ALT,M

for TESTCASE in range(1,N+1):
    (H,W) = map(int,f.readline().split(' '))
    ALT = []
    M = []
    FLOW = []
    for y in range(H):
        ALT.append(map(int,f.readline().split(' ')))
        M.append(range(W*y,(W*(1+y))))
        FLOW.append(range(W*y,(W*(1+y))))

    for x in range(W):
        for y in range(H):
            diff = []
            if x > 0: diff.append((ALT[y][x-1],2,(-1,0)))
            if y > 0: diff.append((ALT[y-1][x],1,(0,-1)))
            if x < W-1: diff.append((ALT[y][x+1],3,(+1,0)))
            if y < H-1: diff.append((ALT[y+1][x],4,(0,+1)))

            diff.sort()

            if len(diff)> 0 and diff[0][0] < ALT[y][x]:
                FLOW[y][x] = diff[0][2]
            else:
                FLOW[y][x] = False

    changes = 1
    while changes > 0:
        changes = 0
        for x in range(W):
            for y in range(H):
                d = FLOW[y][x]
                if d == False: continue
                if M[y+d[1]][x+d[0]] != M[y][x]:
                    changes = changes+1
                    m = min(M[y+d[1]][x+d[0]],M[y][x])
                    (M[y+d[1]][x+d[0]],M[y][x]) = (m,m)

    z = {}
    print "Case #"+str(TESTCASE)+":"
    for y in range(H):
        for x in range(W):
            if M[y][x] in z: c = z[M[y][x]]
            else: z[M[y][x]] = c = chr(ord('a')+len(z))
            print c,
        print
