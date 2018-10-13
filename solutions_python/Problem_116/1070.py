

f = open('A-large.in')

outfile = open('1.out', 'w')

for case in xrange(int(f.readline())):
    orig = []
    for r in xrange(4):
        orig.append(list(f.readline().strip()))
    fullMap = True
    gameOver = False
    for player in ('X', 'O'):
        new = []
        for i in xrange(4):
            r = orig[i]
            new.append([])
            for c in r:
                if c == player:
                    new[i].append(1)
                elif c == 'T':
                    new[i].append(1)
                elif c == '.':
                    fullMap = False
                    new[i].append(0)
                else:
                    new[i].append(0)
        # horizontal
        for r in xrange(4):
            if sum(new[r]) == 4:
                outfile.write('Case #%d: %s won' % (case+1, player))
                gameOver = True
                break
        if gameOver: break
        for c in xrange(4):
            if sum([new[r][c] for r in xrange(4)]) == 4:
                outfile.write('Case #%d: %s won' % (case+1, player))
                gameOver = True
                break
        if gameOver: break
        # diagonal
        if sum([new[r][r] for r in xrange(4)]) == 4:
            outfile.write('Case #%d: %s won' % (case+1, player))
            gameOver = True
            break
            
        elif new[3][0] + new[2][1] + new[1][2] + new[0][3] == 4:
            outfile.write('Case #%d: %s won' % (case+1, player))
            gameOver = True
            break
    if not gameOver:
        if fullMap:
            outfile.write('Case #%d: Draw' % (case+1,))
        else:
            outfile.write('Case #%d: Game has not completed' % (case+1,))
    outfile.write('\n')
    f.readline()



outfile.close()
f.close()
