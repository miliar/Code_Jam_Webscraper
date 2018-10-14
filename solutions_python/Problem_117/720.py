
def possibleH(table, r, c):
    if len(table[r]) == c: return True
    return (len(filter(lambda x: x > table[r][c], table[r])) == 0)

def possibleV(table, r, c):
    if len(table) == r: return True
    return (len(filter(lambda x: x[c] > table[r][c], table)) == 0)

def checkTable(table):
    for r in xrange(0, len(table)):
        for c in xrange(0, len(table[r])):
            if not possibleH(table, r, c) and not possibleV(table, r, c):
                return False
    return True

if __name__ == "__main__":
    T = int(raw_input())
    for c in xrange(1,T+1):
        table = []
        [N, M] = map(lambda x: int(x), raw_input().split())
        for i in xrange(0,N):
            table.append(map(lambda x: int(x), raw_input().split()))

        msg = 'NO'
        if (checkTable(table)): msg = 'YES'

        print 'Case #%d: %s' % (c, msg)

    

