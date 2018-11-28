k = 0
for i in range(int(raw_input())):
    inp = raw_input()
    maxshy = int(inp.split(" ")[0])
    row = map(int, list(inp.split(" ")[1]))
    numClapping = 0
    numAdded = 0
    shyness = 0
    for numshy in row:
        if shyness == 0:
            numClapping += numshy
        else:
            if numshy != 0 and numClapping < shyness:
                numAdded += shyness - numClapping
                numClapping += numAdded
            numClapping += numshy
        shyness += 1
    k += 1
    print 'Case #'+str(k)+': '+str(numAdded)