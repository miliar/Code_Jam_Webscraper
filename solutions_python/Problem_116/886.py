import sys


def checkDirection(grid, i, j, di, dj):
    """ Check the score in a given direction """

    score = {'X': 0, 'O': 0, 'T': 0, '.': 0}

    while i < 4 and j < 4 and i >= 0 and j >= 0:
        score[grid[i][j]] += 1
        i += di
        j += dj

    if (score['X'] + score['T']) == 4:
        return 0
    elif (score['O'] + score['T']) == 4:
        return 2
    else:
        return 1


def check(grid):
    score = [0, 0, 0]
    notOver = False

    for i in xrange(0, 4):
        for j in xrange(0, 4):
            if grid[i][j] == '.':
                notOver = True
            score[checkDirection(grid, i, j, -1, 1)] += 1  # diag sup
            score[checkDirection(grid, i, j, 0, 1)] += 1  # line
            score[checkDirection(grid, i, j, 1, 1)] += 1  # diag inf
            score[checkDirection(grid, i, j, 1, 0)] += 1  # col

    if notOver and score[0] == score[2] == 0:
        return 'Game has not completed'
    elif score[0] == score[2]:
        return 'Draw'
    elif score[0] > score[2]:
        return 'X won'
    else:
        return 'O won'


def main(f):
    _t = int(f.readline())

    # Number of cases
    for t in xrange(0, _t):
        grid = [f.readline()[:-1] for x in xrange(0, 4)]
        print 'Case #%d: %s' % (t + 1, check(grid))
        f.readline()

if __name__ == '__main__':
    f = sys.stdin
    main(f)
