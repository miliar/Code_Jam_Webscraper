fin = open('1.in', 'r')
fout = open('1.out', 'w')
t = int(fin.readline()[:-1])
for tests in range(t):
    smax, ks = fin.readline()[:-1].split()
    smax = int(smax)
    ks = list(map(int, list(ks)))
    need = 0
    stand = 0
    for k in range(smax+1):
        if stand < k:
            need += 1
            stand += 1
        stand += ks[k]
    output = 'Case #{0}: {1}'.format(tests+1, need)
    fout.write(output+'\n')
fout.close()
fin.close()
