import sys

MINX = {}
MINY = {}


'''[[1,2,3]
 [1,2,3]
 [1,2,3]]'''
def check_field(field):
    rr = {}
    MINX = {}
    MINY = {}
    for y in xrange(0, len(field)):
        #print field[y]
        MINY[y] = max(*(field[y] + [0,]))
    for x in xrange(0, len(field[0])):
        t = [0,]
        for y in xrange(0, len(field)):
            t.append(field[y][x])
        #print t
        MINX[x] = max(*t)
    #print MINX, MINY
    for y in xrange(0, len(field)):
        for x in xrange(0, len(field[0])):
            #print x, MINX[x], y, MINY[y]
            if field[y][x] < MINX[x] and field[y][x] < MINY[y]:
                #print y, x, MINX, MINY
                return False
    
    return True


def execute(intxt):
    lines = intxt.split('\n')
    tests_total = int(lines[0])
    outtxt = ''
    cur_line = 1
    for test_num in xrange(0, tests_total):
        dy, dx = map(int, lines[cur_line].split(' '))
        field = map(lambda x: map(int, x.split(' ')), lines[cur_line + 1: cur_line + dy + 1])
        result = "YES" if check_field(field) else "NO"
        outtxt += "Case #%s: %s\n" % (test_num + 1, result)
        cur_line += dy + 1
    return outtxt[:-1]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        infile = sys.argv[1]
        outfile = sys.argv[2]
    else:
        infile = "B-small-attempt0.in.txt"
        outfile = "testOut.txt"
    with open(infile, 'r') as _ifile:
        with open(outfile, 'wb') as _ofile:
            _ofile.write(execute(_ifile.read()))
