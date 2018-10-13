import fileinput,sys

print_indicator = 0
    

lines = []

for line in fileinput.input():
    lines.append(line)

n= int(lines[0])

def column(board,col):
    result = []
    for i in xrange(0,4):
        result.append(board[i][col])
    return result

def ldiag(board):
    result = []
    myprint("board,ldiag", board)
    for i in xrange(0,4):
        result.append(board[i][i])
    return result
                   
def rdiag(board):
    result = []
    for i in xrange(0,4):
        result.append(board[3-i][i])
    return result

def win(foursome):
    myprint(foursome)
    (xcount,ycount,tcount) = (0,0,0)
    for i in xrange(0,4):
        if foursome[i] == 'X':
            xcount+=1
        elif foursome[i] == 'O':
            ycount+=1
        elif foursome[i] == 'T':
            tcount+=1
    myprint("counts", xcount,ycount,tcount)
    if xcount + tcount == 4:
        return "X won"
    elif ycount + tcount == 4:
        return "O won"
    else:
        return False

def myprint(*arg):
    if print_indicator != 0:
        print print_indicator
        print arg

case = 0
line_no =1      
for j in xrange(1,n+1):
    board = []
    case +=1
    print "Case #%d:" % (case),
    for j in xrange(0,4):
        board.append(lines[line_no])
        line_no+=1
    line_no+=1
    #myprint("board", board)
    val = False
    for i in xrange(0,4):
        val = win(column(board,i))
        myprint(val)
        if val:
            print val
            break
        val = win(board[i])
        myprint(val)
        if val:
            print val
            break
        val = win(ldiag(board))
        myprint(val)
        if val:
            print val
            break
        val = win(rdiag(board))
        if val:
            print val
            break
    if not val:
        for i in xrange(0,4):
            if ("." in board[i]):
                val = "Game has not completed"
                print val
                break
        if not val:
            print "Draw"
            
                

