import sys

def isWin(board, mark):
    idx = [ [0,4,8,12],
            [1,5,9,13],
            [2,6,10,14],
            [3,7,11,15],
            [0,1,2,3],
            [4,5,6,7],
            [8,9,10,11],
            [12,13,14,15],
            [0,5,10,15],
            [3,6,9,12]]

    for b in idx:
        if board[b[0]] == mark and board[b[1]] == mark and \
           board[b[2]] == mark and board[b[3]] == mark:
            return True
    
    return False

def checkValue(xteam, oteam, has_empty_cell):
    if (isWin(xteam, 'X') == True):
        return "X won"
    if (isWin(oteam, 'O') == True):
        return "O won"

    if (has_empty_cell == True):
        return "Game has not completed"

    return "Draw"

if __name__ == '__main__':
    lines = int(raw_input())
    for i in xrange(lines):
        xteam = []
        oteam = []
        count_empty_cell = 0

        for c in xrange(4):
            buf = raw_input()
            for t in xrange(4):
                if buf[t] is 'T':
                    xteam.append('X')
                    oteam.append('O')
                else:
                    xteam.append(buf[t])
                    oteam.append(buf[t])

                if buf[t] is '.':
                    count_empty_cell = count_empty_cell + 1
                
        has_empty_cell = False
        if count_empty_cell > 0:
            has_empty_cell = True

        print "Case #%s: %s"%(i+1, checkValue(xteam,oteam, has_empty_cell))
        buf = raw_input()
