



if __name__ == '__main__':
    testcases = int(raw_input())
    for tc in xrange(testcases):
        r, c = (int(x) for x in raw_input().split())
        rows = [list(raw_input()) for _ in xrange(r)]
        positions = {(i, j) : rows[i][j] for i in xrange(r) for j in xrange(c)
                     if rows[i][j] != '?'}
        
        for i, j in sorted(positions, key = lambda (i,j):(j,i)):
            child = positions[(i, j)]
            i_upper_pointer = i + 1
            while i_upper_pointer < r and rows[i_upper_pointer][j] == '?':
                rows[i_upper_pointer][j] = child
                i_upper_pointer += 1
            
            i_lower_pointer = i - 1
            while i_lower_pointer >= 0 and rows[i_lower_pointer][j] == '?':
                rows[i_lower_pointer][j] = child
                i_lower_pointer -= 1
                
            j_pointer = j - 1
            while j_pointer >= 0 and rows[i][j_pointer] == '?':
                for i_pointer in xrange(i_lower_pointer + 1, i_upper_pointer):
                    rows[i_pointer][j_pointer] = child
                j_pointer -= 1
        
        for i in xrange(r):
            for j in xrange(1, c):
                if rows[i][j] == '?':
                    rows[i][j] = rows[i][j-1]
        
        print "Case #{}:".format(tc + 1)
        for row in rows:
            print ''.join(row)
    