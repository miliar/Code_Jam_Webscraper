f = open('2.ex', 'r')
fo = open('2.out' ,'w')

cases = int(f.readline())

for c in xrange(cases):
    
    m, n = [int(x) for x in f.readline().split()]
    
    lawn = []
    for row in xrange(m):
        lawn.append(f.readline().split())
    
    ok = True
    for row in xrange(m):
        for column in xrange(n):
            height = lawn[row][column]
            max_row_height = max(lawn[row])
            row_ok = max_row_height <= height
            max_column_height = max([row2[column] for row2 in lawn])
            col_ok = max_column_height <= height
            if not row_ok and not col_ok:
                ok = False
                break
        if not ok:
            break
            
    
    output = 'YES' if ok else 'NO'
    
    fo.write('Case #' + str(c+1) + ': ' + str(output) + '\n')