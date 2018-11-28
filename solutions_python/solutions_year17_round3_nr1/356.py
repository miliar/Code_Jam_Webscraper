import operator
import math
fin = open('A-large.in', 'r')
fout = open('output.out', 'w')
tcs = int(fin.readline())
for tc in range(0, tcs):
    PI = math.pi
    inptemp = fin.readline().split(' ')
    n = int(inptemp[0])
    k = int(inptemp[1])
    cakes = list()
    for i in range(0, n):
        inptemp2 = fin.readline().split(' ')
        r = int(inptemp2[0])
        h = int(inptemp2[1])
        cakes.append([r, h])

    cakes.sort(key=operator.itemgetter(0), reverse=True)
    maxrad = 0.0
    for i in range(0, n-k+1):
        syrup = list()
        curmax = 0.0
        syrup.append(PI * cakes[i][0] * cakes[i][0] + 2 * PI * cakes[i][0] * cakes[i][1])
        for j in range(i+1, i+k):
            syrup.append(2 * PI * cakes[j][0] * cakes[j][1])
        curmax = sum(syrup)
        for j in range(i+k, n):
            curr = 2 * PI * cakes[j][0] * cakes[j][1]
            if curmax - min(syrup) + curr > curmax:
                syrup.pop(syrup.index(min(syrup)))
                syrup.append(curr)

        if(sum(syrup) > maxrad):
            maxrad = sum(syrup)
    print("Case #%d: %.9f" %(tc+1, maxrad))
    fout.write("Case #%d: %.9f\n" %(tc+1, maxrad))
fin.close()
fout.close()
