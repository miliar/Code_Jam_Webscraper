__author__ = 'William Archinal'


# Note this requires items to be sorted
def getSmallestLargerThan(target, items):
    for i in items:
        if i > target:
            return i


def handleCase(n):
    # Get block count
    blockCount = int(raw_input())

    # Get each player's blocks
    naomiBlocksStr = raw_input().split(" ")
    kenBlocksStr = raw_input().split(" ")

    naomiBlocks = []
    kenBlocks = []
    for b in naomiBlocksStr:
        naomiBlocks.append(float(b))
    for b in kenBlocksStr:
        kenBlocks.append(float(b))

    # Sort the array for easy and efficient comparison
    naomiBlocks = sorted(naomiBlocks)
    kenBlocks = sorted(kenBlocks)

    # We're now ready to get the best case for each person
    # Determine best case for honesty
    bestHonest = 0
    while len(naomiBlocks) > 0:
        naomiSelection = naomiBlocks.pop(0)
        if naomiSelection > kenBlocks[-1]:
            kenBlocks.pop(0)
            bestHonest += 1
        else:
            kenBlocks.remove(getSmallestLargerThan(naomiSelection, kenBlocks))

    # Reset the lists
    naomiBlocks = []
    kenBlocks = []
    for b in naomiBlocksStr:
        naomiBlocks.append(float(b))
    for b in kenBlocksStr:
        kenBlocks.append(float(b))

    naomiBlocks = sorted(naomiBlocks)
    kenBlocks = sorted(kenBlocks)

    # Determine best case for cheating
    bestCheat = 0
    while len(naomiBlocks) > 0:
        # If ken has a better smallest block than naomi, weed out ken's best
        if kenBlocks[0] > naomiBlocks[0]:
            kenBlocks.pop()
            naomiBlocks.pop(0)
        else:
            kenBlocks.pop(0)
            naomiBlocks.pop(0)
            bestCheat += 1

    print "Case #" + str(n) + ": " + str(bestCheat) + " " + str(bestHonest)


def main():
    numCases = raw_input()
    for case in xrange(1, int(numCases) + 1):
        handleCase(case)


if __name__ == "__main__":
    main()