def main():
    fi = open('A-small-attempt3.in')
    fo = open('A-small-attempt3.out', 'w')
    t = int(fi.readline())
    
    for i in range(t):
        tc = fi.readline().split()
        r,c = int(tc[0]), int(tc[1])
        matrix = []
        last = ''
        
        has_blue = False
        
        for x in range(r):
            matrix.append(list(fi.readline().rstrip()))
            
        #print matrix
        
        for x in range(r):
            last = ''
            for y in range(c):
                if last == '#' and matrix[x][y] == '#':
                    last = ''
                    lc = '/'
                    rc = '\\'
                    
                    if y > 1:
                        if matrix[x][y-2] == '/' and matrix[x][y-1] == '\\':
                            lc = '/'
                            rc = '\\'
                            
                    if x > 0:
                        if matrix[x-1][y-1] == '/' and matrix[x-1][y] == '\\':
                            lc = '\\'
                            rc = '/'
                    
                    matrix[x][y-1] = lc
                    matrix[x][y] = rc
                else:
                    last = matrix[x][y]
        
        for x in range(r):
            for y in range(c):
                if matrix[x][y] == '#':
                    has_blue = True
                    break
                
        result = ''
        if has_blue:
            result = 'Impossible'
            fo.write("Case #%d:\n%s\n" % (i+1, result))
            print "Case #%d:\n%s" % (i+1, result)
        else:
            
            fo.write("Case #%d:\n" % (i+1))
            print "Case #%d:" % (i+1)
            string = ''
            
            for x in range(r):
                for y in range(c):
                    string =  string + matrix[x][y]
                string = string + '\n'
                
            print string.rstrip()
            fo.write("%s\n" % string.rstrip())        

if __name__ == "__main__":
    main()