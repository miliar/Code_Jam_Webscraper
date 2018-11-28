import timeit
ONE = 2
I = 3
J = 5
K = 7
conv = {'i' : I, 'j' : J, 'k' : K, '1' : ONE} # 1 not needed

table = [0, 0, 0, 0, 2, 0, 3, 0, 0, -2, 5, 0, 0, 0, 7, -7, 0, 0, 0, 0, 0, 5, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2]


def parseInput(text):
    cases = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if i == 0 or i % 2 != 1:
            continue
        numOfChars, times = line.split(' ')
        string = lines[i+1]

        cases.append((string, int(times)))
    return cases

def getOutput(solved):
    lines = []
    for i, solvedCase in enumerate(solved):
        lines.append("Case #%d: %s" % (i + 1, "YES" if solvedCase else "NO"))
    return '\n'.join(lines)

def generateOutput(filename, outFile = None):
    cases = getCases(filename)
    solvedCases = [naiveSolution(*case) for case in cases]
    output = getOutput(solvedCases)
    if outFile == None:
        outFile = filename[:-2] + "out"
    with open(outFile, "w") as h:
        h.write(output)

    
def getCases(filename):
    with open(filename) as h:
        data = h.read()
    return parseInput(data)





def mult(a, b):
    global table
    #print(disp(a), disp(b))
    minusSign = 1
    if a < 0:
        minusSign *= -1
        a *= -1
    if b < 0:
        minusSign *= -1
        b *= -1

    #return table[a*b] * minusSign

    
    if a == ONE:
        return minusSign*b
    if b == ONE:
        return minusSign*a
    if a == b:
        return -ONE*minusSign
    if a == K:
        if b == J:
            return -I*minusSign
        if b == I:
            return J*minusSign
    if a == J and b == I:
        return -K*minusSign
    return -mult(b, a)*minusSign
    


def canCreate(prefix, string, times, sign):
    # Can we create sign from (prefix + string*times)? returns indexes
    pass
    
def oneErate(string, times):
    soFar = ONE
    ones = [0]
    string = [conv[c] for c in list(string*times)]
    parts = []
    for i, c in enumerate(string):
        soFar = mult(soFar, c)
        if soFar == ONE:
            parts.append(''.join([str(a) for a in string[ones[len(ones) - 1]:i + 1]]))
            ones.append(i)
    return ones, parts
            
def naiveSolution(string, times = 1):
    global conv
    #if times > 16:
    #    times = 16 + times % 4
    string = [conv[c] for c in list(string*times)]
    
    splitAtI = []
    soFar = ONE
    for i, c in enumerate(string):
        soFar = mult(soFar, c)
        if soFar == I:
            splitAtI.append(i + 1)

    if len(splitAtI) == 0:
        return False


    splitAtK = []
    soFar = ONE
    #print (string)
    #print([disp(c) + ":" + str(i) for i, c in reversed(list(enumerate(string)))])
    for i, c in reversed(list(enumerate(string))):
        soFar = mult(c, soFar)
        #print("%s*soFar: %s" % (disp(string[i]), disp(soFar)))
        if soFar == K:
            splitAtK.append(i)

    if len(splitAtK) == 0:
        return False
    #print(splitAtI, splitAtK)
    startAt = min(splitAtI)
    finishAt = max(splitAtK)
    soFar = ONE
    lastI = startAt
    for i in range(startAt, finishAt):
        #print("from a%d*...*a%d, we got %s" % (startAt, i, disp(soFar)))
        soFar = mult(soFar, string[i])
        #print("soFar*%s: %s" % (disp(string[i]), disp(soFar)))
        if soFar == 1:
            lastI = i
        if soFar == J and (i + 1) in splitAtK:
            #print(lastI, i+1)
            return True
    return False
    
    

def myPow(tkn, times):
    mod4 = times % 4
    if times == 0:
        return ONE
    elif times == 1:
        return tkn
    elif times == 2:
        return -ONE
    elif times == 3:
        return -tkn
def evalString(string):
    string = [conv[c] for c in list(string)]
    soFar = ONE
    for c in string:
        soFar = mult(soFar, c)
    return disp(soFar)

def rotate(l,n):
    return l[n:] + l[:n]
            
def disp(a):
    minus = False
    if a < 0:
        minus = True
        a *= -1
    if a == I:
        s = 'i'
    elif a == J:
        s = 'j'
    elif a == K:
        s = 'k'
    elif a == ONE:
        s = '1'
    
    return ("-" if minus else "") + s

a = 4
samp= "i" * a + "j" * a + "k" * a
