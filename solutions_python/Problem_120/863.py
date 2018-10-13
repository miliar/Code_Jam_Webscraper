import sys
import math

def area(r):
    return math.pi * r * r

def ring(r1, r2):
    return math.pi * (r2 * r2 - r1 * r1)
# 100000000
# 7070

#pi r r = s
#r r = s/pi
def execute(intxt):
    lines = intxt.split('\n')
    tests_total = int(lines[0])
    outtxt = ''
    for test_num in xrange(1, tests_total + 1):
        r, t = map(int, lines[test_num].split(' '))
        print t ** .5
        treq = 0
        result = 0
        t = t
        while True:
            treq += (r + 1) * (r + 1) - r * r #ring(r, r + 1)
            if treq > t:
                break
            result += 1
            r += 2
        outtxt += "Case #%s: %s\n" % (test_num, result)
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
