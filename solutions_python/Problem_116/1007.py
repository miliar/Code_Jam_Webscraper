import sys
def tictac (i):
    row =[]
    for y in range (0,4):
        row.append(raw_input())
    crap = sys.stdin.readline()
    # comparing rows
    for y in row:
        if y in ["XXXX","XXXT","XXTX","XTXX","TXXX"]:
            print "Case #" + str(i+1) + ": X won"
            return
        elif y in ["OOOO","OOOT","OOTO","OTOO","TOOO"]:
            print "Case #" + str(i+1) + ": O won"
            return
    # comparing columns
    for y in range (0,4):
        if row[0][y] in ["X","T"] and row[1][y] in ["X","T"] and row[2][y] in ["X","T"] and row[3][y] in ["X","T"]:
            print "Case #" + str(i+1) + ": X won"
            return
        elif row[0][y] in ["O","T"] and row[1][y] in ["O","T"] and row[2][y] in ["O","T"] and row[3][y] in ["O","T"]:
            print "Case #" + str(i+1) + ": O won"
            return
    # comparing diagonal from upper left to lower right
    if row[0][0] in ["X","T"] and row[1][1] in ["X","T"] and row[2][2] in ["X","T"] and row[3][3] in ["X","T"]:
        print "Case #" + str(i+1) + ": X won"
        return
    elif row[0][0] in ["O","T"] and row[1][1] in ["O","T"] and row[2][2] in ["O","T"] and row[3][3] in ["O","T"]:
        print "Case #" + str(i+1) + ": O won"
        return
    # comparing diagonal from lower left to upper right
    elif row[3][0] in ["X","T"] and row[2][1] in ["X","T"] and row[1][2] in ["X","T"] and row[0][3] in ["X","T"]:
        print "Case #" + str(i+1) + ": X won"
        return
    elif row[3][0] in ["O","T"] and row[2][1] in ["O","T"] and row[1][2] in ["O","T"] and row[0][3] in ["O","T"]:
        print "Case #" + str(i+1) + ": O won"
        return
    for j in range (0,4):
        for k in range (0,4):
            if row[j][k] in ["."]:
                print "Case #" + str(i+1) + ": Game has not completed"
                return
    print "Case #" + str(i+1) + ": Draw"
    return
    
t_cases = raw_input()
t_cases = int(t_cases)
for x in range (0,t_cases):
    tictac(x)
