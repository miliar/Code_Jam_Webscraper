import sys                       
import os

def main():
    s = ''.join(sys.stdin.readlines()).split()
    os.close(0)

    T = int(s[0])
    s = s[1:]

    for i in range(T):
        N = int(s[0])
        K = int(s[1])
        s = s[2:]
        board = []
        for j in range(N):
            board += [[]]
            for k in s[0]:
                board[j] += [s[0][0]]
                s[0] = s[0][1:]
            s = s[1:]
        board = gravity(board)
        win = checkwin(board,K)
        if len(win) == 0:
            print "Case #" + str(i+1) + ": Neither"
        if len(win) == 2:
            print "Case #" + str(i+1) + ": Both"
        if win == "R":
            print "Case #" + str(i+1) + ": Red"
        if win == "B":
            print "Case #" + str(i+1) + ": Blue"


def gravity(board):
    for i in board:
        for j in range(len(i)-2,-1,-1):
            if i[j] in 'RB':
                k = j+1
                while k < len(i) and i[k] == '.':
                    i[k] = i[k-1]
                    i[k-1] = '.'
                    k += 1
    return board

def checkwin(board,K):
    won = ""
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in 'RB' and board[i][j] not in won:
                win = checkHor(board,i,j,K) or checkVert(board,i,j,K) or checkDDiag(board,i,j,K) or checkUDiag(board,i,j,K)
                if win:
                    if board[i][j] not in won:
                        won += board[i][j]

    return won

def checkDDiag(board,i,j,K):
    count = 0
    k = i
    l = j
    sym = board[i][j]
    while k >= 0 and l >= 0 and board[k][l] == sym:
        count += 1
        k -=1
        l -=1

    if i < len(board)-1 and j < len(board)-1 and board[i+1][j+1] == sym:
        k = i+1
        l = j+1
        while k < len(board) and l < len(board) and board[k][l] == sym:
            count += 1
            k += 1
            l += 1

    return count >= K

def checkUDiag(board,i,j,K):
    count = 0
    k = i
    l = j
    sym = board[i][j]
    while k >= 0 and l <= len(board)-1 and board[k][l] == sym:
        count += 1
        k -=1
        l +=1

    if i < len(board)-1 and l >= 0 and board[i+1][j-1] == sym:
        k = i+1
        l = j-1
        while k < len(board) and l >= 0 and board[k][l] == sym:
            count += 1
            k += 1
            l -= 1

    return count >= K

def checkHor(board,i,j,K):
    count = 0
    k = i
    sym = board[i][j]
    while k >= 0 and board[k][j] == sym:
        count += 1
        k -=1

    if i < len(board)-1 and board[i+1][j] == sym:
        k = i+1
        while k < len(board) and board[k][j] == sym:
            count += 1
            k += 1

    return count >= K

def checkVert(board,i,j,K):
    count = 0
    k = j
    sym = board[i][j]
    while k >= 0 and board[i][k] == sym:
        count += 1
        k -=1

    if j < len(board)-1 and board[i][j+1] == sym:
        k = j+1
        while k < len(board) and board[i][k] == sym:
            count += 1
            k += 1

    return count >= K

if __name__ == "__main__":
 	main()

