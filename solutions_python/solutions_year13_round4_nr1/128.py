tsum = [0, 1]
for i in range(2, 101):
    tsum.append(tsum[i - 1] + i)

fi = open("A-small-attempt0.in", 'r')
fo = open("A-small.out", 'w')

tcase = int(fi.readline())
for icase in range(tcase):
    line = fi.readline().split()
    n = int(line[0])
    m = int(line[1])

    origlen = 0
    plen = 0
    
    b = [0 for i in range(102)]
    for i in range(m):
        line = fi.readline().split()
        o = int(line[0])
        e = int(line[1])
        p = int(line[2])
        for j in range(p):
            origlen += tsum[e - o]
        for j in range(o, e):
            b[j] += p

    while True:
        i = 0
        while i <= n and b[i] == 0:
            i += 1
        if i > n:
            break

        j = i
        while j < n and b[j + 1] <> 0:
            j += 1

        plen += tsum[j - i + 1]
        for ii in range(i, j + 1):
            b[ii] -= 1

    fo.write("Case #%d: %d\n" %(icase + 1, plen - origlen))

fi.close()
fo.close()
