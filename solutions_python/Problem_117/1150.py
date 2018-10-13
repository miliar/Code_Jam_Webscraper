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
    nbym = (lines[line_no]).partition(" ")
    N = int(nbym[0])
    M = int(nbym[2])
    for j in xrange(0,N):    
        line_no+=1
        current_line = lines[line_no]
        myprint("current_line", current_line)
        row = []
        for k in xrange(0,M):
            cl_split = current_line.partition(" ")
            row.append(int(cl_split[0]))
            current_line = cl_split[2]
        board.append(row)
    myprint("board", board)
    line_no+=1
    max_row_vals = [];
    max_col_vals = []
    for j in xrange(0,N):
        max_row_vals.append(0)
        for k in xrange(0,M):
            if board[j][k] > max_row_vals[j]:
                max_row_vals[j] = board[j][k]

    for k in xrange(0,M):
        max_col_vals.append(0)
        for j in xrange(0,N):
            if board[j][k] > max_col_vals[k]:
                max_col_vals[k] = board[j][k]

    cool = True
    myprint("maxcols", max_col_vals)
    myprint("maxrows", max_row_vals)
    for k in xrange(0,M):
        for j in xrange(0,N):
            if ((not board[j][k] == max_row_vals[j]) and (not board[j][k] == max_col_vals[k])):
                cool = False
                break
        if not cool:
            break
    if cool:
        print "YES"
    else:
        print "NO"
            
    
            
            
                

