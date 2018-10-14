def parser(filename):
    f = open(filename, 'r')
    iteration = int(f.readline()[:-1])
    output = []
    for i in range(iteration):
        sample = [int(f.readline()[:-1])]
        grid = []
        for k in range(4):
            grid.append(f.readline()[:-1].split(' '))
        sample.append(int(f.readline()[:-1]))
        sample.append(grid)
        grid = []
        for k in range(4):
            grid.append(f.readline()[:-1].split(' '))
        sample.append(grid)

        output.append(sample)
    return output

def magic(ans1, ans2, grid1, grid2):
    row1 = set(grid1[ans1-1])
    row2 = set(grid2[ans2-1])
    inter = row1.intersection(row2)
    inter = list(inter)

    if len(inter) == 0:
        return 'Volunteer cheated!'
    elif len(inter) == 1:
        return inter[0]
    else:
        return 'Bad magician!'


input = parser('A-small-attempt1.in')
case = 0
for s in input:
    case += 1
    print 'Case #'+str(case)+': ' + magic(s[0], s[1], s[2], s[3])
