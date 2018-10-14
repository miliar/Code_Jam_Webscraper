__author__ = 'George'
#Magic Trick
outputFile = open("magicOutput_real.txt", "a")
inputFile = open("A-small-attempt0.in", "r")
lines = inputFile.readlines()
TestCases = int(lines[0])
startLine = 1

def SolveProblem(linesfed):
    # print linesfed
    possibilities = 0
    SelectedCard = None
    rowFirst = int(linesfed[0])+0
    rowSecond = int(linesfed[5])+5
    strLeft = linesfed[rowFirst].split("\n")[0]
    strRight = linesfed[rowSecond].split("\n")[0]

    lefts = tuple(int(x) for x in strLeft.split(" "))
    rights = tuple(int(x) for x in strRight.split(" "))
    for card in lefts:
        if card in rights:
            possibilities += 1
            SelectedCard = card
    return possibilities, SelectedCard


for cases in range(TestCases):
    print >>outputFile, "Case #%s:" %(cases+1),
    pos, val = SolveProblem(lines[startLine:startLine+10])
    if pos == 1:
        print >>outputFile, val
    elif pos == 0:
        print >>outputFile, "Volunteer cheated!"
    else:
        print >>outputFile, "Bad magician!"

    startLine += 10



