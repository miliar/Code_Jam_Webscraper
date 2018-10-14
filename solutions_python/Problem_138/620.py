infile = open('in')
outfile = open('out','w')

n = int(infile.readline())
for testcase in range(n):
    #print()
    n = int(infile.readline())
    naomi = [float(i) for i in infile.readline().split()]
    ken = [float(i) for i in infile.readline().split()]
    naomi.sort()
    ken.sort()
    print(naomi,'\n',ken)
    total = 0

    nc = naomi[:]
    kc = ken[:]
    for i in range(n):
        choose = nc[i]
        choose2 = kc[0]
        for j in range(len(kc)):
            if kc[j] > choose:
                choose2 = kc[j]
                break
        if choose > choose2:
            total += 1
        kc.remove(choose2)
    total2 = 0

    nc = naomi[:]
    kc = ken[:]
    for i in range(n):
        choose = nc[n-i-1]
        choose2 = kc[0]
        for j in range(len(kc)):
            if kc[j] > choose:
                choose2 = kc[j]
                break
        if choose > choose2:
            total2 += 1
        kc.remove(choose2)
    total = max(total,total2)

    dtotal = 0
    nc = naomi[:]
    kc = ken[:]
    for i in range(n):
        choose = nc[i]
        if choose < kc[0]:
            choose2 = kc[len(kc)-1]
        else:
            choose2 = kc[0]
        if choose > choose2:
            dtotal += 1
        kc.remove(choose2)

    outfile.write('Case #' + str(testcase+1) + ': ' + str(dtotal) + ' ' + str(total) + '\n')
