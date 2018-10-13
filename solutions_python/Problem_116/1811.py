fin = open('f1.txt')

cases = int(fin.readline())

def count(r):
    global dot
    winner = 0
    h = {'X':0, 'O':0, '.':0, 'T':0}
    for i in xrange(0, 4):
        h[r[i]] += 1
    if h['X'] + h['T'] == 4:
        winner = 1
    elif h['O'] + h['T'] == 4:
        winner = 2

    if h['.'] > 0:
        dot = True
    return winner

dot    = False
fout = open('out.txt','w')
for x in xrange(0, cases):
    board = [fin.readline(), fin.readline(), fin.readline(), fin.readline()]
    score = []
    fin.readline()

    winner = 0
    dot    = False
    for i in xrange(0, 4):
        w = count(board[i])
        if w > 0:
            winner = w

    for i in xrange(0, 4):
        s = [board[j][i] for j in xrange(0, 4)]
        w = count(s)
        if w > 0:
            winner = w

    d = [board[i][i] for i in xrange(0, 4)]    
    w = count(d)
    if w > 0:
        winner = w

    h = count(d)
    if w > 0:
        winner = w

    #print "Winner: {} Dot: {}".format(winner, dot)
    if winner == 1:
        fout.write("Case #{}: X won\n".format(x + 1))
    elif winner == 2:
        fout.write("Case #{}: O won\n".format(x + 1))
    elif dot:
        fout.write("Case #{}: Game has not completed\n".format(x + 1))
    else:
        fout.write("Case #{}: Draw\n".format(x + 1))

