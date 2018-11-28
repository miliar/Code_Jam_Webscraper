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
    row = line[0]
    col = line[1]
    #arr = readIntArr(row, col, True)
    #arr = readIntArr(row, col, False)
    #arr = readCharArr(row, col, True)
    arr = readCharArr(row, col, False)

    for i in xrange(row):
        for j in xrange(col):
            if arr[i][j] == '#':
                arr[i][j] = '/'
                if j + 1 >= col or arr[i][j+1] != '#':
                    return '\nImpossible'
                else:
                    arr[i][j+1] = '\\'
                    if i+1 >= row or arr[i+1][j] != '#':
                        return '\nImpossible'
                    else:
                        arr[i+1][j] = '\\'
                        if arr[i+1][j+1] != '#':
                            return '\nImpossible'
                        else:
                            arr[i+1][j+1] = '/'
                    
                    
    ans = '' 
    for i in xrange(row):
        for j in xrange(col):
            ans = ans + arr[i][j]
        if (i != row - 1):
            ans = ans + '\n'
    return '\n' + str(ans)


T = int(readline())
for t in xrange(T):
    answer = solve(input)
    print 'Case #%d: %s' % (t + 1, answer)
    sys.stdout.flush()
