cases = int(input())

for i in range(cases):
    row1 = int(input()) - 1
    grid1 = []
    for j in range (4):
        grid1.append(input().strip('\n').split(' '))
        for k in range(4):
            grid1[j][k] = int(grid1[j][k])
    
    initgrid = grid1[row1]

    row2 = int(input()) - 1
    grid2 = []
    for j in range (4):
        grid2.append(input().strip('\n').split(' '))
        for k in range(4):
            grid2[j][k] = int(grid2[j][k])

    fingrid = grid2[row2]

    counter = 0
    match = 0
    for element in initgrid:
        if (element in fingrid):
            counter += 1
            match = element

    if (counter == 0):
        print("Case #" + str(i + 1) + ": Volunteer cheated!")
    elif (counter == 1):
        print("Case #" + str(i + 1) + ": " + str(match) + "")
    else:
        print("Case #" + str(i + 1) + ": Bad magician!")
