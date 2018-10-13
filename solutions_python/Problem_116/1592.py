f = open("input.txt","r")
t = int(f.readline())
out = open("output.txt","w")
for a in xrange(t):
    mat = []
    for i in xrange(4):
        j = f.readline()[:4]
        mat.append(j)
    x = 0
    o = 0
    draw = 0
    gnc = 0
    flag = 0
    for i in xrange(4):
        for j in xrange(4):
            cur = mat[i][j]
            if mat[i][j] == '.':
                draw = -1
            if j+1 < 4 and j+2 < 4 and j+3 < 4 and (cur == 'X' or cur == 'O'):
                if mat[i][j+1] == cur or mat[i][j+1] == 'T':
                    if mat[i][j+2] == cur or mat[i][j+2] == 'T':
                        if mat[i][j+3] == cur or mat[i][j+3] == 'T':
                            if cur == 'X':
                                x = 1
                                flag = 1
                                break
                            else:
                                o = 1
                                flag = 1
                                break
            if i+1 < 4 and i+2 < 4 and i+3 < 4 and (cur == 'X' or cur == 'O'):
                if mat[i+1][j] == cur or mat[i+1][j] == 'T':
                    if mat[i+2][j] == cur or mat[i+2][j] == 'T':
                        if mat[i+3][j] == cur or mat[i+3][j] == 'T':
                            if cur == 'X':
                                x = 1
                                flag = 1
                                break
                            else:
                                o = 1
                                flag = 1
                                break
            if i+1 < 4 and i+2 < 4 and i+3 < 4 and j+1 < 4 and j+2 < 4 and j+3 < 4 and (cur == 'X' or cur == 'O'):
                if mat[i+1][j+1] == cur or mat[i+1][j+1] == 'T':
                    if mat[i+2][j+2] == cur or mat[i+2][j+2] == 'T':
                        if mat[i+3][j+3] == cur or mat[i+3][j+3] == 'T':
                            if cur == 'X':
                                x = 1
                                flag = 1
                                break
                            else:
                                o = 1
                                flag = 1
                                break
            if i+1 < 4 and i+2 < 4 and i+3 < 4 and j-1 >= 0 and j-2 >= 0 and j-3 >= 0 and (cur == 'X' or cur == 'O'):
                if mat[i+1][j-1] == cur or mat[i+1][j-1] == 'T':
                    if mat[i+2][j-2] == cur or mat[i+2][j-2] == 'T':
                        if mat[i+3][j-3] == cur or mat[i+3][j-3] == 'T':
                            if cur == 'X':
                                x = 1
                                flag = 1
                                break
                            else:
                                o = 1
                                flag = 1
                                break
            
            if flag == 1:
                break
    if flag == 0 and draw == -1:
        gnc = 1
    elif flag == 0:
        draw = 1
    if x == 1:
        wr = "Case #"+str(a+1)+": X won\n"
    elif o == 1:
        wr = "Case #"+str(a+1)+": O won\n"
    elif draw == 1:
        wr = "Case #"+str(a+1)+": Draw\n"
    elif gnc == 1:
        wr = "Case #"+str(a+1)+": Game has not completed\n"
    out.write(wr)
    f.readline()
f.close()
out.close()
