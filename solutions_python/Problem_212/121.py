import sys, collections

inputfile = file(sys.argv[1])
outputfile = file(sys.argv[2], 'w')

for case in xrange(int(inputfile.readline())):
    N, P = map(int, inputfile.readline().split())
    groups = map(int, inputfile.readline().split())
    modulos = [0 for _ in xrange(P)]
    ngroups = []
    onlyfresh = 0
    for g in groups:
        if g % P == 0:
            onlyfresh += 1
        else:
            modulos[g%P] += 1
    #for i in xrange(1, P):
    #    if (P % 2 == 1):
    if P == 2:
        onlyfresh += modulos[1] / 2
        if modulos[1] % 2 != 0:
            onlyfresh += 1
    elif P == 3:
        matching = min(modulos[1], modulos[2])
        modulos[1] -= matching
        modulos[2] -= matching
        onlyfresh += matching
        onlyfresh += modulos[1] / 3
        onlyfresh += modulos[2] / 3
        if modulos[1] % 3 != 0:
            onlyfresh += 1
        if modulos[2] % 3 != 0:
            onlyfresh += 1
    outputfile.write('Case #{}: {}\n'.format(case+1, onlyfresh))

outputfile.close()