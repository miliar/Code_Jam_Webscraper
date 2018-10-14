import sys
from itertools import product

def ispalindrom(num):
    s = "%s" % num
    if s == s[::-1]:
        return True
    return False

def execute(intxt):
    lines = intxt.split('\n')
    tests_total = int(lines[0])
    outtxt = ''
    for test_num in xrange(0, tests_total):
        s, e = map(int, lines[test_num + 1].split(' '))
        i = int(s ** .5)
        result = 0
        while(True):
            if (ispalindrom(i) and ispalindrom(i*i)):
                if (i * i >= s and i * i <= e):
                    result += 1
            i += 1
            if i > e ** .5:
                break

        outtxt += "Case #%s: %s\n" % (test_num + 1, result)
    return outtxt

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
