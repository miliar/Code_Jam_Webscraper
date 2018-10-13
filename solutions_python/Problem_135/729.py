import sys
from math import sqrt, floor
f = open(sys.argv[1], 'r')

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print "Case #" + str(i) + ":",
    
    # read test case
    fstAns = int(f.readline())
    for j in range(1, 5) :
        tmp = f.readline()
        if j == fstAns :
            fstRowStr = tmp.split(' ')
            fstRow = []
            for col in fstRowStr :
                fstRow.append(int(col))

    sndAns = int(f.readline())
    for j in range(1, 5) :
        tmp = f.readline()
        if j == sndAns :
            sndRowStr = tmp.split(' ')
            sndRow = []
            for col in sndRowStr :
                sndRow.append(int(col))
    
    # check test case for row
    firstFind = False
    secondFind = False
    anser = 0
    for i in fstRow :
        for j in sndRow :
            if i == j :
                if firstFind :
                    secondFind = True
                    break
                else :
                    firstFind = True
                    answer = i
                    break
        if secondFind :
            break

    if secondFind :
        print "Bad magician!"
    elif firstFind :
        print answer
    else :
        print "Volunteer cheated!"
