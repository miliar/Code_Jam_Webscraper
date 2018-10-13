def findSpeed(D,N,KS):
    times = []
    longestTime = 0
    speed = 0
    for horse in range(N):
        restDistance = D - KS[horse][0]
        time = restDistance / KS[horse][1]
        if(time >= longestTime):
            speed = KS[horse][1]
            longestTime = time
    return longestTime

if(__name__ == "__main__"):
    import sys
    readFile = open(sys.argv[1])
    testCases = readFile.readline().rstrip()
    testCases = int(testCases)
    result = []
    for pos, lineNum in enumerate(range(testCases)):
        D, N = readFile.readline().rstrip().split(" ")
        horses = []
        for i in range(int(N)):
            line = readFile.readline().rstrip().split(" ")
            horses.append([int(line[0]), int(line[1])])
        time = findSpeed(int(D),int(N),horses)
        result.append("Case #{}: {sp:.6f}\n".format(pos+1, sp = int(D)/time))
    readFile.close()

    writeFile = open("result.txt",'w')
    writeFile.writelines(result)
    writeFile.close()


