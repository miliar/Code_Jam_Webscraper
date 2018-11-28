import sys
filename = sys.argv[0] 

result = ''
_in = open(filename.replace('.py', '.in'), 'r')
count = _in.readline()

def change(char):
    if char == 'X':
        return -1 
    elif char == 'O':
        return 1 
    elif char == 'T':
        return 0 
    elif char == '.':
        return 1000 

def check(l):
    if 3 in l or 4 in l:
        return 'O won'
    elif -3 in l or -4 in l:
        return  'X won'
    elif len([n for n in l if n > 100]) == 10 or 998 in l or 1002 in l or 1999 in l or 2001 in l:
        return 'Game has not completed'
    
    else:
        return 'Draw'
         

def isWin(data):
    result = [0] * 10
    matrix = [list(d) for d in data.split('\n')]
   
    for idx_row, row in enumerate(matrix):
        for idx_col, col in enumerate(row):
            result[idx_row] += change(col)
            result[4+idx_col] += change(col)
        result[8] += change(matrix[idx_row][idx_row])
        result[9] += change(matrix[idx_row][3-idx_row])
    print result    
    return check(result)

for idx, data in enumerate(_in.read().split('\n\n')):
    if idx < 10:
        result += 'Case #%s: %s\n' % (idx+1, isWin(data))

_out = open(filename.replace('.py', '.out'), 'w')
_out.write(result)
_out.close()

