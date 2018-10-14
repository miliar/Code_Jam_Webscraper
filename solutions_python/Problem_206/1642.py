import operator

fin = open('A-small-attempt0.in', 'r')
fout = open('A-small-attempt0.out', 'w')

tc = int(fin.readline())
for testcase in range(0, tc):
    temp = fin.readline().split()
    endlength = int(temp[0])
    numhorse = int(temp[1])
    listhorse = list()
    for i in range(0, numhorse):
        temp2 = fin.readline().split()
        listhorse.append( (int(temp2[0]), int(temp2[1])) )
    listhorse.sort(key=operator.itemgetter(0))
    #print(listhorse)
    listtime = list()
    for i in range(0, numhorse-1):
        if listhorse[i+1][1] - listhorse[i][1] != 0:
            listtime.append(((listhorse[i+1][0] - listhorse[i][0]) / (listhorse[i+1][1] - listhorse[i][1]), i, i+1))
    #print(listtime)
    result = 0
    if len(listtime) == 0:
        result = endlength / ((endlength - listhorse[0][0]) / listhorse[0][1])
    else:
        if listtime[0][0] > 0:
            # not meet
            result = endlength / ((endlength - listhorse[0][0]) / listhorse[0][1])
        if listtime[0][0] < 0:
            thistime = abs(listtime[0][0])
            if thistime * listhorse[0][1] + listhorse[0][0] > endlength:
                result = endlength / ((endlength - listhorse[0][0]) / listhorse[0][1])
            else:
                result = endlength / ((endlength - listhorse[1][0]) / listhorse[1][1])
    print("Case #%d: %.6f" %(testcase+1, result))
    fout.write("Case #%d: %.6f\n" %(testcase+1, result))

fin.close()
fout.close()