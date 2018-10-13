inp = open('A-small.in', 'r')
out = open('A-small.out', 'w')

cases = int(inp.readline().strip())

for x in range(cases):
    row1 = int(inp.readline().strip())
    grid1 = [[],[],[],[]]
    currentnum = ''

    for a in range(4):
        line = inp.readline().strip() + ' '
        for b in line:
            if b != ' ':
                currentnum = currentnum + b
            else:
                grid1[a].append(int(currentnum))
                currentnum = ''

    potential1 = grid1[row1-1]

    row2 = int(inp.readline().strip())
    grid2 = [[],[],[],[]]
    currentnum = ''

    for a in range(4):
        line = inp.readline().strip() + ' '
        for b in line:
            if b != ' ':
                currentnum = currentnum + b
            else:
                grid2[a].append(int(currentnum))
                currentnum = ''

    potential2 = grid2[row2-1]

    combined = 0
    combnum = 0

    for c in potential1:
        if c in potential2:
            combined += 1
            combnum = c

    if combined == 0:
        print("Case #" + str(x+1) + ": Volunteer cheated!")
        out.write("Case #" + str(x+1) + ": Volunteer cheated!\n")
    elif combined == 1:
        print("Case #" + str(x+1) + ": " + str(combnum))
        out.write("Case #" + str(x+1) + ": " + str(combnum) + "\n")
    else:
        print("Case #" + str(x+1) + ": Bad magician!")
        out.write("Case #" + str(x+1) + ": Bad magician!\n")

inp.flush()
out.flush()
inp.close()
out.close()
