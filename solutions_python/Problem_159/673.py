filename = "A-large.in"
# filename = "testinput.txt"

f = open(filename, "r")
numTestCases = f.readline()

for testCase in range(int(numTestCases)):
    n = int(f.readline())
    mushrooms = [int(i) for i in f.readline().split()]

    m1 = 0
    biggestDiff = 0
    for i in range(len(mushrooms)):
        if i != 0:
            if mushrooms[i] < mushrooms[i - 1]:
                m1 += mushrooms[i - 1] - mushrooms[i]
                if mushrooms[i - 1] - mushrooms[i] > biggestDiff:
                    biggestDiff = mushrooms[i - 1] - mushrooms[i]


    m2 = 0
    mushroomsOnPlate = 0
    nonEaten = 0

    for i in range(len(mushrooms) - 1):
        # mushroomsOnPlate += mushrooms[i]
        # if mushroomsOnPlate >= biggestDiff:
        #     m2 += biggestDiff
        #     mushroomsOnPlate -= biggestDiff
        # elif mushroomsOnPlate > 0:
        #     m2 += mushroomsOnPlate
        #     mushroomsOnPlate = 0
        if mushrooms[i] < biggestDiff:
            nonEaten += biggestDiff - mushrooms[i]

    m2 = (n - 1) * biggestDiff - nonEaten

    print "Case #" + str(testCase + 1) + ": " + str(m1) + " " + str(m2)