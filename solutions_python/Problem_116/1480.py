def someoneWon(result,the_list):
    symbols = set(the_list)
    if symbols <= set(['T','X']):
        return 'X'
    elif symbols <= set(['T','O']):
        return 'O'
    return result

with open('input.in') as f:
    
    outfile = open('outfile.out','w')
    n = int(f.readline())
    #print n
    for case in range(1,n+1):
        #print case
        result = '.'
        board = [[],[],[],[]]
        for row in range(4):
            board[row] = []
            for c in f.readline().strip():
                board[row].append(c)
        totalsym = set()
        for row in board:
            totalsym.update(row)

        for row in board:
            result = someoneWon(result,row)
        for column in range(4):
            result = someoneWon(result,[board[i][column] for i in range(4)])
        result = someoneWon(result,[board[i][i] for i in range(4)])
        result = someoneWon(result,[board[i][3-i] for i in range(4)])
        
        if result == 'X':
            outfile.write("Case #%d: X won\n" % case)
        elif result == 'O':
            outfile.write("Case #%d: O won\n" % case)
        elif '.' in totalsym:
            outfile.write("Case #%d: Game has not completed\n" % case)
        else:
            outfile.write("Case #%d: Draw\n" % case)
        f.readline()
    outfile.close()
        
        