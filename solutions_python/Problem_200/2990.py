

def convertToInt(numList):
    s = ''.join(map(str, numList))
    return int(s)

def isSorted(Num):
    StrNum = str(Num)
    nl=[]
    for d in StrNum:
        nl.append(int(d))
        nlsort = sorted(nl)

    if convertToInt(nlsort) == Num:
        return True
    else:
        return False

def updateNines(Num):
    StrNum = str(Num)
    nl=[]
    for d in StrNum:
        nl.append(int(d))

    for i in range(0, len(nl)):
        c = nl[i]
        n = nl[i+1]
        if n < c:
            nl[i] = nl[i]-1
            for j in range(i+1, len(nl)):
                nl[j] = 9
            return convertToInt(nl)

def prevTidyNum(N):
    tidy = False
    pN = N
    if isSorted(pN):
        return pN
    else:
        while tidy == False:
            pN = updateNines(pN)
            #print pN
            if isSorted(pN) == True:
                return pN


print prevTidyNum(24789)

# read input N
file = open("B-large.in", "r")
Testcases = int(file.readline())
print Testcases

outfile = open("B-large.out","w")

for x in range(1, Testcases+1):
    val = int(file.readline())
    result = prevTidyNum(val)
    print result
    OutputText = "Case #" + str(x) + ": " + str(result)
    outfile.write(OutputText + '\n')

file.close()
outfile.close()

