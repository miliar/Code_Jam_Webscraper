import sys
sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')
out = sys.stdout
N = input()
for i in range(1, N+1):
    out.write('Case #')
    out.write(str(i))
    out.write(': ')
    won = False
    board = []
    for j in range(0,4):
        board.append(raw_input())

    for k in range(0,2):
        for p in ['X', 'O']:        
            b = [x.replace('T', p) for x in board]        
            for j in range(0,4):            
                if b[j] == p*4:
                    won = p
                    break
            if won: break
        if won: break
        board = zip(*board)
        board = [''.join(x) for x in board]

    for p in ['X', 'O']:
        b = [x.replace('T', p) for x in board]
        if ''.join([b[0][0], b[1][1], b[2][2], b[3][3]]) == p*4 or \
                ''.join([b[0][3], b[1][2], b[2][1], b[3][0]]) == p*4:
            won = p
            break

    if not won:
        board = ''.join(board)
        if '.' in board:
            print 'Game has not completed'
        else:
            print 'Draw'
    else:
        print won, 'won'
    sys.stdin.readline()
sys.stdin.close()
sys.stdout.close()
