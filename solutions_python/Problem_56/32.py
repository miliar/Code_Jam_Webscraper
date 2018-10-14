import psyco
psyco.full()

name = 'A-large'
f = open(name+'.in')
fo = open(name + '.out','w')

T = int(f.next().strip())

mydict = {'.':0,'B':1,'R':2}

for t in xrange(T):
    N,K = [int(x) for x in f.next().strip().split()]
    board = [[mydict[s] for s in list(f.next().strip())] for i in xrange(N)]
    board2 = [[0 for i in xrange(N)] for j in xrange(N)]
    for i in xrange(N):
        which = N-1
        for j in xrange(N-1,-1,-1):
            if board[i][j]:
                board2[which][N-1-i] = board[i][j]
                which -= 1
    # check horizontals
    wins = [False,False]
    for i in xrange(N):
        j = 0
        while j < N:
            if board2[i][j]:
                val = board2[i][j]
                tot = 0
                while j < N and board2[i][j] == val:
                    tot += 1
                    j += 1
                
                if tot >= K:
                    wins[val-1] = True
            else:
                j += 1
    # check verticals
    for j in xrange(N):
        i = 0
        while i < N:
            if board2[i][j]:
                val = board2[i][j]
                tot = 0
                while i < N and board2[i][j] == val:
                    tot += 1
                    i += 1
                if tot >= K:
                    wins[val-1] = True
            else:
                i += 1
    # check diags
    for x in xrange(N):
        i = x
        j = 0
        while i < N:
            if board2[i][j]:
                val = board2[i][j]
                tot = 0
                while i < N and board2[i][j] == val:
                    tot += 1
                    i += 1
                    j += 1
                if tot >= K:
                    wins[val-1] = True
            else:
                i += 1
                j += 1
    for x in xrange(1,N):
        i = 0
        j = x
        while j < N:
            if board2[i][j]:
                val = board2[i][j]
                tot = 0
                while j < N and board2[i][j] == val:
                    tot += 1
                    i += 1
                    j += 1
                if tot >= K:
                    wins[val-1] = True
            else:
                i += 1
                j += 1
    for x in xrange(N):
        i = 0
        j = x
        while j > -1:
            if board2[i][j]:
                val = board2[i][j]
                tot = 0
                while j > -1 and board2[i][j] == val:
                    tot += 1
                    i += 1
                    j -= 1
                if tot >= K:
                    wins[val-1] = True
            else:
                i += 1
                j -= 1
    for x in xrange(1,N):
        i = x
        j = N-1
        while i < N:
            if board2[i][j]:
                val = board2[i][j]
                tot = 0
                while i < N and board2[i][j] == val:
                    tot += 1
                    i += 1
                    j -= 1
                if tot >= K:
                    wins[val-1] = True
            else:
                i += 1
                j -= 1
    fo.write('Case #%d: '%(t+1))
    if sum(wins) == 2:
        fo.write('Both\n')
    elif wins[0]:
        fo.write('Blue\n')
    elif wins[1]:
        fo.write('Red\n')
    else:
        fo.write('Neither\n')


f.close()
fo.close()
