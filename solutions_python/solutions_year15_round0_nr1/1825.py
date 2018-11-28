f = open('input-large')
cases = int(f.readline())
case = 0
for line in f:
    case += 1
    cases = line.split()
    sMax = int(cases[0])
    rest = list(cases[1])
    rest = [int(x) for x in rest]
    count = 0
    index = 0
    numFr = 0
    tmpFr = 0
    while count < sMax: 
        if count < index:
            tmpFr = index - count
            if count + tmpFr < sMax:
                numFr += tmpFr
                count = count + tmpFr
            else:
                numFr += sMax - count
                break
        count += rest[index]
        index += 1
    print "Case #"+str(case) + ": " + str(numFr)
