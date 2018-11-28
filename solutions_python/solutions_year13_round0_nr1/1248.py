file1 = open("A-large.in")
text1 = file1.read().split()
text = []
for i in range(len(text1)):
    if (i%4==0):
        text.append([text1[i], text1[i+1], text1[i+2], text1[i+3]])
i = 1
X_win = [['T', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]
O_win = [['O', 'O', 'O', 'T'], ['O', 'O', 'O', 'O']]

for game in text:

    # Diagonals
    diagonal1 = sorted(game[0][0] + game[1][1] + game[2][2] + game[3][3])
    diagonal2 = sorted(game[0][3] + game[1][2] + game[2][1] + game[3][0])
    if diagonal1 in X_win or diagonal2 in X_win:
        print ("Case #", i, ": X won", sep='')
        i += 1
        continue
    elif diagonal1 in O_win or diagonal2 in O_win:
        print ("Case #", i, ": O won", sep='')
        i += 1
        continue

    # Horizontal lines
    elif sorted(game[0]) in X_win or sorted(game[1]) in X_win or sorted(game[2]) in X_win or sorted(game[3]) in X_win:
        print ("Case #", i, ": X won", sep='')
        i += 1
        continue
    elif sorted(game[0]) in O_win or sorted(game[1]) in O_win or sorted(game[2]) in O_win or sorted(game[3]) in O_win:
        print ("Case #", i, ": O won", sep='')
        i += 1
        continue

    # Vertical lines
    else:
        line0 = sorted(game[0][0] + game[1][0] + game[2][0] + game[3][0])
        line1 = sorted(game[0][1] + game[1][1] + game[2][1] + game[3][1])
        line2 = sorted(game[0][2] + game[1][2] + game[2][2] + game[3][2])
        line3 = sorted(game[0][3] + game[1][3] + game[2][3] + game[3][3])
        if line0 in X_win or line1 in X_win or line2 in X_win or line3 in X_win:
            print ("Case #", i, ": X won", sep='')
            i += 1
            continue
        elif line0 in O_win or line1 in O_win or line2 in O_win or line3 in O_win:
            print ("Case #", i, ": O won", sep='')
            i += 1
            continue

    # Draw
    if '.' not in game[0]+game[1]+game[2]+game[3]:
        print ("Case #", i, ": Draw", sep='')
        i += 1
        continue

    # Incomplete game
    else:
        print ("Case #", i, ": Game has not completed", sep='')
        i += 1
        continue
