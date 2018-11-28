t = int(raw_input().strip())

for i in range(t):
    row1 = int(raw_input().strip())
    for u in range(4):
        row = map(int, raw_input().strip().split(' '))
        if u == row1 - 1:
            rowset1 = set(row)

    row2 = int(raw_input().strip())
    for u in range(4):
        row = map(int, raw_input().strip().split(' '))
        if u == row2 - 1:
            rowset2 = set(row)

    inter = rowset1 & rowset2
    if len(inter) == 0:
        print 'Case #%d: Volunteer cheated!' % (i+1)
    elif len(inter) == 1:
        print 'Case #%d: %d' % (i+1, list(inter)[0])
    else:
        print 'Case #%d: Bad magician!' % (i+1)
