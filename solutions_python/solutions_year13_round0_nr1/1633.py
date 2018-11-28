import itertools

fin = open("A-small-attempt0.in", "r")
fout = open("A-small.out", "w")

def all_same_not_empty( items ):
    return all(x == items[0] != '.' for x in items)    

def checkT(i,j,board):
#checkin if it works with T
    ranI = range(4) 
    ranJ = range(4)
    ranI.remove(i)
    ranJ.remove(j)
    
    lst = []
    if i == j:
        for ri in ranI:
            lst.append(board[ri][ri])
        if all_same_not_empty(lst):
            print board[ri][ri], "won"
            fout.write("%c won\n" %(board[ri][ri]))    
            return True
        
    lst = []
    diag = [(3,0),(2,1),(1,2),(0,3)]
    if (i,j) in diag:
        diag.remove((i,j))
        for (ii,jj) in diag:
            lst.append(board[ii][jj])    
        if all_same_not_empty(lst):
            print board[ii][jj], "won"        
            fout.write("%c won\n" %(board[ii][jj]))
            return True
    
    lst = []
    for ri in ranI:
        lst.append(board[ri][j])
    if all_same_not_empty(lst):
        print board[ri][j], "won"
        fout.write("%c won\n" %(board[ri][j]))
        return True
 
    lst = []
    for rj in ranJ:
        lst.append(board[i][rj])
    if all_same_not_empty(lst):
        print board[i][rj], "won"
        fout.write("%c won\n" %(board[i][rj]))
        return True
    return False


        
        

def check_result(board):
    for i in range(0,4):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] != "." :
            print board[i][0], "won\n"
            fout.write("%c won\n" %(board[i][0]))
            return
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] != ".":
            print board[0][i], "won\n"
            fout.write("%c won\n" %(board[0][i]))
            return            
            
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] != "." :
        print board[0][0], "won\n"
        fout.write("%c won\n" %(board[0][0]))
        return
    if board[0][2] == board[1][1] == board[2][0] == board[3][3] != ".":
            print board[0][2], "won\n"
            fout.write("%c won\n" %(board[0][2]))
            return

    i=0
    Tfound = False
    for level in board:
        if 'T' in level:
            j = level.index('T')
            Tfound = True
            break
        i = i+1

    if Tfound:
        if checkT(i,j,board):
            return

    if "." not in board[0] and "." not in board[1] and "." not in board[2]:
        print "Draw \n"
        fout.write("Draw\n")
        return
    else:
        print "Game has not completed \n"
        fout.write("Game has not completed\n")



def main():
    
    N = int(fin.readline())
    for n in xrange(1,N+1):
        fout.write("Case #%i: " %(n))
        
        board = []
        for i in range(5):
            line = fin.readline()
            if line is None or line == '\n':
                continue
            line = line.rstrip('\n')
            board.append(list(line))
        print board    

        check_result(board)    

    fout.close()

if __name__ == '__main__':
    main()
