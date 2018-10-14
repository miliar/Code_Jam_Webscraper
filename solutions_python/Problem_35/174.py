import sys


def main():
    line = sys.stdin.readline().strip()
    values = line.split()

    testCnt = int(values[0])

    for testNum in range(testCnt):
        line = sys.stdin.readline().strip()
        values = line.split()
        rows = int(values[0])
        columns = int(values[1])

        mi = {}
        mo = {}
        for i in range(1, rows + 1):
            line = sys.stdin.readline().strip()
            elevations = line.split()
            for j in range(columns + 2):
                if j == 0 or j == columns + 1:
                    mi[i, j] = 99999
                else:
                    mi[i, j] = int(elevations[j - 1])
                    mo[i, j] = 'X'
        for j in range(0, columns + 2):
            mi[0, j] = 99999
            mi[rows + 1, j] = 99999

        nid = 'a'
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                if mo[i, j] == 'X':
                    nid = explore(mi, mo, rows, columns, i, j, nid)

        print 'Case #%d:' % (testNum + 1)
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):        
                print '%s' % mo[i, j],
            print

def explore(mi, mo, rows, columns, i, j, id):          
    nid = id
    if i <= 0 or j <= 0 or i > rows or j > columns or mo[i, j] <> 'X':
        return nid
    e = 10000
    d = 'X'    
    if mi[i + 1, j] < mi[i, j] and mi[i + 1, j] <= e:
        e = mi[i + 1, j]
        d = 'S'
    if mi[i, j + 1] < mi[i, j] and mi[i, j + 1] <= e:
        e = mi[i, j + 1]
        d = 'E'
    if mi[i, j - 1] < mi[i, j] and mi[i, j - 1] <= e:
        e = mi[i, j - 1]
        d = 'W'
    if mi[i - 1, j] < mi[i, j] and mi[i - 1, j] <= e:
        e = mi[i - 1, j]
        d = 'N'
    if d == 'N':
        nid = explore(mi, mo, rows, columns, i - 1, j, id)
        mo[i, j] = mo[i - 1, j]
    elif d == 'S':
        nid = explore(mi, mo, rows, columns, i + 1, j, id)
        mo[i, j] = mo[i + 1, j]
    elif d == 'W':
        nid = explore(mi, mo, rows, columns, i, j - 1, id)
        mo[i, j] = mo[i, j - 1]
    elif d == 'E':
        nid = explore(mi, mo, rows, columns, i, j + 1, id)
        mo[i, j] = mo[i, j + 1]
    else:
        mo[i, j] = id
        nid = chr(ord(id[0]) + 1)
    return nid
         
if __name__ == "__main__":
    main()
