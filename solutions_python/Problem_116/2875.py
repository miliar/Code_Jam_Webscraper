def grouper(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

inputfile = open('A-small-attempt0.in', 'r')
lines = inputfile.readlines()
inputfile.close()

n = 0
outputfile = open('output.txt', 'w')

for game in grouper(lines, 5):
    Xwon = 0
    Owon = 0
    draw = 1
    incomplete = 0
    n = n + 1

    for i in range(4):

        #columns
        if game[1][i]=='O' or game[1][i]=='T':
            if game[2][i]=='O' or game[2][i]=='T':
                if game[3][i]=='O' or game[3][i]=='T':
                    if game[4][i]=='O' or game[4][i]=='T':
                        Owon = 1
                        draw = 0
                        
        if game[1][i]=='X' or game[1][i]=='T':
            if game[2][i]=='X' or game[2][i]=='T':
                if game[3][i]=='X' or game[3][i]=='T':
                    if game[4][i]=='X' or game[4][i]=='T':
                        Xwon = 1
                        draw = 0

        #rows
        j=i+1
        if game[i][0]=='O' or game[i][0]=='T':
            if game[i][1]=='O' or game[i][1]=='T':
                if game[i][2]=='O' or game[i][2]=='T':
                    if game[i][3]=='O' or game[i][3]=='T':
                        Owon = 1
                        draw = 0
                        
        if game[i][0]=='X' or game[i][0]=='T':
            if game[i][1]=='X' or game[i][1]=='T':
                if game[i][2]=='X' or game[i][2]=='T':
                    if game[i][3]=='X' or game[i][3]=='T':
                        Xwon = 1
                        draw = 0

        #diagonals
        if game[1][0]=='X' or game[1][0]=='T':
            if game[2][1]=='X' or game[2][1]=='T':
                if game[3][2]=='X' or game[3][2]=='T':
                    if game[4][3]=='X' or game[4][3]=='T':
                        Xwon = 1
                        draw = 0

        if game[1][0]=='O' or game[1][0]=='T':
            if game[2][1]=='O' or game[2][1]=='T':
                if game[3][2]=='O' or game[3][2]=='T':
                    if game[4][3]=='O' or game[4][3]=='T':
                        Owon = 1
                        draw = 0
                        
        if game[1][3]=='X' or game[1][3]=='T':
            if game[2][2]=='X' or game[2][2]=='T':
                if game[3][1]=='X' or game[3][1]=='T':
                    if game[4][0]=='X' or game[4][0]=='T':
                        Xwon = 1
                        draw = 0
                        
        if game[1][3]=='O' or game[1][3]=='T':
            if game[2][2]=='O' or game[2][2]=='T':
                if game[3][1]=='O' or game[3][1]=='T':
                    if game[4][0]=='O' or game[4][0]=='T':
                        Owon = 1
                        draw = 0

        if draw:
            for x in range (4):
                for y in range (1,5):
                    if game[y][x] == '.':
                        incomplete = 1
                        draw = 0
            

    if Owon:
        outputfile.write("Case #" + str(n) + ": O won\n")
        incomplete = 0
    if Xwon:
        outputfile.write("Case #" + str(n) + ": X won\n")
        incomplete = 0
    if draw:
        outputfile.write("Case #" + str(n) + ": Draw\n")
        incomplete = 0
    if incomplete:
        outputfile.write("Case #" + str(n) + ": Game has not completed\n")
outputfile.close()                   
        
    
