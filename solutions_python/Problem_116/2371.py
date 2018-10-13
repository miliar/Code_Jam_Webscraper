import sys;

t = int(sys.stdin.readline());
for i in range(t):
    matrix = [[0,0,0,0] for _ in range(4)];
    for j in range(4):
        line = sys.stdin.readline();
        matrix[j][0] = line[0];
        matrix[j][1] = line[1];
        matrix[j][2] = line[2];
        matrix[j][3] = line[3];
    winner = "Draw";
    done = False;
    for j in range(4):
        if (matrix[j][0] == 'X' or matrix[j][0] == 'T') and (matrix[j][1] == 'X' or matrix[j][1] == 'T') and            (matrix[j][2] == 'X' or matrix[j][2] == 'T') and            (matrix[j][3] == 'X' or matrix[j][3] == 'T'):
            winner = "X won";
            done = True;
            break;
        if (matrix[j][0] == 'O' or matrix[j][0] == 'T') and            (matrix[j][1] == 'O' or matrix[j][1] == 'T') and            (matrix[j][2] == 'O' or matrix[j][2] == 'T') and            (matrix[j][3] == 'O' or matrix[j][3] == 'T'):
            winner = "O won";
            done = True;
            break;
        if matrix[j][0] == '.' or            matrix[j][1] == '.' or           matrix[j][2] == '.' or           matrix[j][3] == '.':
            winner = "Game has not completed";
    if done == False:
        for j in range(4):
            if (matrix[0][j] == 'X' or matrix[0][j] == 'T') and                (matrix[1][j] == 'X' or matrix[1][j] == 'T') and                (matrix[2][j] == 'X' or matrix[2][j] == 'T') and                (matrix[3][j] == 'X' or matrix[3][j] == 'T'):
                winner = "X won";
                done = True;
                break;
            if (matrix[0][j] == 'O' or matrix[0][j] == 'T') and                (matrix[1][j] == 'O' or matrix[1][j] == 'T') and                (matrix[2][j] == 'O' or matrix[2][j] == 'T') and                (matrix[3][j] == 'O' or matrix[3][j] == 'T'):
                winner = "O won";
                done = True;
                break;
    if done == False:
        if (matrix[0][0] == 'X' or matrix[0][0] == 'T') and            (matrix[1][1] == 'X' or matrix[1][1] == 'T') and            (matrix[2][2] == 'X' or matrix[2][2] == 'T') and            (matrix[3][3] == 'X' or matrix[3][3] == 'T'):
            winner = "X won";
        if (matrix[0][3] == 'X' or matrix[0][3] == 'T') and            (matrix[1][2] == 'X' or matrix[1][2] == 'T') and            (matrix[2][1] == 'X' or matrix[2][1] == 'T') and            (matrix[3][0] == 'X' or matrix[3][0] == 'T'):
            winner = "X won";
        if (matrix[0][0] == 'O' or matrix[0][0] == 'T') and            (matrix[1][1] == 'O' or matrix[1][1] == 'T') and            (matrix[2][2] == 'O' or matrix[2][2] == 'T') and            (matrix[3][3] == 'O' or matrix[3][3] == 'T'):
            winner = "O won";
        if (matrix[0][3] == 'O' or matrix[0][3] == 'T') and            (matrix[1][2] == 'O' or matrix[1][2] == 'T') and            (matrix[2][1] == 'O' or matrix[2][1] == 'T') and            (matrix[3][0] == 'O' or matrix[3][0] == 'T'):
            winner = 'O won';
    line = sys.stdin.readline();
    print('Case #{0}: {1}'.format(i+1, winner));




