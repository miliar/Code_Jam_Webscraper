'''

check if someone wins

if no one wins
    game not complete, or draw
elif O wins
    print O wins
elif X wins
    print X wins

'''
####################################################################

T = int(raw_input())

def win(s,c): # s = 4-character string, c = either X or O
    if (s.count(c) == 4) or ((s.count(c) == 3) and ('T' in s)):
        return True
    else:
        return False

for i in range(T):

    # get matrix
    M = []
    empty = False # if there are empty cells
    for j in range(4):
        M.append(raw_input())
        if '.' in M[j]:
            empty = True
    raw_input()

    # check if someone wins
    Xwins = False
    Owins = False

#    print M

    #### 1. the two diagonals
    diagonal = []
    diagonal.append(M[0][0] + M[1][1] + M[2][2] + M[3][3])
    diagonal.append(M[0][3] + M[1][2] + M[2][1] + M[3][0])
#    print diagonal
    for k in range(2):
        if '.' not in diagonal[k]:
            Xwins = win(diagonal[k], 'X')
            Owins = win(diagonal[k], 'O')
            if Xwins or Owins:
                break

    #### 2. the 4 verticals and 4 horizontals
    if not (Xwins or Owins):
        S = []
        for j in range(4): # horizontals
            S.append(M[j][0] + M[j][1] + M[j][2] + M[j][3])
        for j in range(4): # verticals
            S.append(M[0][j] + M[1][j] + M[2][j] + M[3][j])
        for k in range(8):
            if '.' not in S[k]:
                Xwins = win(S[k], 'X')
                Owins = win(S[k], 'O')
                if Xwins or Owins:
                    break


    if not (Xwins or Owins): # if no one wins
        if empty:
            print 'Case #%d: Game has not completed' % (i+1)
        else:
            print 'Case #%d: Draw' % (i+1)
    elif Xwins:
        print 'Case #%d: X won' % (i+1)
    elif Owins:
        print 'Case #%d: O won' % (i+1)


'''

check if someone wins

if no one wins
    game not complete, or draw
elif O wins
    print O wins
elif X wins
    print X wins

'''




