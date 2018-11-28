import sys
rl = lambda: sys.stdin.readline().strip()


T = int(rl())
for tcase in range(T):
    first = int(rl())
    board1 = [map(int, rl().split()) for i in range(4)]
    second = int(rl())
    board2 = [map(int, rl().split()) for i in range(4)]
    row1 = board1[first - 1]
    row2 = board2[second - 1]
    rows = row1 + row2
    cnts = sorted([(s, rows.count(s)) for s in set(rows)], key=lambda x: x[1], reverse=True)
    if cnts[0][1] == 2 and cnts[1][1] == 2:
        print 'Case #%d: Bad magician!' % (tcase + 1)
    elif cnts[0][1] == 2:
        print 'Case #%d: %d' % (tcase + 1, cnts[0][0])
    else:
        print 'Case #%d: Volunteer cheated!' % (tcase + 1)
