from copy import copy, deepcopy

def check_winner(row):
    w = ""
    if row == "XXXX" or row == "TXXX":
        w = "X won"
    elif row == "OOOO" or row == "OOOT":
        w = "O won"
    return w

def test(tc):
    rows = []
    winner = ''
    draw = True
    
    for r in range(4):
        row = raw_input()
        rows.insert(r,list(row))

    for row in rows:
        for col in row:
            if draw and col == ".":
                draw = False

    # check rows
    tmp_rows = deepcopy(rows)
    for trows in tmp_rows:
        trows.sort()
        row = "".join(str(x) for x in trows)
        if winner == "":
            winner = check_winner(row)

    if winner == "":
        tmp_rows = zip(*rows)
        for tr in tmp_rows:
            trows = list(tr)
            trows.sort()
            row = "".join(str(x) for x in trows)
            if winner == "":
                winner = check_winner(row)
                
    if winner == "":
        diag1 = ""
        rrows = []
        for i in range(4):
            diag1 = diag1 + rows[i][i]
            rrows.insert(i,rows[i])
            rrows[i].reverse()
        row = "".join(str(x) for x in diag1)
        winner = check_winner(row)

        if winner == "":
            diag2 = ""
            for i in range(4):
                diag2 = diag2 + rrows[i][i]
            row = "".join(str(x) for x in diag2)
            winner = check_winner(row)

    if winner == "":
        if draw:
            winner = "Draw"
        else:
            winner = "Game has not completed"
        
    print ("Case #" + str(tc)+": "+winner)
           
           
if __name__ == '__main__' :
    # number of test cases
    T = input()
    tc = 1
    while tc <= T:
        test(tc)
        tc = tc + 1
        raw_input()

    
