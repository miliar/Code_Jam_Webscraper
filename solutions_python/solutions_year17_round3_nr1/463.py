import math
TC = int(raw_input())
for i in range(0,TC):
    rad = []
    side = []
    input1 = raw_input()
    input1 = input1.split()
    #print input1
    k = int(input1[0])
    n = int(input1[1])
    for j in range(0,k):
        input2 = raw_input().split()
        a = int(input2[0])
        b = int(input2[1])
        rad.append((a, j, b*a))
        side.append((b*a, a, 0, j))
    maximum = 0
    sortedbyrad = sorted(rad, key=lambda s: s[0], reverse=True)
    sortedbyside = sorted(side, key=lambda s: s[0], reverse=True)
    #print sortedbyrad
    #print sortedbyside
    for j in sortedbyrad:
        cumulative = j[2]
        count = 1
        for ki in sortedbyside:
            if count == n:
                break
            if ki[3] == j[1]:
                continue
            if ki[1] > j[0]:
                sortedbyside.remove(ki)
                continue
            cumulative += ki[0]
            count += 1
        summation = cumulative * 2 * math.pi + math.pi * j[0] * j[0]
        if summation > maximum:
            maximum = summation
    print ("Case #" + str(i+1) + ": %.9f" % maximum)
