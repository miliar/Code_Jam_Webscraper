# Google Code Jam 2014 Qualifying question A

infile = open('A-small-attempt3.in', 'r')
outfile = open('A_small.txt', 'w')

n = infile.readline()

for case in range(1, int(n) + 1):
    grid1, grid2 = [], []
    answer1 = infile.readline()
    for j in range(4):
        line = infile.readline()
        line = line.split(' ')
        grid1.append(line[:-1] + [line[-1][:-1]])
    answer2 = infile.readline()
    for k in range(4):
        line = infile.readline()
        line = line.split(' ')
        grid2.append(line[:-1] + [line[-1][:-1]])
    matching = []
    for card in grid1[int(answer1) - 1]:
        for card2 in grid2[int(answer2) - 1]:
            if card == card2:
                matching.append(card)
    if len(matching) == 0:
        output = 'Case #{0}: Volunteer cheated!'.format(str(case))
    elif len(matching) == 1:
        output = 'Case #{0}: {1}'.format(str(case), str(matching[0]))
    else:
        output = 'Case #{0}: Bad magician!'.format(str(case))
    print(output)
    outfile.write(output + '\n')

infile.close()
outfile.close()
