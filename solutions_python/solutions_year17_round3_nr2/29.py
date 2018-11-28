def parent(Atimes,Btimes):
    a = len(Atimes)
    b = len(Btimes)
    tot = []
    atime = 0
    btime = 0
    for i in range(a):
        tot.append([Atimes[i][0],Atimes[i][1],'A'])
        atime += Atimes[i][1] - Atimes[i][0]
    for i in range(b):
        tot.append([Btimes[i][0],Btimes[i][1],'B'])
        btime += Btimes[i][1] - Btimes[i][0]
    tot = sorted(tot, key = lambda x: x[0])
    comps = []
    atime = 720 - atime
    btime = 720 - btime
    for i in range(len(tot)-1):
        if tot[i][2] == tot[i+1][2]:
            if tot[i][2] == 'A':
                comps.append([tot[i+1][0]-tot[i][1],'A'])
            else:
                comps.append([tot[i+1][0]-tot[i][1],'B'])
    if tot[0][2] == tot[len(tot)-1][2]:
        if tot[0][2] == 'A':
            comps.append([tot[0][0]+1440-tot[len(tot)-1][1],'A'])
        else:
            comps.append([tot[0][0]+1440-tot[len(tot)-1][1],'B'])

    adds = len(comps)
    comps = sorted(comps, key = lambda x: x[0])

    #print tot
    #print len(tot)
    #print comps
    for i in range(len(comps)):
        if comps[i][1] == 'A':
            if comps[i][0] <= atime:
                adds -= 2
                atime -= comps[i][0]
        else:
            if comps[i][0] <= btime:
                adds -= 2
                btime -= comps[i][0]
    return len(tot) + adds





t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
    a, b = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    Atimes = [[int(s) for s in raw_input().split(" ")] for line in range(a)]
    Btimes = [[int(s) for s in raw_input().split(" ")] for line in range(b)]
    print "Case #{}: {}".format(i, parent(Atimes, Btimes))