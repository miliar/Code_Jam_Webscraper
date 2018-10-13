# Problem 1 Tic-Tac-Toe-Tomek
import sys

f = open(sys.argv[1])

numgames = int(f.readline().strip())

for g in range(numgames):

    gamenum = g + 1

    X_won = False
    O_won = False
    has_empty = False
    game_over = False
    
    r = []
    r.append(f.readline().strip())
    r.append(f.readline().strip())
    r.append(f.readline().strip())
    r.append(f.readline().strip())
    bl = f.readline()

    cases = []
    
    # rows
    cases.extend(r)

    # column
    for i in [0,1,2,3]:
        cases.append("".join([row[i] for row in r]))

    diag1 = []
    diag2 = []
    # diagonals
    for i in [0,1,2,3]:
        diag1.append(r[i][i])
        diag2.append(r[i][3-i])
        
    cases.append("".join(diag1))
    cases.append("".join(diag2))
        
    for case in cases:
        seen_X = False
        seen_O = False
        seen_empty = False
        
        for sq in case:
            if sq == ".":
                # No winner possible using this case
                seen_empty = True
                has_empty = True
                break

            if sq == "X":
                seen_X = True        
            elif sq == "O":
                seen_O = True

        if not seen_empty:
            if seen_O:
                if not seen_X:
                    O_won = True
                    game_over = True

            if seen_X:
                if not seen_O:
                    X_won = True
                    game_over = True

        if game_over:
            break

    if X_won:
        print "Case #%s: %s won" % (gamenum, "X")
    elif O_won:
        print "Case #%s: %s won" % (gamenum, "O")

    else:
        if has_empty:
            print "Case #%s: Game has not completed" % (gamenum)
        else:
            print "Case #%s: Draw" % (gamenum)

         



