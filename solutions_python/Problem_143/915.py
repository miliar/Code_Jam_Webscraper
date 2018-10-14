import sys

def main():
    with open(sys.argv[1]) as inputFile:
        outputFile = open('lottery_output.txt', 'w')

        numberCases = int(inputFile.readline())
        for x in range(0, numberCases):
            numWins = 0
            inputNums = inputFile.readline().split()
            a = int(inputNums[0])
            b = int(inputNums[1])
            k = int(inputNums[2])

            numWins = generateWins(a, b, k)

            outputFile.write("Case #" + str(x + 1) + ": " + str(numWins) + '\n')
            outputFile.write("\n")
        outputFile.close()

def generateWins(a, b, k):
    winPossibilities = []
    for i in range(0, a):
        for j in range(0, b):
            winPossibilities.append([i, j])

    numWins = 0
    K = int(k)
    for possibleWin in winPossibilities:
        if possibleWin[0] & possibleWin[1] < K:
            numWins += 1
    return numWins

if __name__ == "__main__":
    main()