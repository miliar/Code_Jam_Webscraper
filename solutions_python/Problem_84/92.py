import sys

def doOne():
    result = ''
    lastLine = []
    inSquare = False
    R, C = [int(x) for x in f.readline().strip().split()]
    rows = [f.readline() for r in range(R)]
    for row in rows:
        thisLine = []
        for n, c in enumerate(row):
            if lastLine and lastLine[0] == n:
                lastLine.pop(0)
                inSquare = True
                assert c == '#'
                result += '\\'
                top = False
            elif inSquare:
                assert c == '#'
                inSquare = False
                if top:
                    result += '\\'
                else:
                    result += '/'
            elif c == '#':
                inSquare = True
                thisLine.append(n)
                top = True
                result += '/'
            elif c == '.':
                result += '.'
            else:
                result += '\n'

        lastLine = thisLine
    assert not lastLine
    return result 

with open(sys.argv[1]) as f:
    T = int(f.readline().strip())
    for t in range(T):
        print "Case #%s:" % (t+1)
        try:
            sys.stdout.write(doOne())
        except AssertionError:
            print "Impossible"

