

def subCount(string, sub = "welcome to code jam"):
    strList = []
    posMap = makePosMap(sub)

    totalStrs = 0L
    
    for i in range(0,len(string)):
        char = string[i]
        strList.append({})
        if not char in posMap: continue
        posList = posMap[char]
        for posIndex in posList:
            numPos = 0
            if posIndex == 0:
                strList[i][0] = 1
                continue
            for j in range(0,i):
                if posIndex-1 in strList[j]:
                    numPos += strList[j][posIndex-1]
            if numPos > 0:
                strList[i][posIndex] = numPos
                if posIndex == len(sub)-1:
                    totalStrs += numPos
    return totalStrs
                

def makePosMap(string = "welcome to code jam"):
    posMap = {}
    for i in range(0,len(string)):
        if string[i] in posMap:
            posMap[string[i]].append(i)
        else:
            posMap[string[i]] = [i]
    return posMap

f = open('intext.txt')
of = open('out2.txt','w')
numLines = int(f.readline()[:-1])
for i in range(0,numLines):
    line = f.readline()[:-1]
    numWords = subCount(line)
    words4digits = ("0000" + str(numWords))[-4:]
    of.write("Case #%d: %s\n" % (i+1,words4digits))
    print "Case #%d: %s" % (i+1,words4digits)
of.flush()
of.close()
f.close()
