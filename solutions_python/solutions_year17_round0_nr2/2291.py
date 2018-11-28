

def main():
    f = open("B-large.in")
    tests = int(f.readline())
    for i in range(tests):
        n = int(f.readline())
        result = makeTidy(n)
        print("Case #{0}: {1}".format(i+1, result))
        # print("is tidy: {0}".format(result == lastTidy(n)))

def lastTidy(n):
    while not isTidy(n):
        n -= 1
    return n

def isTidy(n):
    nString = str(n)
    lastDigit = 0
    for s in nString:
        thisDigit = int(s)
        if thisDigit < lastDigit:
            return False
        lastDigit = thisDigit
    return True

def makeTidy(n):
    nList = [int(s) for s in str(n)]
    lastDigit = 9
    i = len(nList) - 1
    while not isTidy(toInt(nList)):
        thisDigit = int(nList[i])
        if thisDigit > lastDigit:
            for index in range(i+1, len(nList)):
                nList[index] = 9
            nList[i] = nList[i] - 1 if nList[i] > 0 else 9
            i = len(nList) - 1
            lastDigit = 9
        else:
            lastDigit = thisDigit
            i -= 1
    return toInt(nList)

def toInt(l):
    return int(''.join(map(str, l)))

if __name__ == "__main__":
    main()
