from re import split
import sys

__author__ = 'sladiwal'

fname = "A-large.in"


def count(list_in):
    xcount, ocount, tcount = 0, 0, 0
    for i in list_in:
        xcount += (i == 'X')
        ocount += (i == 'O')
        tcount += (i == 'T')
    return xcount, ocount, tcount


def winner(xcount, ocount, tcount):
    if (xcount == 3 and tcount == 1) or (ocount == 3 and tcount == 1) or (xcount == 4) or (ocount == 4):
        return True, 'X' if xcount >= 3 else 'O'
    return False, ''


def win_diag(mat):
    temp = [mat[0][0], mat[1][1], mat[2][2], mat[3][3]]
    return winner(*count(temp))


if __name__ == "__main__":
    f = open(fname, "r")
    T = int(f.readline())
    for x in range(T):
        mat = []
        won = False
        person = ''
        empty = False
        for y in range(4):
            mat += f.readline().rstrip().split()
            xcount, ocount, tcount = count(mat[y])
            w, p = winner(xcount, ocount, tcount)
            if w:
                won, person = w, p
            if xcount + ocount + tcount < 4:
                empty = True
        if not won:
            won, person = win_diag(mat)
        if not won:
            mat = zip(*mat[::-1])
            for y in range(4):
                w, p = winner(*count(mat[y]))
                if w:
                    won, person = True, p
                    break
        if not won:
            won, person = win_diag(mat)
        sys.stdout.write('Case #%d: ' % (x+1))
        if won:
            print '%s won' % person
        elif not empty:
            print 'Draw'
        else:
            print 'Game has not completed'
        f.readline()




