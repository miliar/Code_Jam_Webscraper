# CodeJam 2013
# Matt Maybeno
# biophetik@gmail.com

import itertools


def readinput():
    """ Reads input one line at a time """
    with open("A-large.in") as f:
        tcases = f.next()
        for line in f:
            yield line.rstrip()


def run():
    """ Sends single 4x4 array to be calculated """
    gamearray = []
    num = 1
    output = open("output_large.txt", "w")
    for line in readinput():
        if line:
            gamearray.append(line)

        if len(gamearray) == 4:
            outputstr = "Case #%s: %s\n" % (str(num), solve(gamearray))
            output.write(outputstr)
            gamearray = []
            num += 1
    output.close()


def solve(gamearray):
    """ Computes who wins """
    xwin = 0
    owin = 0
    total = 0
    for row in vec(gamearray):
        xcount = row.count("X")
        ocount = row.count("O")
        tcount = row.count("T")
        total += xcount + ocount + tcount
        if xcount + tcount == 4:
            xwin = 1
        if ocount + tcount == 4:
            owin = 1

    if xwin == 0 and owin == 0 and total == 40:
        return "Draw"
    elif xwin == 0 and owin == 0:
        return "Game has not completed"
    elif xwin == 1 and owin == 0:
        return "X won"
    elif owin == 1 and xwin == 0:
        return "O won"


def vec(gamearray):
    """ All vectors in 4x4 """

    colarray = ["".join(x) for x in zip(*gamearray)]
    fdiag = "".join([gamearray[x][x] for x in xrange(4)])
    rdiag = "".join([gamearray[x][y] for x, y in zip(xrange(4),
                                                     xrange(3, -1, -1))])
    return itertools.chain(gamearray, colarray, [fdiag], [rdiag])

if __name__ == "__main__":
    run()