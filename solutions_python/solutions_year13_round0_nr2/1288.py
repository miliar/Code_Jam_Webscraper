import sys

def checkandsetcol(table, col):
    lst = [table[i][col] for i in xrange(len(table))]
    minval = min(lst)[0]
    if minval == sys.maxint: return True
    if ((not any(x[0] != sys.maxint and x[0] > minval for x in lst)) and
             all([x[0] != sys.maxint or x[1] <= minval for x in lst])):
        for i in xrange(len(table)):
            table[i][col][0] = sys.maxint
            table[i][col][1] = minval
        return True
    return False

def checkandsetrow(table, row):
    lst = [table[row][i] for i in xrange(len(table[0]))]
    minval = min(lst)[0]
    if minval == sys.maxint: return True
    if ((not any(x[0] != sys.maxint and x[0] > minval for x in lst)) and
             all([x[0] != sys.maxint or x[1] <= minval for x in lst])):
        for i in xrange(len(table[0])):
            table[row][i][0] = sys.maxint
            table[row][i][1] = minval
        return True
    return False

def calc(table):
    row = [False] * len(table)
    col = [False] * len(table[0])
    for r in xrange(5 * (len(table) + len(table[0]))):
        for i in xrange(len(table)):
            if not row[i] and checkandsetrow(table, i): row[i] = True
        for i in xrange(len(table[0])):
            if not col[i] and checkandsetcol(table, i): col[i] = True
    return "YES" if all(row) and all(col) else "NO"

def main():
    for t in xrange(input()):
        r, c = raw_input().split()
        table = []
        for i in xrange(int(r)):
            table.append([[int(x), 0] for x in raw_input().split()])
        print "Case #%d:" % (t + 1), calc(table)

if __name__ == "__main__":
    main()
