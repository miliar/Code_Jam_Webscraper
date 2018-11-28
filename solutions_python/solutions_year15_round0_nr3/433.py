import sys


TARGET=(1, 0)  #(sign, char)
CHAR2INT = {
    '1' : 0,
    'i' : 1,
    'j' : 2,
    'k' : 3,
    }

MATRIX=[
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,1), (1,0), (0,3), (1,2)],
    [(0,2), (1,3), (1,0), (0,1)],
    [(0,3), (0,2), (1,1), (1,0)]
    ]

def multiplyTuple(x, y):
    z = MATRIX[x[1]][y[1]]
    sign = (x[0] + y[0] + z[0]) % 2
    return (sign, z[1])


def multiply(x, char):
    c = CHAR2INT[char]
    return multiplyTuple(x, (0, c))


def caclstr(s, times):
    ret = reduce(multiply, s, (0,0))
    return reduce(multiplyTuple, [ret] * times, (0,0))


def equal(x, y):
    return x[0] == y[0] and x[1] == y[1]


def findTarget(line, X, target):
    ret = (0, 0)
    LEN = len(line)

    for x in xrange(0, X):
        for i in xrange(0, LEN):
            ret = multiply(ret, line[i])
            if equal(ret, target):
                return x*LEN + i

        if x == 0 and ret[1] == 0:
            return None

    return None


def findTargetTail(line, X, target):
    ret = (0, 0)
    LEN = len(line)

    for x in xrange(X-1, -1, -1):
        for i in xrange(LEN-1, -1, -1):
            cur = (0, CHAR2INT[line[i]])
            ret = multiplyTuple(cur, ret)
            if equal(ret, target):
                return x*LEN + i

    return None

def caclRange(line, X, L, start, end):
    ret = (0, 0)
    LEN = len(line)

    for idx in xrange(start, end):
        i = idx % LEN
        ret = multiply(ret, line[i])

    return ret

def run(idx):
    line = sys.stdin.readline()
    arr = line.split(' ')
    L = int(arr[0])
    X = int(arr[1])
    line = sys.stdin.readline().strip()

    ret = False
    s="""
    if L <= 3 and X <= 3:
        if L * X < 3:
            return ret
        elif L * X == 3:
            return line * X == "ijk"
"""
    total = caclstr(line, X)
#    print "total=", total
    if not equal(total, TARGET):
        return False

    iIdx = findTarget(line, X, (0, 1))
    if iIdx is None:
        return False
    kIdx = findTargetTail(line, X, (0, 3))
#    print "iIdx=", iIdx, " kIdx=", kIdx
    if kIdx is None:
        return False
    if kIdx - iIdx < 2:
        return False

    return equal(caclRange(line, X, L, iIdx+1, kIdx), (0, 2))


T = int(sys.stdin.readline())
for i in xrange(1, T+1):
#for i in xrange(1, 2):
#    print "=========", i
    rstr = "YES" if run(i) else "NO"
    print "Case #%d: %s" % (i,  rstr)
