import sys

def solve(b,m,n):
    for i in range(m):
        for j in range(n):
            if(b[i][j]=='#'):
                if j==n-1:
                    return False
                if i==m-1:
                    return False
                if (b[i][j+1]!='#' or b[i+1][j]!='#' or b[i+1][j+1]!='#'):
                    return False
                b[i][j]='/'
                b[i][j+1]='\\'
                b[i+1][j]='\\'
                b[i+1][j+1]='/'
    return True


f = sys.stdin
t = int(f.readline())
for i in range(t):
    s = f.readline().split()
    r = int(s[0])
    c = int(s[1])
    board =[]
    for j in range(r):
        s = f.readline()
        l = []
        for x in range(c):
            l.append(s[x])
        board.append(l)
    print "Case #%d:" % (i+1)
    if solve(board,r,c):
        for j in range(r):
            for i in range(c):
                sys.stdout.write(board[j][i])
            print ""
    else:
        print "Impossible"