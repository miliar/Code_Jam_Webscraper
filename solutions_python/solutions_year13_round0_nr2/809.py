def readboard(f):
    mn = f.readline().split(" ")
    m = int(mn[0])
    data = []
    while m>0:
        m-=1
        data+= [[int (i) for i in f.readline().split(" ")]]
    return data
def checkboard(board):
    m = len(board)
    n = len(board[0])
    result = []
    for i in range(m):
        result +=[[]]    
        for j in range(n):
            result[i]+=[0]
    rowMax = [max(i) for i in board]        
    column = [[i[j] for i in board] for j in range(n)]       
    columnMax = [max(i) for i in column]        
    for i in range(m):
        for j in range(n):
            if board[i][j] != rowMax[i]:
                if board[i][j] != columnMax[j]:
                    return "NO"
    return "YES"
def main():
    f = open("input.txt")
    counter = int(f.readline())
    result = "Draw"
    case = 1
    while case<= counter:
        board = readboard(f)
        print "Case #%s: %s"%(case,checkboard(board))
        case +=1
        
main()

