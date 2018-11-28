




def readboards(filename):
    f = open(filename, 'r')
    n = int(f.readline().strip())
    boards = []
    for i in range(n):
        yield [f.readline().strip() for b in range(4)]
        f.readline()

def row(b, a):
    for r in b:
        if win(r,a):
            return True
    return False

def win(line, a):
    return line.replace('T',a) == a*4

def flip(b):
    return ["".join([b[i][j] for i in range(4)]) for j in range(4)]


def diags(b):
    d1 = "".join([r[i] for i,r in enumerate(b)])
    d2 = "".join([r[3-i] for i,r in enumerate(b)])
    return d1,d2

def complete(b):
    for r in b:
        if '.' in r:
            return False
    return True

def boardstate(b):
    fb = flip(b)
    d1, d2 = diags(b)
    xwins = row(b, 'X') or row(fb, 'X') or win(d1, 'X') or win(d2, 'X')
    ywins = row(b, 'O') or row(fb, 'O') or win(d1, 'O') or win(d2, 'O')

    if xwins is ywins:
        if complete(b):
            return "Draw"
        else:
            return "Game has not completed"
    elif xwins:
        return "X won"
    else:
        return "O won"



case = 1
infile = 'A-large.in' 
outfile = infile+'.out'
of = open(outfile, 'w')
for b in readboards(infile):
    of.write("Case #%i: %s\n" % (case, boardstate(b)))
    case += 1

