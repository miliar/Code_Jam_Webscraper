def poss(zmin, zmax):
    z = zmin
    count = 0
    while(z <= zmax):
        zwp = []
        cz = str(z)
        l = len(cz)
        for p in range(1,l):
            nz = cz[l-p:] + cz[:l-p]
            if nz.startswith('0') or z == int(nz):
                continue
            if zmin <= z <= int(nz) <= zmax:
                m = str(z) + ':' + nz
                if m not in zwp:
                    zwp.append(m)
                    count += 1
        z += 1
    return count

fin = open('C:\\temp\\C-large.in')
fout = open('C:\\temp\\C-large.out','w')
cases = int(fin.readline())
for case in range(cases):
    line = fin.readline().strip('"\n')
    minmax = line.split(' ')
    fout.write('Case #' + str(case+1) + ': ' + str(poss(int(minmax[0]),int(minmax[1]))) + '\n')