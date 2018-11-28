import sys

if __name__ == '__main__':
    fileInput   = open(sys.argv[1], 'r')
    fileOutput  = open("output.txt", 'w')

    numCases = int(fileInput.readline())

    for case in range(numCases):
        fileOutput.write("Case #"+str(case+1)+": ")

        numRounds = int(fileInput.readline())
        sumNaomi = [float(x) for x in fileInput.readline().split()]
        sumKen   = [float(x) for x in fileInput.readline().split()]
        sumNaomi2 = [x for x in sumNaomi]
        sumKen2   = [x for x in sumKen]
        sumNaomi.sort()
        sumKen.sort()
        sumNaomi2.sort()
        sumKen2.sort()

        accumWar = 0
        accumDecit = 0

        for i in sumNaomi2:
            check = False

            for k in sumKen2:
                if k > i:
                    sumKen2.remove(k)
                    check = True
                    break
            if check == False:
                accumWar += 1

        for i in range(numRounds):
            if min(sumNaomi) < min(sumKen):
                sumNaomi.pop(0)
                sumKen.pop()
            elif max(sumNaomi) < max(sumKen):
                sumNaomi.pop(0)
                sumKen.pop()
            else:
                sumNaomi.pop(0)
                sumKen.pop(0)
                accumDecit += 1
        fileOutput.write(str(accumDecit)+" "+str(accumWar))
        if case < numCases-1:
            fileOutput.write('\n')
