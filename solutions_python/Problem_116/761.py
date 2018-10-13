import sys,os

class OutFile(file):
    def __init__(self,file_name):
        file.__init__(self,file_name,'w')
    def write(self,x):
        sys.stdout.write(x)
        file.write(self,x)
    def writelines(self,x):
        print x
        assert False
    def __enter__(self,*argv):
        return self
    def __exit__(self,*argv):
        self.close()

def lineHcheck(board,th,play):
    for i in xrange(4):
        if not board[th][i] in ['T',play]:
            return False
    return True

def lineVcheck(board,th,play):
    for i in xrange(4):
        if not board[i][th] in ['T',play]:
            return False
    return True

def check_reminder(board):
    return '.' in ''.join(board)

def DiagCheck(board,play):
    check1,check2 = True,True
    for i in xrange(4):
        if not board[i][i] in ['T',play]:
            check1 = False
            break
    for i in xrange(4):
        if not board[i][3-i] in ['T',play]:
            check2 = False
            break
    return check1 or check2

def check_winner(board,play):
    for i in xrange(4):
        if lineVcheck(board,i,play) or lineHcheck(board,i,play):
            return True
    if DiagCheck(board,play):
        return True
    return False

def calculate(f_in,f_out):
    board = []
    for i in xrange(4):
        board.append(f_in.readline().strip())
    f_in.readline()
    if check_winner(board,'O'):
        print >>f_out,'O won'
    elif check_winner(board,'X'):
        print >>f_out,'X won'
    elif check_reminder(board):
        print >>f_out,'Game has not completed'
    else:
        print >>f_out,'Draw'

def do(file_name):
    name,ext = os.path.splitext(file_name)
    file_out = name+'.out'
    with open(file_name) as f1:
        with OutFile(file_out) as f2:
            case = int(f1.readline())
            for i in xrange(case):
                print >>f2,'Case #%d:'%(i+1),
                calculate(f1,f2)

if __name__ == '__main__':
    do(sys.argv[1])
