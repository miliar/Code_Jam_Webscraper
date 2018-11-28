import math,sys

fin = open('B-large.in','r')
fout = open('pancakesLarge.out','w')

cases = int(fin.readline().strip())

a = 1

while a <= cases:
    numPlates = int(fin.readline().strip())

    plates = map(int, fin.readline().strip().split(' '))
    plates = sorted(plates,reverse=True)

    maxTime = plates[0]
    minTime = sys.maxsize

    for i in range(1,maxTime+1):
        toMove = 0

        for x in plates:

            if x <= i:
                break

            toMove += math.ceil(x/i) - 1

        if toMove + i < minTime:
            minTime = toMove + i

    fout.write('Case #%d: %d\n' % (a, minTime))

    a+=1
fin.close()
fout.close()

