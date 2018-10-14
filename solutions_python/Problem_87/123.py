import sys
import math

input = sys.stdin
def readline():
    return input.readline().strip(' \r\n\t')

def readIntLine(hasSpace):
    if (hasSpace):
        return [int(x) for x in readline().split()]
    else:
        arr = []
        line = readline()
        for i in xrange(0, len(line)):
            arr.append(int(line[i]))
        return arr

def readCharLine(hasSpace):
    if (hasSpace):
        return readline().split()
    else:
        arr = []
        line = readline()
        for i in xrange(0, len(line)):
            arr.append(line[i])
        return arr

def readIntArr(row, col, hasSpace):
    arr = [[0] * col for x in xrange(row)] 
    for i in xrange(row):
        if (hasSpace):
            arr[i] = [int(x) for x in readline().split()]
        else:
            line = readline()
            for j in xrange(0, col):
                arr[i][j] = int(line[j])
    return arr

def readCharArr(row, col, hasSpace):
    arr = [[''] * col for x in xrange(row)] 
    for i in xrange(row):
        if (hasSpace):
            arr[i] = readline().split()
        else:
            line = readline()
            for j in xrange(0, col):
                arr[i][j] = line[j]
    return arr

def solve(input):
    line = readIntLine(True)
    #line = readIntLine(False)
    #line = readCharLine(True)
    #line = readCharLine(False)
    #arr = readIntArr(row, col, True)
    #arr = readIntArr(row, col, False)
    #arr = readCharArr(row, col, True)
    #arr = readCharArr(row, col, False)
    X = line[0]
    S = line[1]
    R = line[2]
    t = float(line[3])
    N = line[4]

    g = [] 
    current = 0
    for i in xrange(N):
        line = readIntLine(True)
        if (line[0] > current):
            g.append((float(S) / float(R), 0,  current, line[0]))
        g.append((float(S + line[2]) / float(R + line[2]), line[2], line[0], line[1]))
        current = line[1]
    if current < X:
        g.append((float(S / R), 0, current, X))
    g = sorted(g)
    time = 0.0
    for i in xrange(len(g)):
        interval = g[i][3] - g[i][2]
        use = float(interval) / float(R + g[i][1])
        if use <= t:
            t = t - use
            time = time + use
        else:
            time = time + t
            leftinterval = interval - (t*(R + g[i][1]))
            time = time + (float(leftinterval) / float(S + g[i][1]))
            t = 0

    return time

T = int(readline())
for t in xrange(T):
    answer = solve(input)
    print 'Case #%d: %s' % (t + 1, answer)
    sys.stdout.flush()
