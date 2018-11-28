f = open('a.in')
out = open('a.out', 'w+')
t = int(f.readline())
for tc in range(t):
    rows = []
    for i in range(2):
        guess = int(f.readline())
        grid = []
        for x in range(4):
            grid.append([int(p) for p in f.readline().split()])
        rows.append(grid[guess-1])
    poss = list(set(rows[0]) & set(rows[1]))
    if len(poss) == 0:
        res = 'Volunteer cheated!'
    elif len(poss) > 1:
        res = 'Bad magician!'
    else:
        res = str(poss[0])
    out.write('Case #{0}: {1}\n'.format(tc+1, res))