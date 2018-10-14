f = open('input1.txt')
lines = f.readlines()
f.close

cases = int(lines[0])
games = []
for x in range(cases):
    game = []
    for i in range(1,5):
        game.append(lines[5*x+i])
    games.append(game)

case = 1

def whoWon(game):
    xsd1 = 0
    osd1 = 0
    xsd2 = 0
    osd2 = 0
    empties = 0
    for i in range(4):
        xs1 = 0
        os1 = 0
        xs2 = 0
        os2 = 0
        if game[i][i] == 'X':
            xsd1 += 1
        if game[i][i] == 'O':
            osd1 += 1
        if game[i][i] == 'T':
            xsd1 += 1
            osd1 += 1
        if game[3-i][i] == 'X':
            xsd2 +=1
        if game[3-i][i] == 'O':
            osd2 +=1
        if game[3-i][i] == 'T':
            xsd2 +=1
            osd2 +=1
        for j in range(4):
            if game[i][j] == '.':
                empties += 1
            if game[i][j] == 'X':
                xs1 += 1
            if game[i][j] == 'O':
                os1 += 1
            if game[i][j] =='T':
                xs1 += 1
                os1 += 1
            if game[j][i] == 'X':
                xs2 += 1
            if game[j][i] == 'O':
                os2 += 1
            if game[j][i] =='T':
                xs2 += 1
                os2 += 1
        if xs1 == 4 or xs2 == 4:
            return 'X'
        if os1 == 4 or os2 == 4:
            return 'O'
    if xsd1 == 4 or xsd2 == 4:
        return 'X'
    if osd1 == 4 or osd2 == 4:
        return 'O'
    if empties == 0:
        return 'D'
    return 'G'


for x in range(cases):
    winner = whoWon(games[x])
    if winner == 'X':
        print("Case #" + str(x+1) + ": X won")
    elif winner == 'O':
        print("Case #" + str(x+1) + ": O won")
    elif winner == 'D':
        print("Case #" + str(x+1) + ": Draw")
    elif winner == 'G':
        print("Case #" + str(x+1) + ": Game has not completed")


