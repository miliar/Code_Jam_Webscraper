from collections import deque as Queue


def solve(g):
    players = ['X', 'O']
    
    seqs = getseqs(g)
    winner = checkseqs(seqs, players)
    done = checkdone(g)
    if winner == 'X':
        return 'X won'
    elif winner == 'O':
        return 'O won'
    elif done:
        return 'Draw'
    else:
        return 'Game has not completed'


def getseqs(g):
    seqs = set()
    for row in g:
        rowseq = row
        seqs.add(rowseq)
    for i in range(len(g[0])):
        colseq = ''.join([row[i] for row in g])
        seqs.add(colseq)
        
    diag1seq = str(''.join([g[i][i] for i in range(4)]))
    seqs.add(diag1seq)
    diag2seq = str(''.join([g[i][4-i-1] for i in range(4)]))
    seqs.add(diag2seq)
    return seqs

def checkseqs(seqs, plrs):
    for plr in plrs:
        for seq in seqs:
            if seq.count(plr) >= 4:
                return plr
            elif seq.count(plr) >= 3 and seq.count('T') >= 1:
                return plr
    return 'N'

def checkdone(g):
    for row in g:
        if row.count('.'):
            return False
    return True



inp = raw_input()
T = int(inp)
for t in range(1,T+1):
    grid = []

    for i in range(4):
        inp = raw_input()
        row = str(inp)
        grid.append(row)
    inp = raw_input()
    answer = solve(grid)
    print "Case #" + str(t) + ": " + str(answer)
