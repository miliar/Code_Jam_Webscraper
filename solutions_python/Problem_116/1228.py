import sys

invalid_line = {'X', 'O'}

def judge_line(line):
    if '.' not in line and len(line) <= 2 and invalid_line != line:
        return list(line - {'T'})[0]
    else:
        return False

if __name__ == '__main__':
    num_tests = int(next(sys.stdin))
    
    for i in xrange(num_tests):
        incomplete = False
        
        rows = [next(sys.stdin).rstrip() for j in xrange(4)]
        columns = [[row[y] for row in rows] for y in xrange(4)]
        diagonals = [[rows[0][0], rows[1][1], rows[2][2], rows[3][3]],
                     [rows[0][3], rows[1][2], rows[2][1], rows[3][0]]]
        
        for line in rows + columns + diagonals:
            if '.' in line:
                incomplete = True
            
            result = judge_line(set(line))
            
            if result:
                break
        
        if result:
            message = result + ' won'
        elif incomplete:
            message = 'Game has not completed'
        else:
            message = 'Draw'
        
        print 'Case #{0}: {1}'.format(i + 1, message)
        
        next(sys.stdin)