input = open("/home/doohyunl/A-large.in", 'rb').readlines()

cases = int(input[0])

for case in xrange(cases):
    rows = [input[i+1] for i in xrange(case*5, case*5 + 4)]
    columns = [[] for i in xrange(4)]
    board = []
    for row in rows:
        for i in xrange(4):
            columns[i].append(row[i])
            board.append(row[i])
    columns = ["".join(column) for column in columns]
    diagonals = ["".join([rows[0][0], rows[1][1], rows[2][2], rows[3][3]]), "".join([rows[0][3], rows[1][2], rows[2][1], rows[3][0]])]
    x_wins = ['XXXX', 'TXXX', 'XTXX', 'XXTX', 'XXXT']
    o_wins = ['OOOO', 'TOOO', 'OTOO', 'OOTO', 'OOOT']
    status = ""
    won = 0
         
    for config in x_wins:
        for row in rows:
            if config in row:
                status = "X won"
                won = 1
        for column in columns:
            if config in column:
                status = "X won"
                won = 1
        for diagonal in diagonals:
            if config in diagonal:
                status = "X won"
                won = 1

    for config in o_wins:
        for row in rows:
            if config in row:
                status = "O won"
                won = 1
        for column in columns:
            if config in column:
                status = "O won"
                won = 1
        for diagonal in diagonals:
            if config in diagonal:
                status = "O won"
                won = 1
             

    if not won:
        if '.' in board:
            status = "Game has not completed"
        else:
            status = "Draw"

    print "Case #{0}: {1}".format(case+1, status)
        
     
    

