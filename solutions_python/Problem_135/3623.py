import sys

def process_input(inputFile):
    f = open(inputFile, 'r')
    numCases = int(f.readline())

    if numCases < 1 or numCases > 1000:
        return False

    for x in range(numCases):
        round1Answer = int(f.readline())
        round1Arrangement = []
        for y in range(4):
            round1Arrangement.append(list(map(int, f.readline().split())))
        round1Line = round1Arrangement[round1Answer-1]

        round2Answer = int(f.readline())
        round2Arrangement = []
        for y in range(4):
            round2Arrangement.append(list(map(int, f.readline().split())))
        round2Line = round2Arrangement[round2Answer-1]

        chosenCardSet = set(round1Line).intersection(set(round2Line))

        sys.stdout.write("Case #%d: " % (x+1))

        if chosenCardSet:
            numOfPossible = len(chosenCardSet)
            if numOfPossible == 1:
                sys.stdout.write("%d\n" % int(chosenCardSet.pop()))
            else:
                sys.stdout.write("Bad magician!\n")
        else:
            sys.stdout.write("Volunteer cheated!\n")

    f.close()
    return True

if __name__ == "__main__":
    inputFile = sys.argv[1]

    if not process_input(inputFile):
        print "Error"
