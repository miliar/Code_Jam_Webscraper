fo = open('A-small-attempt1.in','rU');
fr = open('results.txt','w');

numTests = int(fo.readline().strip())
print numTests
X = ["XXXX", "XXXT", "XXTX", "XTXX", "TXXX"]
O = ["OOOO", "OOOT", "OOTO", "OTOO", "TOOO"]
D = "...."
k = 0
l = [D, D, D, D]
while (k < numTests):
    fr.write("Case #")
    fr.write('{0}'.format(k+1))
    fr.write(": ")
    l[0] = fo.readline().strip()
    l[1] = fo.readline().strip()
    l[2] = fo.readline().strip()
    l[3] = fo.readline().strip()
    fo.readline()
    if (l[0] in X or l[1] in X or l[2] in X or l[3] in X):
        fr.write("X won\n")
    elif (l[0] in O or l[1] in O or l[2] in O or l[3] in O):
        fr.write("O won\n")
    else:
        c1 = l[0][0] + l[1][0] + l[2][0] + l[3][0]
        c2 = l[0][1] + l[1][1] + l[2][1] + l[3][1]
        c3 = l[0][2] + l[1][2] + l[2][2] + l[3][2]
        c4 = l[0][3] + l[1][3] + l[2][3] + l[3][3]
        lr = l[0][0] + l[1][1] + l[2][2] + l[3][3]
        rl = l[3][0] + l[2][1] + l[1][2] + l[0][3]
        if (c1 in X or c2 in X or c3 in X or c4 in X or lr in X or rl in X):
            fr.write("X won\n")
        elif (c1 in O or c2 in O or c3 in O or c4 in O or lr in O or rl in O):
            fr.write("O won\n")
        else:
            unfinished = False
            for i in range(0,3):
                for j in range(0,3):
                    if (l[i][j] == '.'):
                        unfinished = True
            if (unfinished):
                fr.write("Game has not completed\n")
            else:
                fr.write("Draw\n");
    k+=1
fo.close()
fr.close()
