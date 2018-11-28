import sys
from itertools import chain, izip


def readfield(inf):
    l = [inf.readline().strip() for i in range(4)]
    inf.readline()  # Empty line
    return l


def diags(field):
    yield "".join(field[i][i] for i in range(4))
    yield "".join(field[3 - i][i] for i in range(4))


def dofield(field, fieldno):
    sys.stdout.write("Case #{}: ".format(fieldno))

    def iswinning(line):
        linefill = reduce(lambda acc, x: acc if acc == x or x == 'T' else '.', line, line[0] if line[0] != 'T' else line[1])
        return linefill if linefill != '.' else False

    # Check rows, cols, diagonals, respectively.
    for row in chain(field, izip(*field), diags(field)):
        winner = iswinning(row)
        if winner:
            print(winner + " won")
            return

    if '.' in "".join(chain(*field)):
        print("Game has not completed")
        return

    print("Draw")


inf = sys.stdin
fields = [readfield(inf) for i in range(int(inf.readline()))]
map(dofield, fields, range(1, len(fields) + 1))
