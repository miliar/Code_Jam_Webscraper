# Google Code Jam 2014 qualification round A.
# Read a row number, four rows of four cards, repeat, and return the
# selected card or an error string.
import sys

def doCase(file):
    chosen = []                 # The cards chosen by the volunteer
    for _ in range(2):
        rowChosen = int(file.readline()) - 1
        rows = []               # The rows of cards in the grid
        for row in range(4):
            rows.append(map(int, file.readline().split()))
        chosen.append(set(rows[rowChosen]))
    card = chosen[0] & chosen[1]
    if len(card) > 1:
        return 'Bad magician!'
    if len(card) < 1:
        return 'Volunteer cheated!'
    return card.pop()

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        answer = doCase(file)
        print 'Case #{0}: {1}'.format(case, answer)
run()
