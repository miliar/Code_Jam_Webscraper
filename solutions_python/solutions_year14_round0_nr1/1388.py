from sys import stdin

def handleTest(case, inputLines):
    answer1 = int(inputLines[0])
    cards1 = map(lambda l: l.split(" "), inputLines[1:5])

    answer2 = int(inputLines[5])
    cards2 = map(lambda l: l.split(" "), inputLines[6:])

    chosen1 = set(cards1[answer1 - 1])
    chosen2 = set(cards2[answer2 - 1])

    cardChoice = chosen1.intersection(chosen2)

    result = ""
    if len(cardChoice) == 0:
        result = "Volunteer cheated!"
    elif len(cardChoice) == 1:
        result = list(cardChoice)[0]
    else:
        result = "Bad magician!"

    print "Case #%s: %s" % (case, result)


if __name__ == '__main__':
    data = stdin.read().strip()

    lines = data.split("\n")

    numTests = int(lines[0])

    case = 1
    index = 1
    while index < len(lines):
        linesPerTest = 1 + 4 + 1 + 4
        inputLines = lines[index:index+linesPerTest]
        handleTest(case, inputLines)
        case += 1

        index += linesPerTest
