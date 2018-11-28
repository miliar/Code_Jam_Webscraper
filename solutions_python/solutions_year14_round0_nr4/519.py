# Google Code Jam 2014 Qualifying question D

infile = open('D-large.in', 'r')
outfile = open('D_large.txt', 'w')

n = infile.readline()

for case in range(1, int(n) + 1):
    num = infile.readline()
    nBlocks = infile.readline()
    kBlocks = infile.readline()
    nBlocks = nBlocks.split(' ')
    nBlocks[-1] = nBlocks[-1][:-1]
    kBlocks = kBlocks.split(' ')
    kBlocks[-1] = kBlocks[-1][:-1]
    nBlocks.sort()
    kBlocks.sort()
    nBlocks1 = nBlocks
    kBlocks1 = kBlocks
    war = 0    
    for block in nBlocks:
        greater = False
        i = 0
        while i < len(kBlocks) and not greater:
            if kBlocks[i] > block:
                greater = True
                kBlocks = kBlocks[:i] + kBlocks[i+1:]
            else:
                i += 1
        if not greater:
            war += 1
    dWar = 0
    n = nBlocks1[0]
    k = kBlocks1[-1]
    if n > k:
        dWar = len(nBlocks1)
    else:
        while nBlocks1 != []:
            if nBlocks1[0] > kBlocks1[0]:
                dWar += 1
                nBlocks1, kBlocks1 = nBlocks1[1:], kBlocks1[1:]
            else:
                nBlocks1, kBlocks1 = nBlocks1[1:], kBlocks1[:-1]

    output = 'Case #{0}: {1} {2}'.format(str(case), str(dWar), str(war))
    outfile.write(output + '\n')

infile.close()
outfile.close()
