case = int(raw_input())
for tt in range(1,case+1):
    size = raw_input().split()
    board = []
    ans = []
    can = True
    k = ''
    for i in range(int(size[1])+2):
        k+='o'
    board.append(k)
    for i in range(int(size[0])):
        ss = raw_input()
        board.append('o'+ss+'o')
        ans.append(str(ss))
    board.append(k)
    for i in range(len(board)):
        if(board[i].count('#')%2 != 0):
            can = False
            #print '1'
    for i in range(int(size[1])+2):
        c = 0
        for j in range(int(size[0])+2):
            if(board[j][i] == '#'):
                c += 1
        if(c%2 != 0):
            can = False
            #print '2'
            break
    for i in range(1,len(board)-1):
        for j in range(int(size[1])):
            if(board[i][j] == '#'):
                if not((board[i-1][j] == '#' or board[i+1][j] == '#') and (board[i][j+1] == '#' or board[i][j-1] == '#')):
                    can = False
                    #print '3'
    print 'Case #' + str(tt) + ':'
    if(can):
        p = []
        for i in range(len(ans)):
            p.append([])
            for j in range(len(ans[i])):
                p[i].append(ans[i][j])
        for i in range(len(p)):
            for j in range(len(p[i])):
                if(p[i][j] == '#'):
                    p[i][j] = '/'
                    p[i][j+1] = '\\'
                    p[i+1][j] = '\\'
                    p[i+1][j+1] = '/'
        for i in range(len(p)):
            k = ''
            for j in range(len(p[i])):
                k += p[i][j]
            print k
    else:
        print 'Impossible'
