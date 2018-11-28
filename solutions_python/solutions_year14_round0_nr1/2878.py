T = int(raw_input())

for t in range(T):
    r1 = int(raw_input())
    grid1 = []
    for i in range(4):
        grid1.append([int(x) for x in raw_input().split()])
    l1 = set(grid1[r1 - 1])
    r2 = int(raw_input())
    grid2 = []
    for i in range(4):
        grid2.append([int(x) for x in raw_input().split()])
    l2 = set(grid2[r2 - 1])

    inter = l1.intersection(l2)
    if not inter:
        out = 'Volunteer cheated!'
    elif len(inter) > 1:
        out = 'Bad magician!'
    else:
        out = str(list(inter)[0])
    print 'Case #{}: {}'.format(t+1, out)
