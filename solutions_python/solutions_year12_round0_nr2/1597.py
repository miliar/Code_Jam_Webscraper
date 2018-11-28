filesDir = '/home/alberto/py/'
inFile = 'B-large.in'

def writeToFile(filename,content):
    f = open(filesDir + filename,'w')
    f.write(content)
    f.close()

def readFileLines(filename):
    f = open(filesDir + filename,'r')
    t = f.readlines()
    t.pop(0)
    g = []
    for l in t:
        g.append(l.replace('\n',''))
    return g

def processArray(array):
    output = ''
    curCase = 1
    for line in array:
        curLine = 'Case #' + str(curCase) + ': ' + processLine(line) + '\n'
        output += curLine
        curCase += 1
    return output

def procedure():
    outFile = inFile.replace('.in','.out')
    array = readFileLines(inFile)
    processedArray = processArray(array)
    writeToFile(outFile,processedArray)

def getValues(input):
    array = input.split(' ')
    totals = []
    for i in array[3:len(array)]:
        totals.append(int(i))
    totals.sort()
    totals.reverse()
    output = [int(array[0]), int(array[1]), int(array[2]), totals]
    return output

def getMaxs(input):
    output = []
    for i in input:
        v = i/3
        if (i % 3) > 0:
            v += 1
        output.append(v)
    return output

def getOverP(t,maxs,p,S):
    count = 0
    totS = S
    for a in xrange(len(maxs)):
        i = maxs[a]
        j = t[a]
        if (i >= 2) | (j >= p):
            if (i >= p):
                count += 1
            elif (i <= 28):
                if (totS > 0) & ((j % 3) != 1):
                    totS -= 1
                    i = i + 1
                    if (i >= p):
                        count += 1
    return count
            
def processLine(input):
    [N, S, p, t] = getValues(input)
    maxs = getMaxs(t)
    left = getOverP(t,maxs,p,S)
    output = str(left)
    return output

procedure()


