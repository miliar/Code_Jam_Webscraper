
import copy

class Log():
    def __init__(self, debug=False):
        self.debug = debug

    def info(self, fmt, *args):
        if self.debug:
            print fmt % args

log = Log()

def check_raw(mat):
    win = ''
    complete = True
    for r in range(4):
        for c in range(4):
            cr = mat[r][c]
            if cr == '.':
                complete = False
                win = ''
                break
            if win == '':
                if cr <> 'T':
                    win = cr
            elif win <> cr:
                if cr == "T":
                    continue
                else:
                    win = ''
                    break
        if win <> '':
            break
    return win, complete

def check_col(mat):
    win = ''
    complete = True

    for r in range(4):
        for c in range(4):        
            cr = mat[c][r]
            if cr == '.':
                complete = False
                win = ''
                break
            if win == '':
                if cr <> 'T':
                    win = cr
            elif win <> cr:
                if cr == "T":
                    continue
                else:
                    win = ''
                    break
        if win <> '':
            break
    return win, complete

def check_dia1(mat):
    win = ''
    complete = True
    for r in range(4):
        cr = mat[r][r]
        if cr == '.':
            complete = False
            win = ''
            break
        if win == '':
            if cr <> 'T':
                win = cr
        elif win <> cr:
            if cr == "T":
                continue
            else:
                win = ''
                break

    return win,complete

def check_dia2(mat):
    win = ''
    complete = True
    row = 0
    col = 3

    for r in range(4):
        cr = mat[row][col]
        if cr == '.':
            complete = False
            win = ''
            break
        if win == '':
            if cr <> 'T':
                win = cr
        elif win <> cr:
            if cr == "T":
                continue
            else:
                win = ''
                break
        row += 1
        col -= 1
    return win,complete
    
    
def solve():
    raw = 4
    mat = []
    for r in range(4):
        mat.append(raw_input())
    
    win = ''
    complete = True
    for i in range(4):
        if i == 0:
            win,complete = check_raw(mat)
            log.info("raw %s %d" ,win,complete)
        elif i == 1 and win == '':
            win,complete = check_col(mat)
            log.info("col %s %d" ,win,complete)
        elif i == 2 and win == '':
            win,complete = check_dia1(mat)
            log.info("dia1 %s %d" ,win,complete)
        elif i == 3 and win == '':        
            win,complete = check_dia2(mat)
            log.info("dia2 %s %d" ,win,complete)
        if win <> '':
            break
            
    ans = ''
    if win <> '':
        ans = "%s won"%win
    elif complete:
        ans = "Draw"
    else:
        ans = "Game has not completed"
    return ans

if __name__ == '__main__':
    
    case = int(raw_input())
    for i in range(1, case+1):
        ans = solve()
        print "Case #%d: %s"%(i, ans)
        if case <> i:
            temp = raw_input()