filein = open("A-large.in", 'r')
fileout = open("output.txt", 'w')

test_cases = int(filein.readline())

for test_case in range(test_cases):
    grid = list()
    for i in range(4):
        grid.append(filein.readline().strip())
    filein.readline()
    
    whoWon = ""
    #counting the rows
    for i in range(4):
        Xocc, Oocc, Tocc = 0, 0, 0
        for j in range(4):
            if grid[i][j] == 'X': Xocc += 1
            if grid[i][j] == 'O': Oocc += 1
            if grid[i][j] == 'T': Tocc += 1
        if Xocc == 4 or (Xocc == 3 and Tocc == 1):
            whoWon = "X won"
            break
        elif Oocc == 4 or (Oocc == 3 and Tocc == 1):
            whoWon = "O won"
            break
    
    if whoWon == "X won":
        fileout.write("Case #{}: X won\n".format(test_case+1))
        continue
    elif whoWon == "O won":
        fileout.write("Case #{}: O won\n".format(test_case+1))
        continue
    
    #counting the columns
    for i in range(4):
        Xocc, Oocc, Tocc = 0, 0, 0
        for j in range(4):
            if grid[j][i] == 'X': Xocc += 1
            if grid[j][i] == 'O': Oocc += 1
            if grid[j][i] == 'T': Tocc += 1
        if Xocc == 4 or (Xocc == 3 and Tocc == 1):
            whoWon = "X won"
            break
        elif Oocc == 4 or (Oocc == 3 and Tocc == 1):
            whoWon = "O won"
            break
    
    if whoWon == "X won":
        fileout.write("Case #{}: X won\n".format(test_case+1))
        continue
    elif whoWon == "O won":
        fileout.write("Case #{}: O won\n".format(test_case+1))
        continue
    
    #counting the diagonals
    Xocc, Oocc, Tocc = 0, 0, 0
    for i in range(4):
        if grid[i][i] == 'X': Xocc += 1
        if grid[i][i] == 'O': Oocc += 1
        if grid[i][i] == 'T': Tocc += 1
        
        if Xocc == 4 or (Xocc == 3 and Tocc == 1):
            whoWon = "X won"
            break
        elif Oocc == 4 or (Oocc == 3 and Tocc == 1):
            whoWon = "O won"
            break
     
    if whoWon == "X won":
        fileout.write("Case #{}: X won\n".format(test_case+1))
        continue
    elif whoWon == "O won":
        fileout.write("Case #{}: O won\n".format(test_case+1))
        continue
       
    
    #counting the reversed diagonals
    Xocc, Oocc, Tocc = 0, 0, 0
    for i in range(4):
        if grid[3-i][i] == 'X': Xocc += 1
        if grid[3-i][i] == 'O': Oocc += 1
        if grid[3-i][i] == 'T': Tocc += 1
        
        if Xocc == 4 or (Xocc == 3 and Tocc == 1):
            whoWon = "X won"
            break
        elif Oocc == 4 or (Oocc == 3 and Tocc == 1):
            whoWon = "O won"
            break
    
    
    if whoWon == "X won":
        fileout.write("Case #{}: X won\n".format(test_case+1))
        continue
    elif whoWon == "O won":
        fileout.write("Case #{}: O won\n".format(test_case+1))
        continue
       
    
    dotOcc = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == '.':
                dotOcc += 1
    
    if dotOcc == 0:
        fileout.write("Case #{}: Draw\n".format(test_case+1))
    else:
        fileout.write("Case #{}: Game has not completed\n".format(test_case+1))
        
    
            