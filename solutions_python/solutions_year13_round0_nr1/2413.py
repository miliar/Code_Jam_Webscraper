import sys

finput = sys.stdin

def getboard(n):
    return [list(finput.readline()) for row in xrange(n)]

def countch(lst,sub):
    return sum([1 if x in sub else 0 for x in lst])

def check(lst,n):
    # there is only ever one T so the all 'T's case is ignored
    X = countch(lst,"XT")
    O = countch(lst,"OT")
    if X == n : return 'X' 
    if O == n : return 'O' 
    if '.' in lst : return '.'
    else      : return 'T'



def main():
    for test in xrange(int(finput.readline())):
        board = getboard(4)
        rows = map(lambda x: check(x,4) , board)
        cols = map(lambda x: check(x,4) , zip(*board))
        
        digs = map(lambda x: check(x,4),
                   [[l[i] for i,l in enumerate(board)]
                    ]+
                   [[l[i] for i,l in enumerate(board[::-1])]])
        
        vals = rows+cols+digs
        
        print "Case #{0:1d}:".format(test+1),
        
        if   'X' in vals: print "X won"
        elif 'O' in vals: print "O won"
        elif '.' in vals: print "Game has not completed"
        else            : print "Draw"
        finput.readline()
        
        
        

if __name__ == "__main__":
    main()
