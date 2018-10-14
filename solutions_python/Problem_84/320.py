import sys
import math

fi = open("input.txt", "r")
fo = open("output.txt", "w")

def which_letter(i, j):
    if i == 0 and j == 0: return '/'
    else:
        if i == 0 and j == 1: return 'a'
        else:
            if i == 1 and j == 0: return 'a'
            else: return '/'

c = int(fi.readline().strip());
for tc in range(1, c + 1):
    tmp = list(map(int, fi.readline().strip().split(" ")))
    row, col = tmp[0], tmp[1]
    board = [' '*col]*row

    for r in range(0, row):
        tmp = fi.readline().strip()
        board[r] = tmp

    for r in range(0, row):
        for c in range(0, col):
            if board[r][c] == '#':
                ok = True
                for i in range(0,2):
                    for j in range(0,2):
                        if (r+i) >=  row or (c+j) >= col or board[r+i][c+j] != '#':
                            ok = False
                if ok:
                    tmp = list(board[r])
                    tmp2 = list(board[r+1])
                    tmp[c] = '/'
                    tmp[c+1] = '\\'
                    board[r] = "".join(tmp)
                    tmp2[c] = '\\'
                    tmp2[c+1] = '/'
                    board[r+1] = "".join(tmp2)

    ok = True
    for r in range(0, row):
        for c in range(0, col):
            if board[r][c] == "#":
                ok = False
    if ok == True:
        fo.write("Case #{0}:\n".format(tc))
        for r in range(0, row):
            for c in range(0, col):
                fo.write(board[r][c])
            fo.write("\n")
    else:
        fo.write("Case #{0}:\n{1}\n".format(tc, "Impossible"))
    
fi.close()
fo.close()