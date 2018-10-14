#!/usr/bin/python3

from sys import argv

def answer(firstRow, firstGrid, secondRow, secondGrid):
    firstChoices = set(firstGrid[firstRow-1])
    secondChoices = set(secondGrid[secondRow-1])
    choices = firstChoices.intersection(secondChoices)
    if len(choices) == 0:
        return 'Volunteer cheated!'
    elif len(choices) > 1:
        return 'Bad magician!'
    else:
        for c in choices:
            result = c
        return str(c)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Google Code Jam I/O
    infile = open(argv[1])
    cases = int(infile.readline())
    for i in range(cases):
        firstRow = int(infile.readline())
        firstGrid = []
        for j in range(4):
            firstGrid.append(map(int, infile.readline().split()))
        secondRow = int(infile.readline())
        secondGrid = []
        for j in range(4):
            secondGrid.append(map(int, infile.readline().split()))
        print("Case #{}: {}".format(i+1, answer(firstRow, firstGrid, secondRow, secondGrid)))
