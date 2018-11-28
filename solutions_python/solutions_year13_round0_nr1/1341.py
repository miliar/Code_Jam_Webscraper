def readline_ints():
    return [int(num) for num in fin.readline().strip().split()]
def readline():
    return [num for num in fin.readline().strip().split()]
def wins(p,board):
    for i in range(4):
        if (board[i]==p or board[i]=="T") and (board[i+4]==p or board[i+4]=="T") and (board[i+8]==p or board[i+8]=="T") and (board[i+12]==p or board[i+12]=="T"):
            return True
        if (board[4*i]==p or board[4*i]=="T") and (board[4*i+1]==p or board[4*i+1]=="T") and (board[4*i+2]==p or board[4*i+2]=="T") and (board[4*i+3]==p or board[4*i+3]=="T"):
            return True
    if (board[0]==p or board[0]=="T") and (board[5]==p or board[5]=="T") and (board[10]==p or board[10]=="T") and (board[15]==p or board[15]=="T"):
        return True
    if (board[3]==p or board[3]=="T") and (board[6]==p or board[6]=="T") and (board[9]==p or board[9]=="T") and (board[12]==p or board[12]=="T"):
        return True
    else: return False
    
# <codecell>

# Update this with the filename
fname = "A-large"
with open(fname+".in","r") as fin, open(fname+".out","w") as fout:

    numcases = readline_ints()[0]
    
    print(numcases, "cases")
    for caseno in range(1, numcases+1):
        # Code goes here
        line=[]   
        line.append(readline())
        line.append(readline())
        line.append(readline())
        line.append(readline())
        line.append(readline())
        del line[-1]
        board=[]
        for row in range(4):
            for col in range(4):
                board.append(line[row][0][col])
        if wins("X",board):
            result="X won"
        elif wins("O",board):
            result="O won"
        elif "." in board:
            result="Game has not completed"
        else:
            result="Draw"
        outstr = "Case #%d: %s" % (caseno, result)
        fout.write(outstr + "\n")
        print(outstr)
