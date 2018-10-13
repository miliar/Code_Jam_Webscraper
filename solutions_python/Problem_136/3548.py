import sys

def process_input(inputFile):
    f = open(inputFile, 'r')
    numCases = int(f.readline())

    if numCases < 1 or numCases > 100:
        return False

    for x in range(numCases):
        C, F, X = list(map(float, f.readline().split()))

        times = []
        bestTime = None
        y = 0
        while True:
            cookiesPerSecond = 2.0
            totalTime = 0.0
            count = range(y+1)
            count.reverse()
            for z in count:
                if z == 0:
                    totalTime += (X / cookiesPerSecond)
                else:
                    totalTime += (C / cookiesPerSecond)

                cookiesPerSecond += F

            if bestTime == None:
                bestTime = totalTime
            else:
                if totalTime < bestTime:
                    bestTime = totalTime
                else:
                    break
            y+=1

        sys.stdout.write("Case #%d: %0.7f\n" % ((x+1), bestTime))

    f.close()
    return True

if __name__ == "__main__":
    inputFile = sys.argv[1]

    if not process_input(inputFile):
        print "Error"
