def getResultOfAnalysis(arrangement1, arrangement2, choice1, choice2):
    choice1 = choice1 - 1
    choice2 = choice2 - 1
    numberOfCommonCards = 0
    commonCard = ""
    for i in range(4):
        for j in range(4):
            if (arrangement1[choice1][i] == arrangement2[choice2][j]):
                numberOfCommonCards = numberOfCommonCards + 1
                commonCard = arrangement1[choice1][i]
    if numberOfCommonCards == 1:
        return commonCard
    elif numberOfCommonCards == 0:
        return "Volunteer cheated!"
    elif numberOfCommonCards > 1:
        return "Bad magician!"


def run():
    f = open("magicTrickInput.txt")
    numberOfTestCases = int(f.readline())
    for i in range(numberOfTestCases):
        choice1 = int(f.readline())
        line1 = f.readline().split()
        line2 = f.readline().split()
        line3 = f.readline().split()
        line4 = f.readline().split()
        arrangement1 = [line1, line2, line3, line4]

        choice2 = int(f.readline())
        line1 = f.readline().split()
        line2 = f.readline().split()
        line3 = f.readline().split()
        line4 = f.readline().split()
        arrangement2 = [line1, line2, line3, line4]

        print "Case #" + str(i + 1) + ": " + getResultOfAnalysis(arrangement1, arrangement2, choice1, choice2)

run()
