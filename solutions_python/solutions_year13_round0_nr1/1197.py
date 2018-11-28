def line(datalist, indexvect):
    vector = [];
    for element in indexvect:
        vector.append(datalist[element]);
    return vector

fo = open("largeinput.txt", "r")
fout = open("outputlarge", "wb")

N = int(fo.readline());

for i in range(N):
    # Solve a game
    board = [];
    for j in range(4):
        board += fo.readline(4);
        fo.readline();

    # X & O boards
    Xboard = range(16);
    Oboard = range(16);
    for k in range(16):
        element = board[k];
        if element == 'X':
            Xboard[k] = 1;
            Oboard[k] = 0;
        elif element == 'O':
            Xboard[k] = 0;
            Oboard[k] = 1;
        elif element == 'T':
            Xboard[k] = 1;
            Oboard[k] = 1;
        else:
            Xboard[k] = 0;
            Oboard[k] = 0;

    Winner = "Noone";
    
    # Horizontal
    for l in range(4):
        index = range(4);
        for m in range(4):
            index[m] += 4*l;
        if sum(line(Xboard,index)) == 4:
            Winner = "X won\n"
        elif sum(line(Oboard,index)) == 4:
            Winner = "O won\n"
            
    # Vertical
    for l in range(4):
        index = [0,4,8,12];
        for m in range(4):
            index[m] += l;
        if sum(line(Xboard,index)) == 4:
            Winner = "X won\n"
        elif sum(line(Oboard,index)) == 4:
            Winner = "O won\n"

    # Diagonal
    index = [0, 5, 10, 15];
    if sum(line(Xboard,index)) == 4:
        Winner = "X won\n"
    elif sum(line(Oboard,index)) == 4:
        Winner = "O won\n"

    index = [3, 6, 9, 12];
    if sum(line(Xboard,index)) == 4:
        Winner = "X won\n"
    elif sum(line(Oboard,index)) == 4:
        Winner = "O won\n"  

    if Winner == "Noone":
        if "." in board:
            Winner = "Game has not completed\n";
        else:
            Winner = "Draw\n";
            
    fo.readline();  # Read the empty line
    
    # Write to output
    fout.write('Case #')
    fout.write(str(i+1))
    fout.write(': ')
    fout.write(Winner)
    

fo.close()
fout.close()
