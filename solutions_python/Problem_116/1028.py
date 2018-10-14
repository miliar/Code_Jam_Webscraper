import sys


def check_line(r, sx, sy, xd, yd):
    line = []
    x = sx
    y = sy
    for i in xrange(0, 4):
        line.append(r[x][y])
        x += xd
        y += yd
    linestr = ''.join(line)
    if linestr.replace('T', 'X') == 'XXXX':
        return 'X'
    if linestr.replace('T', 'O') == 'OOOO':
        return 'O'
    #print linestr


def check_field(r):
    p = [[0, 0, 1, 0], [0, 1, 1, 0], [0, 2, 1, 0], [0, 3, 1, 0], [0, 0, 0, 1], [1, 0, 0, 1], [2, 0, 0, 1],
         [3, 0, 0, 1], [0, 0, 1, 1], [3, 0, -1, 1]]
    for i in xrange(len(p)):
        res = check_line(r, *p[i])
        if res:
            return res + " won"
    if '.' in ''.join(r):
        return "Game has not completed"
    return "Draw"

def read_field(lines, test_num):
    r = [lines[1 + test_num * 5]]
    r += [lines[1 + test_num * 5 + 1]]
    r += [lines[1 + test_num * 5 + 2]]
    r += [lines[1 + test_num * 5 + 3]]
    return r

def execute(intxt):
    lines = intxt.split('\n')
    tests_total = int(lines[0])
    outtxt = ''
    for test_num in xrange(0, tests_total):
        result = check_field(read_field(lines, test_num))
        outtxt += "Case #%s: %s\n" % (test_num + 1, result)
    return outtxt[:-1]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        infile = sys.argv[1]
        outfile = sys.argv[2]
    else:
        infile = "testIn.txt"
        outfile = "testOut.txt"
    with open(infile, 'r') as _ifile:
        with open(outfile, 'wb') as _ofile:
            _ofile.write(execute(_ifile.read()))
