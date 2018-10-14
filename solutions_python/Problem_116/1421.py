def complete():
    for i in xrange(4):
        for j in xrange(4):
            if board[i][j]=='.':
                return 0
    return 1

def win(player):
    for i in xrange(4):
        count=0
        for j in xrange(4):
            if board[i][j]==player or board[i][j]=='T':
                count+=1
        if count==4:
            return 1
    for j in xrange(4):
        count=0
        for i in xrange(4):
            if board[i][j]==player or board[i][j]=='T':
                count+=1
        if count==4:
            return 1
    count=0
    for i,j in [0,0],[1,1],[2,2],[3,3]:
        if board[i][j]==player or board[i][j]=='T':
            count+=1
    if count==4:
        return 1
    count=0
    for i,j in [3,0],[2,1],[1,2],[0,3]:
        if board[i][j]==player or board[i][j]=='T':
            count+=1
    if count==4:
        return 1
    return 0

global n,board
infile=open("A-large.in",'r')
outfile=open("out",'w')
lines=infile.readlines()
infile.close()
n=int(lines[0][:-1])
for i in xrange(n):
    board=[]
    for j in xrange(4):
        board.append(lines[5*i+1+j][:-1])
    if win('X'):
        outfile.write("Case #"+str(i+1)+": X won\n")
    elif win('O'):
        outfile.write("Case #"+str(i+1)+": O won\n")
    elif complete():        
        outfile.write("Case #"+str(i+1)+": Draw\n")
    else:
        outfile.write("Case #"+str(i+1)+": Game has not completed\n")
outfile.close()
