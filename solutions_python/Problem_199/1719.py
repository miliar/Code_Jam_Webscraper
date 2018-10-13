import time

def flipSubstring(pancakeStr, flipSize, posNegative):
    panCakeArr = []
    for p in pancakeStr:
        panCakeArr.append(p)
    for i in range(posNegative, posNegative+flipSize):
        if panCakeArr[i] == '+':
            panCakeArr[i]= '-'
        else:
            panCakeArr[i]='+'
    return ''.join(panCakeArr)

def flipPancakes(pString, flipSize):
    pancakeStr = pString
    flipCount = 0
    while pancakeStr.find('-')>-1:
        lenPancakeStr = len(pancakeStr)
        posNegative = pancakeStr.find('-')
        if lenPancakeStr - posNegative >= flipSize:         
            flipCount = flipCount + 1
            pancakeStr = flipSubstring(pancakeStr, flipSize, posNegative)
        else:
            return 'IMPOSSIBLE'
    return flipCount

def fileRead():
    start = time.time()
    fo = open("input.txt", "rw+")
    lineList = fo.readlines()
    noTestCases = int(lineList[0])
    f = open('output.txt', 'w')
    for i in range(1, noTestCases+1):
        inputStringList = lineList[i].split()
        S = inputStringList[0]
        K = int(inputStringList[1])
        result = flipPancakes(S, K)
        print "Case #"+str(i)+": "+str(result)
        if(i==noTestCases):
            f.write("Case #"+str(i)+": "+str(result))
        else:
            f.write("Case #"+str(i)+": "+str(result)+'\n')
    f.close()
    elapsed = (time.time() - start)
    print elapsed

def main():
    fileRead()

if __name__ == "__main__":
    main()