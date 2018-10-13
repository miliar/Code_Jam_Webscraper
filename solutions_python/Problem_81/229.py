import sys
import math

fi = open("input.txt", "r")
fo = open("output.txt", "w")

c = int(fi.readline().strip());
for tc in range(1, c + 1):
    tmp = list(map(int, fi.readline().strip().split(" ")))
    n = tmp[0]
    board = [""] * n
    for i in range (0, n):
        board[i] = fi.readline().strip()

    wp = [0] * n
    for i in range (0, n):
        matches = 0
        wins = 0
        for j in range (0, n):
            if i != j:
                if board[i][j] == '1' or board[i][j] == '0':
                    matches += 1
                    wins += int(board[i][j])
        wp[i] = (1.0*wins) / (1.0*matches)

    owp = [0] * n
    for i in range (0, n):
        total = 0
        cnt = 0
        for j in range (0, n):
            if i != j and (board[i][j] == '1' or board[i][j] == '0'):
                cnt += 1
                tt, ct = 0, 0
                for k in range(0,n):
                    if (board[j][k] == '1' or board[j][k] == '0') and k != i:
                        tt += 1
                        ct += int(board[j][k])
                total += ct*1.0 / tt
        owp[i] = (1.0*total) / (cnt)

    oowp = [0] * n
    for i in range (0, n):
        total = 0
        cnt = 0
        for j in range (0, n):
            if i != j and (board[i][j] == '1' or board[i][j] == '0'):
                cnt += 1
                total += owp[j]
        oowp[i] = (1.0*total) / cnt
        
    fo.write("Case #{0}:\n".format(tc))
    for i in range (0, n):
        fo.write("{0}\n".format(0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]))
    
fi.close()
fo.close()