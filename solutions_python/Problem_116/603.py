def check(game, P):
    win = ['T'+P+P+P,P+'T'+P+P,P+P+'T'+P,P+P+P+'T',P+P+P+P]

    #check rows
    for line in game:
        if line in win:
            return True

    #check cols
    for i in range(4):
        line = game[0][i]+game[1][i]+game[2][i]+game[3][i];
        if line in win:
            return True

    #check diagonals
    d = game[0][0]+game[1][1]+game[2][2]+game[3][3];
    if d in win:
        return True
    d = game[0][3]+game[1][2]+game[2][1]+game[3][0];
    if d in win:
        return True

    return False


def blank_space(game):
    for line in game:
        if line.find('.') != -1:
            return True
    return False

f = open('A-large.in', 'r')

output = open('output.txt','w')

T = int(f.readline())

#print(T)

for i in range(1,T+1):
    game = []
    game.append(f.readline().rstrip())
    game.append(f.readline().rstrip())
    game.append(f.readline().rstrip())
    game.append(f.readline().rstrip())
    f.readline()

    if(check(game,'X') == True):
        result = "X won"
    elif(check(game,'O') == True):
        result = "O won"
    elif(blank_space(game) == True):
        result = "Game has not completed"
    else:
        result = "Draw"

    #print(game)

    text = 'Case #'+str(i)+': '+result

    print(text,file=output)
    #print(text)

    #print()

f.close()
output.close()

#print(lines)
