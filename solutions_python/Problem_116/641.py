#benoni.boy
#Google Code Jam
#13 April 2013
import sys

sys.stdin = open('C:\GCJ\in.txt')
sys.stdout = open('C:\GCJ\out.txt', 'w')

xline = 'XXXX'
oline = 'OOOO'

def doCase(n):
    lines = [input() for i in range(4)]
    incomplete = False
    for l in lines:
        if '.' in l: incomplete = True
        if l.replace('T', 'X') == xline:
            print('Case #' + str(n + 1) + ': X won')
            return
        if l.replace('T', 'O') == oline:
            print('Case #' + str(n + 1) + ': O won')
            return
    columns = [''.join([lines[j][i] for j in range(4)]) for i in range(4)]
    for l in columns:
        if l.replace('T', 'X') == xline:
            print('Case #' + str(n + 1) + ': X won')
            return
        if l.replace('T', 'O') == oline:
            print('Case #' + str(n + 1) + ': O won')
            return
    diag = ''.join([lines[i][i] for i in range(4)])
    if diag.replace('T', 'X') == xline:
        print('Case #' + str(n + 1) + ': X won')
        return
    if diag.replace('T', 'O') == oline:
        print('Case #' + str(n + 1) + ': O won')
        return
    diag = ''.join([lines[i][-i] for i in range(4)])
    if diag.replace('T', 'X') == xline:
        print('Case #' + str(n + 1) + ': X won')
        return
    if diag.replace('T', 'O') == oline:
        print('Case #' + str(n + 1) + ': O won')
        return
    if incomplete:
        print('Case #' + str(n + 1) + ': Game has not completed')
    else: print('Case #' + str(n + 1) + ': Draw')

T = input()
for i in range(eval(T)):
    doCase(i)
    input()

sys.stdin.close()
sys.stdout.close()
