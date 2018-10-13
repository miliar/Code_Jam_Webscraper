def main():
    n = int(raw_input())
    for i in range(n):
        board = []
        boardFull = True
        #check rows
        line = raw_input()
        if line.count('X') == 4 or ((line.count('X') == 3) and 'T' in line):
            print "Case #%s: X won" %(i+1)
            while line:
                line = raw_input()
            continue
        if line.count('O') == 4 or ((line.count('O') == 3) and 'T' in line):
            print "Case #%s: O won" %(i+1)
            while line:
                line = raw_input()
            continue
        boardFull =boardFull and '.' not in line
        board.append(line)

        line = raw_input()
        if line.count('X') == 4 or ((line.count('X') == 3) and 'T' in line):
            print "Case #%s: X won" %(i+1)
            while line:
                line = raw_input()
            continue
        if line.count('O') == 4 or ((line.count('O') == 3) and 'T' in line):
            print "Case #%s: O won" %(i+1)
            while line:
                line = raw_input()
            continue
        boardFull =boardFull and '.' not in line
        board.append(line)

        line = raw_input()
        if line.count('X') == 4 or ((line.count('X') == 3) and 'T' in line):
            print "Case #%s: X won" %(i+1)
            while line:
                line = raw_input()
            continue
        if line.count('O') == 4 or ((line.count('O') == 3) and 'T' in line):
            print "Case #%s: O won" %(i+1)
            while line:
                line = raw_input()
            continue
        boardFull =boardFull and '.' not in line
        board.append(line)

        line = raw_input()
        if line.count('X') == 4 or ((line.count('X') == 3) and 'T' in line):
            print "Case #%s: X won" %(i+1)
            while line:
                line = raw_input()
            continue
        if line.count('O') == 4 or ((line.count('O') == 3) and 'T' in line):
            print "Case #%s: O won" %(i+1)
            while line:
                line = raw_input()
            continue
        boardFull =boardFull and '.' not in line
        board.append(line)
        #print board
        #check columns
        winningCol=False
        for j in range(len(board)):
            col = board[0][j]+board[1][j]+board[2][j]+board[3][j]
            if (col.count('X') == 4) or ((col.count('X') == 3) and 'T' in col):
                print "Case #%s: X won" %(i+1)
                winningCol = True
                break
            if (col.count('O') == 4) or ((col.count('O') == 3) and 'T' in col):
                print "Case #%s: O won" %(i+1)
                winningCol = True
                break
        if winningCol:
            raw_input()
            continue

        #check diagonals
        line = board[0][0]+board[1][1] + board[2][2] + board[3][3]
        if line.count('X') == 4 or ((line.count('X') == 3) and 'T' in line):
            print "Case #%s: X won" %(i+1)
            raw_input()
            continue
        if line.count('O') == 4 or ((line.count('O') == 3) and 'T' in line):
            print "Case #%s: O won" %(i+1)
            raw_input()
            continue
        line = board[3][0]+board[2][1] + board[1][2] + board[0][3]
        if line.count('X') == 4 or ((line.count('X') == 3) and 'T' in line):
            print "Case #%s: X won" %(i+1)
            raw_input()
            continue
        if line.count('O') == 4 or ((line.count('O') == 3) and 'T' in line):
            print "Case #%s: O won" %(i+1)
            raw_input()
            continue

        #draw or incomplete
        if boardFull:
            print "Case #%s: Draw" %(i+1)
        else:
            print "Case #%s: Game has not completed" %(i+1)
        raw_input()
        
if __name__=="__main__": main()
