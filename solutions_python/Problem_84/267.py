#! /usr/bin/python

def solve(n,m,total,board):
    answer = ''
    left = total
    for i in range(0,n):
        for j in range(0,m):
            if i+1<n and j+1<m:
                if board[i][j]=='#' and board[i+1][j]=='#' and board[i][j+1]=='#' and board[i+1][j+1]=='#':
                    left = left - 4
                    board[i][j] = '/'
                    board[i+1][j] = '\\'
                    board[i][j+1] = '\\'
                    board[i+1][j+1] = '/'
    if left==0:
        for i in range(0,n):
            for j in range(0,m):
                answer = answer + board[i][j]
            answer = answer + '\n'
    else:
        answer = 'Impossible\n'
    return answer

if __name__ == "__main__":
    f = open("data.in","r")
    g = open("data.out","w")
    cases = int(f.readline().split()[0])
    for case in range(1,cases+1):
        line = f.readline().split()
        n = int(line[0])
        m = int(line[1])
        board = []
        total = 0
        for i in range(0,n):
            board.append([])
            line = f.readline()
            for j in range(0,m):
                board[i].append(line[j])
                if line[j]=='#':
                    total = total + 1
        #print total
        #print games
        #print games_won
        answer = solve(n,m,total,board)
        g.write("Case #%d:\n%s" % (case,answer))
    f.close()
    g.close()