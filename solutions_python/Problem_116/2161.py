f = open('A-large-1.in', 'r')
n = int(f.readline().strip())
output = ''
for i in range(n):
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    line3 = f.readline().strip()
    line4 = f.readline().strip()
    board = [line1, line2, line3, line4]
    pts = {'X':1, 'O':-1, 'T':0, '.':-1000}
    winner = ''
    unfin = ''
    
    for j in [0,1,2,3]:
        vscore = 0
        hscore = 0
        if winner:
            break
        for y in [0,1,2,3]:
            vscore += pts[board[j][y]]
            hscore += pts[board[y][j]]
        if vscore >= 3 or hscore >= 3:
            winner = 'X'
        elif (vscore < -2 and vscore > -5) or (hscore < -2 and hscore > -5):
            winner = 'O'
        elif vscore < -900 or hscore < -900:
            unfin = 'Y'
    fscore = 0
    sscore = 0
    
    for j in [0,1,2,3]:
        fscore += pts[board[j][j]]
        sscore += pts[board[j][3-j]]
    if i > 0:
        output += '\n'
    if fscore >= 3 or sscore >= 3:
        winner = 'X'
    elif (fscore < -2 and fscore > -5) or (sscore < -2 and sscore > -5):
        winner = 'O'
    elif sscore < -900 or fscore < -900:
        unfin = 'Y'
    if winner:
        output += 'Case #' + str(i +1) + ': ' + winner + ' won'
    elif unfin:
        output += 'Case #' + str(i +1) + ': Game has not completed'
    else:
        output += 'Case #' + str(i +1) + ': Draw'
    f.readline()
f.close()
f = open('A-large-1.out', 'w')
f.write(output)
f.close()
            