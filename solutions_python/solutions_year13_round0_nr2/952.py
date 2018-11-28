cas = int(raw_input().strip())
for cc in range(1,cas+1):
    inp = raw_input().strip().split()
    row = int(inp[0])
    col = int(inp[1])
    lawn = []
    for i in range(row):
        tmp = []
        t_inp = raw_input().strip().split()
        for ii in t_inp:
            tmp.append(int(ii))
        lawn.append(tmp)
    print 'Case #' + str(cc) + ':',
    ans = True
    for r in range(row):
        for c in range(col):
            #by col
            for i in range(col):
                if(lawn[r][i] > lawn[r][c]):
                    #by row
                    for ii in range(row):
                        if(lawn[ii][c] > lawn[r][c]):
                            ans = False
    if(ans):
        print 'YES'
    else:
        print 'NO'
