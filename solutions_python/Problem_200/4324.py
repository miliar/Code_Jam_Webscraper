f = open('B-large-attempt.in', 'r')
w = open('B-large-attempt.out', 'w+')
line = f.readline().strip()
t = int(line)
for k in xrange(1, t+1):
    inStr = str(f.readline().strip())
    numArr = []
    numLen = len(inStr)
    for digit in inStr:
        numArr.append(int(digit))
    #verify tidiness
    outputArr = []
    stuckIdx = -1
    for i in xrange(0, numLen):
        outputArr.append(int(numArr[i]))
    for i in xrange(1, numLen):
        curIdx = numLen-i
        curD = outputArr[curIdx]
        curP = outputArr[curIdx-1]
        if (curD<curP):
            stuckIdx = curIdx
            if (curP == 0):
                outputArr[curIdx-1] = 9
                #Cascade
                while (curIdx-2>=0 and outputArr[curIdx-2] == 0):
                    curIdx = curIdx-2
                    outputArr[curIdx] = 9
                outputArr[curIdx-1] = outputArr[curIdx-1]-1
            else:
                outputArr[curIdx-1] = outputArr[curIdx-1]-1
    if (stuckIdx > -1):
        for i in range(stuckIdx, numLen):
            outputArr[i] = 9
    outputStr = ""
    start = False
    for i in range(0, numLen):
        if (not start):
            if (outputArr[i] != 0):
                start = True
        if (start):
            outputStr += str(outputArr[i])
    print "Case #{0}: {1}".format(k, outputStr)
    w.write("Case #{0}: {1}\n".format(k, outputStr))
f.close()
w.close()
