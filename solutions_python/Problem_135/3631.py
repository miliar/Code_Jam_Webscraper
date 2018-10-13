n = 'E:\code\input'
o = 'E:\code\output'
fin = open(n, 'r', 0)
fout = open ( o, 'w', 0)
line = fin.readline()
for gameNumber in range(int(line)):
    game = []
    for linenumberingame in range(10):
        line = fin.readline()
        x = line[:-1]
        x = x.split()
        newx = []
        for each in x:
            newx.append(int(each))
        x = newx
        game.append(x)
    strow = game[game[0][0]]
    ndrow = game[game[5][0]+5]
    res = []
    for st in strow:
        for nd in ndrow:
            if st == nd :
                res.append(nd)
            else:
                pass
    ##result :D
    length = len(res)
    if length == 0:
        aaa = 'case #' + str(gameNumber+1) + ': ' + 'Volunteer cheated!\n'
        fout.write(aaa)
    elif length ==1:
        aaa = 'case #' + str(gameNumber+1) + ': ' + str(res[0]) +'\n'
        fout.write(aaa)
    else:
        aaa = 'case #' + str(gameNumber+1) + ': ' + 'Bad magician!\n'
        fout.write(aaa)
fout.close()
fin.close()
