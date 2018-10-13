# Google Code Jam 2013 - Qualification Round
# Problem B: Lawnmower
#  By Matt Snider
import sys


def solve(lawn, dim):
    """ Check if this lawn config is possible.

    We need to check if there is a possible path
    out of the lawn at each square. We will examine
    the lawn row by row. For each row, we find the
    max, and examine each square in that row that is
    less than the max.

    Notice that if a square is less than it's rowmax
    there is no path out left/right. Therefore, we
    simply must check if there is an up/down path
    possible.
    """
    rows = lawn
    cols = [list(x) for x in zip(*lawn)]

    for i in range(0, dim[0]):
        tall = max(rows[i])

        for j in  range(0, dim[1]):
            if rows[i][j] < tall:
                path = sum(x <= rows[i][j] for x in cols[j])

                if path < dim[0]:
                    return "NO"

    return "YES"

def get_path():
    """ Find a path outwards from a position on the lawn.

    Each patch of grass must have a path out of the
    lawn on which every patch is the same height or
    smaller.
    """
    pass


if __name__ == '__main__':

    if len(sys.argv) != 2:
        exit("Error: must specify an input file name.")
    f = sys.argv[1]

    fin = open(f)
    fout = open(f[:f.find('.')] + '.out', 'w')
    T = int(fin.readline())

    for i in range(1, T + 1):
        dim = tuple(int(x) for x in fin.readline().split())
        lawn = []

        for _ in range(0, dim[0]):
            line = list(map(int,fin.readline().split()))
            lawn.append(line)

        result = solve(lawn, dim)
        fout.write("Case #%d: %s\n" % (i, result))