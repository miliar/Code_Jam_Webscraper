n=int(raw_input())
try:
    for i in range(1,n+1):
        board=[raw_input() for _ in range(4)]
        rows = board + map(''.join,zip(*board)) + [board[0][0]+board[1][1]+board[2][2]+board[3][3],
                                       board[0][3]+board[1][2]+board[2][1]+board[3][0]]
        if  any(e in rows for e in ['XXXX','XXXT','XXTX','XTXX','TXXX']):
            print "Case #{}: X won".format(i)
        elif  any(e in rows for e in ['OOOO','OOOT','OOTO','OTOO','TOOO']):
            print "Case #{}: O won".format(i)
        elif any('.' in e for e in board):
            print "Case #{}: Game has not completed".format(i)
        else:
            print "Case #{}: Draw".format(i)
        raw_input()
except EOFError:
    pass
