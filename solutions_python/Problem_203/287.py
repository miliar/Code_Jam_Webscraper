T = input()
def filled(r):
    for c in r:
        if c == '?':
            return False
    return True
def first(r, i):
    for c in r[i:]:
        if c != '?':
            return c
for test in xrange(1, T+1):
    r, c = map(int, raw_input().split())
    cake = [list(raw_input()) for x in xrange(r)]
    last = []
    for row in cake:
        if first(row, 0) != None:
            i = 0
            while i < len(row):
                c = first(row, i)
                while i < len(row) and row[i] in {c, '?'}:
                    row[i] = c
                    i+=1
            last = row
    for row in xrange(len(cake)-1, -1, -1):
        if first(cake[row], 0) == None:
            cake[row] = last
        else:
            last = cake[row]
    print "Case #%d:"%test
    print '\n'.join([''.join(row) for row in cake])
