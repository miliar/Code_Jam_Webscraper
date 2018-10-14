import math

formatStringOutput = "Case #{0}: {1}"
nonPossibleSolution = "impossible"

def main():
        with open('test.in', 'r') as f:
                data = f.readlines()
        numberOfDataSets = int(data[0])
        data = data[1:]
        for x in xrange(len(data)):
                solve(x, [int(y) for y in data[x].strip().split('/')])

def solve(problemNumber, pair):
        if pair[1] % pair[0] == 0:
                printResult(problemNumber, int(math.log(pair[1]/pair[0], 2)))
                return
        eGen = -1
        currentPair = [x for x in pair]
        for currentGeneration in xrange(40):
               currentPair[0] = currentPair[0] * 2
               if currentPair[0] >= currentPair[1]:
                        #Found a whole elf
                        if eGen == -1:
                                eGen = currentGeneration + 1
                        currentPair[0] = currentPair[0] - currentPair[1]
                        if currentPair[0] == 0:
                                printResult(problemNumber, eGen)
                                return
        printResult(problemNumber, nonPossibleSolution)


def printResult(problemNumber, result):
        print str.format(formatStringOutput, problemNumber + 1, result)

if __name__ == "__main__":
        main()
