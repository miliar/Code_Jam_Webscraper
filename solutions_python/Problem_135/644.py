# Python 3.2

from common import *

def getrow():
    row = readint()
    rows = []
    for i in range(4):
        rows.append(readints())

    return rows[row - 1]

def main(casenum):
    row1 = getrow()
    row2 = getrow()

    res = list(filter(lambda x : x in row1, row2))

    if len(res) == 0:
        writeline ('Case #{}: Volunteer cheated!'.format(casenum))
    elif len(res) == 1:
        writeline ('Case #{}: {}'.format(casenum, res[0]))
    else:
        writeline ('Case #{}: Bad magician!'.format(casenum))

run(main)
