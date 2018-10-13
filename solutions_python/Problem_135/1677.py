__author__ = 'William Archinal'


def getTable():
    table = []
    for x in xrange(0, 4):
        rowStr = raw_input().split(" ")
        row = []
        for c in rowStr:
            row.append(int(c))
        table.append(row)
    return table


def handleTrick(n):
    firstRow = int(raw_input()) - 1
    table1 = getTable()
    possibles1 = table1[firstRow]
    secondRow = int(raw_input()) - 1
    table2 = getTable()
    possibles2 = table2[secondRow]
    finalPossibles = list(set.intersection(set(possibles1)).intersection(set(possibles2)))
    output = "Case #" + str(n) + ": "
    if len(finalPossibles) is 0:
        output += "Volunteer cheated!"
    elif len(finalPossibles) is 1:
        output += str(finalPossibles[0])
    else:
        output += "Bad magician!"

    print output


def main():
    numCases = raw_input()
    for case in xrange(1, int(numCases) + 1):
        handleTrick(case)


if __name__ == "__main__":
    main()