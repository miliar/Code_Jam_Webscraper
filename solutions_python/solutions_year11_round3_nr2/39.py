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
    #row = line[0]
    #col = line[1]
    #arr = readIntArr(row, col, True)
    #arr = readIntArr(row, col, False)
    #arr = readCharArr(row, col, True)
    #arr = readCharArr(row, col, True)
    L = line[0]
    t = line[1]
    N = line[2]
    C = line[3]
    a = [0] * C
    for c in xrange(0, C):
        a[c] = line[c + 4]

    ans = a
    time = [0] * N
    sumtime = 0
    newtime = []
    cont = 0
    for i in xrange(N):
        time[i] = a[i%C] * 2
        if cont:
            newtime.append(time[i])
        else:
            if sumtime + time[i] > t:
                newtime.append(sumtime + time[i] - t)
                cont = 1
            else:
                sumtime = sumtime + time[i]
    newtime = sorted(newtime)
    for l in xrange(L):
        if (len(newtime) - 1 -l >= 0):
            newtime[len(newtime) - 1 - l] = newtime[len(newtime) - 1 -l] / 2
        else:
            break
    sumtime = 0
    for i in xrange(N):
        sumtime = sumtime + time[i]

    sum = 0
    for i in xrange(len(newtime)):
        sum = sum + newtime[i]
    if (t >= sumtime):
        return str(sumtime)
    else:
        return str(t + sum)


T = int(readline())
for t in xrange(T):
    answer = solve(input)
    print 'Case #%d: %s' % (t + 1, answer)
    sys.stdout.flush()
