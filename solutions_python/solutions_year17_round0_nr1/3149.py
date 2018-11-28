import numpy as np

def flip(input, posn, k):
    myOut = list(input)
    for i in range(posn,posn+k):
        if myOut[i] == '-':
            myOut[i] = '+'
        else:
            myOut[i] = '-'
    return ''.join(myOut)

def config2bin(input):
    mySum = 0
    s = len(input)
    for i in range(0,s):
        if (input[i] == '+'):
            mySum += (2 ** i)
    return mySum

def solveIt(initStr, k):
    s = len(initStr)
    doneStr = '+' * s
    v = np.zeros(2 ** s)
    q = [(initStr, 0)]
    v[config2bin(initStr)] = 1
    myD = -1
    while (len(q) != 0):
        curr, d = q.pop(0)
        if curr == doneStr:
            myD = d
            break
        for i in range(0, s-k+1):
            myElem = flip(curr, i, k)
            myBin = config2bin(myElem)
            if not v[myBin]:
                q.append((myElem, d+1))
                v[myBin] = 1
    return myD

nCases = int(input())

myOutput = ''

for j in range(nCases):
    (myStr, myK) = input().split(' ')
    myK = int(myK)
    myRet = solveIt(myStr, myK)
    if (myRet == -1):
        myOutput += "Case #" + str(j + 1) + ": IMPOSSIBLE\n"
        # print("Case #{}: {}".format(j + 1, 'IMPOSSIBLE'))
    else:
        myOutput += "Case #" + str(j + 1) + ": " + str(myRet) + "\n"
        # print("Case #{}: {}".format(j + 1, myRet))
print(myOutput)
