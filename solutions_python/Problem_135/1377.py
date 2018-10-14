T = int(raw_input())
for t in range(T):
    r1 = int(raw_input()) - 1
    grid1 = []
    for r in range(4):
        grid1.append(map(int, raw_input().split()))
    r2 = int(raw_input()) - 1
    grid2 = []
    for r in range(4):
        grid2.append(map(int, raw_input().split()))

    v1 = set(grid1[r1])
    v2 = set(grid2[r2])

    intersection = list(v1 & v2)
    num = len(intersection)

    if num == 0:
        ret = 'Volunteer cheated!'
    elif num == 1:
        ret = intersection[0]
    else:
        ret = 'Bad magician!'

    print 'Case #%d: %s' % (t + 1, ret)
