import sys
import math
import cPickle as pickle

inName = sys.argv[1]
outName = inName[:inName.index('.')] + '.out'

fin = open(inName)
fout = open(outName, 'w')

cases = int(fin.readline())

def pp(case, out):
    ss= "Case #%d: %s\n" % (case+1, out)
    print ss,
    fout.write(ss)

################
# i = 2, j = 3, k = 4
#
#   1   2   3   4
# 1 1   2   3   4
# 2 2  -1   4  -3
# 3 3  -4  -1   2
# 4 4  3   -2  -1

m = {
    (1, 1): 1,
    (1, 2): 2,
    (1, 3): 3,
    (1, 4): 4,
    (2, 1): 2,
    (2, 2): -1,
    (2, 3): 4,
    (2, 4): -3,
    (3, 1): 3,
    (3, 2): -4,
    (3, 3): -1,
    (3, 4): 2,
    (4, 1): 4,
    (4, 2): 3,
    (4, 3): -2,
    (4, 4): -1,

    (-1, 1): -1,
    (-1, 2): -2,
    (-1, 3): -3,
    (-1, 4): -4,
    (-2, 1): -2,
    (-2, 2): 1,
    (-2, 3): -4,
    (-2, 4): 3,
    (-3, 1): -3,
    (-3, 2): 4,
    (-3, 3): 1,
    (-3, 4): -2,
    (-4, 1): -4,
    (-4, 2): -3,
    (-4, 3): 2,
    (-4, 4): 1,

    (1, -1): -1,
    (1, -2): -2,
    (1, -3): -3,
    (1, -4): -4,
    (2, -1): -2,
    (2, -2): 1,
    (2, -3): -4,
    (2, -4): 3,
    (3, -1): -3,
    (3, -2): 4,
    (3, -3): 1,
    (3, -4): -2,
    (4, -1): -4,
    (4, -2): -3,
    (4, -3): 2,
    (4, -4): 1,

    (-1, -1): 1,
    (-1, -2): 2,
    (-1, -3): 3,
    (-1, -4): 4,
    (-2, -1): 2,
    (-2, -2): -1,
    (-2, -3): 4,
    (-2, -4): -3,
    (-3, -1): 3,
    (-3, -2): -4,
    (-3, -3): -1,
    (-3, -4): 2,
    (-4, -1): 4,
    (-4, -2): 3,
    (-4, -3): -2,
    (-4, -4): -1,
}

cache = {}

def mult(a, b):
    return m[(a, b)]

for case in xrange(cases):
    [L, X] = map(int, fin.readline().strip().split(' '))
    s = tuple(map(lambda c: 2 if c == 'i' else 3 if c == 'j' else 4, list(fin.readline().strip()))) * X

    if len(set(s)) == 1:
        pp(case, 'NO')
        continue

    cache = {}
    n = 0
    solveable = False
    iVal = 1
    kValues = []
    nextK = 1
    for k in xrange(len(s) - 1, -1, -1):
        nextK = mult(s[k], nextK)
        kValues.append(nextK)
    kValues.reverse()

    for i in xrange(1, len(s) - 1):
        iVal = mult(iVal, s[i-1])
        if iVal != 2:
            continue

        jVal = 1
        b = False
        for j in xrange(i + 1, len(s)):
            jVal = mult(jVal, s[j-1])
            if jVal != 3:
                continue

            if kValues[j] != 4:
                continue

            b = True
            solveable = True
            break
        if b:
            break

    pp(case, ('YES' if solveable else 'NO'))

fout.close()
