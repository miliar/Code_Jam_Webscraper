__author__ = 'Levan Kasradze'

import bisect

with open('d.in', 'r') as fin:
    with open('d.out', 'w') as fout:
        t = int(fin.readline())
        for i in range(1, t + 1):
            n = int(fin.readline())
            naomi = fin.readline().strip().split()
            ken = fin.readline().strip().split()
            for j in range(n):
                naomi[j] = float(naomi[j])
                ken[j] = float(ken[j])
            naomi.sort()
            ken.sort()
            kenCopy = ken[:]

            war = 0
            for j in naomi:
                k = bisect.bisect_right(ken, j)
                if k != len(ken):
                    del ken[k]
                else:
                    war += 1
                    del ken[0]

            ken = kenCopy[:]
            deceitfulWar = 0
            for j in ken:
                k = bisect.bisect_right(naomi, j)
                if k != len(naomi):
                    deceitfulWar += 1
                    del naomi[k]
                else:
                    del naomi[0]

            fout.write('Case #' + str(i) + ': ' + str(deceitfulWar) + ' ' + str(war) + '\n')