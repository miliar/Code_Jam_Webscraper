import copy
import itertools

fin = open('B-large.in', 'r') 
T = int(fin.readline().rstrip())
caseNo = 0
fout = open('B-large.out', 'w')
for i in range(T):
    l = fin.readline().rstrip().split()
    N, P = int(l[0]), int(l[1])
    P1 = P

    if P == 2 ** N:
        r1 = 2 ** N - 1
    else:
        x = 2 ** (N - 1)
        r1 = 0
        i = 1
        while P > x:
            i *= 2
            r1 += i
            P -= x
            x //= 2

    P = P1
    r2 = 0
    i = 1
    x = 2 ** (N - 1)
    P = 2 ** N - P
    while P > 0:
        r2 = r2 + i
        i *= 2
        print(P, x)
        P -= x
        x //= 2
    caseNo += 1
    fout.write('Case #' + str(caseNo) + ': ' + str(r1) + ' ' + str(2 ** N - 1 - r2)  + '\n')

fin.close()
fout.close()

