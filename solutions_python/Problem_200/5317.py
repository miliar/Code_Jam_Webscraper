inputFile = open('B-small-attempt0.in', 'r')
outputFile = open('B-small-attempt0.out', 'w')

def previousNumber(noList):
    print noList
    for i in range(1, len(noList)+1):
        if noList[-i] != '0':
            noList[-i] = str(int(noList[-i]) - 1)
            return noList
        else:
            noList[-i] = '9'

def solution(N):
    noList = []
    for n in N:
        noList.append(n)

    while True:
        for i in range(len(noList)):
            if i+1 >= len(noList):
                #remove zero
                invalidNo = True
                result = []
                for x in range(len(noList)):
                    if noList[x] != '0' or invalidNo == False:
                        print 'selected: ' + noList[x]
                        invalidNo = False
                        result.append(noList[x])
                return ''.join(result)
            if noList[i] > noList[i+1]:
                noList = previousNumber(noList)
                break


if __name__ == "__main__":
    T = int(inputFile.readline())
    for t in range(T):
        N = inputFile.readline().replace('\n','')
        result = solution(N)
        output = 'Case #' + str(t+1) + ': ' + result + '\n'
        print output
        outputFile.write(output)
