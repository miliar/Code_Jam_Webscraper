#!/usr/bin python

def main():
    inputFile = open("sample.txt", "r")
    nbTestCases = int(inputFile.readline())

    for idCase in range(nbTestCases):
        # FIXME
        line = inputFile.readline().split()
        C = float(line[0])
        F = float(line[1])
        X = float(line[2])

        bestTime = X / 2.0
        nbFarms = 1.0

        while(1):
            time = 0.0
            numFarm = 1.0
            while (numFarm <= nbFarms):
                time += C / (2.0 + F * (numFarm - 1.0))
                numFarm += 1.0
            time += X / (2.0 + F * nbFarms)
            #currTime = computeTotalTimeForNFarms(C, F, X, nbFarms)
            if (time <= bestTime):
                bestTime = time
                nbFarms += 1.0
            else:
                print("Case #" + str(idCase + 1) + ": " + str(bestTime))
                break

    inputFile.close()


main()
