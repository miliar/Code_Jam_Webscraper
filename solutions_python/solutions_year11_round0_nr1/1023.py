import math
import os

h = open('A-large.in', 'r')
out = open('output.txt', 'w')

l = h.readline()
n = int(l); #no. of cases

for case in range(n):
    ocells = [1]
    bcells = [1]
    l = h.readline().split(' ')
    nsteps = int(l[0])
    steps = []

    for i in range(1, nsteps*2, 2):
        bot = l[i]
        if(bot == 'O'):
            steps.append('O')
            ocells.append(int(l[i+1]))
            bcells.append('')
        else:
            steps.append('B')
            bcells.append(int(l[i+1]))
            ocells.append('')

    lasto = ocells[0]
    lastb = bcells[0]
    otimes = []
    btimes = []
    for i in range(1, nsteps + 1):
        if(ocells[i] != ''):
            otimes.insert(i, int(math.fabs(ocells[i] - lasto)) + 1)
            lasto = ocells[i]
        if(bcells[i] != ''):
            btimes.insert(i, int(math.fabs(bcells[i] - lastb)) + 1)
            lastb = bcells[i]

    nosteps = len(otimes)
    nbsteps = len(btimes)

    ans = 0
    oi = 0
    bi = 0

    for x in steps:
        if(x == 'O'):
            ans = ans + otimes[oi]
            if(bi < nbsteps):
                if(btimes[bi] > otimes[oi]):
                    btimes[bi] = btimes[bi] - otimes[oi]
                else:
                    btimes[bi] = 1
            oi = oi + 1
        else:
            ans = ans + btimes[bi]
            if(oi < nosteps):
                if(otimes[oi] > btimes[bi]):
                    otimes[oi] = otimes[oi] - btimes[bi]
                else:
                    otimes[oi] = 1
            bi = bi + 1

    out.write('Case #' + str(case + 1) + ': ' + str(ans))
    if(case != n-1):
        out.write('\n')

h.close()
out.close()
