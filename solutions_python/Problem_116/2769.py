f = open ('TicTacToe.txt','r')
f1 = open('OutTicTacToe.txt','w')

cases = int(f.readline())

for a in range(cases):
    grid = []
    for i in range(4):
        ln = f.readline()
        grid.append(list(ln.strip()))
    ln=f.readline()

    #Check Horrizontal
    Ohorr = False
    Xhorr = False
    Incom = False
    for i in range(4):
        if Xhorr == True or Ohorr == True: break
        if grid [i][0] != 'T':
            first = grid[i][0]
        else: first = grid[i][1]
        
        counter = 0
        for j in range(1,4):
            if grid[i][j] == '.' or first == '.':
                Incom = True
                break
            if grid[i][j] != first and grid[i][j] != 'T':
                break
            else:counter +=1
        if counter == 3:
            if first == 'X':
                Xhorr = True
                #print('X WINS')
            else:
                Ohorr = True
                #print('O WINS')

    #Check Vertical
    Over = False
    Xver = False
    for i in range(4):
        if Xver == True or Over == True: break
        if grid[0][i] != 'T':
            first = grid [0][i]
        else: first = grid [1][i]

        counter = 0
        for j in range (1,4):
            if grid[j][i] == '.' or first == '.':
                Incom = True
                break
            if grid[j][i] != first and grid [j][i] != 'T':
                break
            else:
                counter +=1
        if counter == 3:
            if first == 'X':
                Xver = True
                #print ('X WINS')                
            else:
                Over = True
                #print('O WINS')                

    Odiag = False
    Xdiag = False
    if Ohorr != True and Over != True and Xhorr != True and Xver != True: 
        #Check Diagonal        
        #Top left to bottom right
        if grid[0][0] == 'T':
            first = grid[1][1]
        else: first = grid [0][0]
        if first != '.':       
            if grid [1][1] == first or grid [1][1] == 'T':
                if grid [2][2] == first or grid [2][2] == 'T':
                    if grid [3][3] == first or grid [3][3] == 'T':
                        if first == 'O':
                            Odiag = True
                            #print ('O WINS')
                        else:
                            Xdiag = True
                            #print ('X WINS')
        
        if Odiag == False and Xdiag == False:
            #Top right to bottom left
            if grid[0][3] == 'T':
                first = grid[1][2]
            else: first = grid [0][3]
            if first != '.':
                if grid [1][2] == first or grid [1][2] == 'T':
                    if grid [2][1] == first or grid [2][1] == 'T':
                        if grid [3][0] == first or grid [3][0] == 'T':
                            if first == 'O':
                                Odiag = True
                                #print('O WINS')
                            else:
                                Xdiag = True
                                #print ('X WINS')

    if Ohorr == True or Over == True or Odiag == True:
        print('Case #' + str(a+1) + ': ' + 'O won', file = f1)
    elif Xhorr == True or Xver == True or Xdiag == True:
        print('Case #' + str(a+1) + ': ' + 'X won', file = f1)
    elif Ohorr == False and Xhorr == False and Over == False and Xver == False and Odiag == False and Xdiag == False and Incom == True:
        print ('Case #' + str(a+1) + ': ' + 'Game has not completed', file = f1)
    elif Ohorr == False and Xhorr == False and Over == False and Xver == False and Odiag == False and Xdiag == False and Incom == False: print ('Case #' + str(a+1) + ': ' + 'Draw', file = f1)
    
f1.close()
