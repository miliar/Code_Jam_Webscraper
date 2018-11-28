f = open("input")
f_out = open('output', 'w')

def Check(lines):
    for line in lines:    
        if '.' in line:
            continue
        if 'X' in line:
            if 'O' in line:
                continue
            else:
                return 'X'
        else:
            return 'O'

def CheckCulRow(matr):
    for i in range(4):
        # --- check lines ---
        l = matrix[i*4:i*4+4]
        
        # --- check row ---
        r = [matrix[i], matrix[i+4], matrix[i+8], matrix[i+12]]
        
        res = Check([l,r])
        if res == None:
            continue
        else:
            return res

count = int(f.readline())
for i in range(count):
    data = f.read(21)
    clearData = data.replace('\n', '')
    matrix = list(clearData)
    
    print "matrix %i: %r" % (i, matrix)
    if  len(matrix) == 16:
        res = CheckCulRow(matrix) 
        if res != None:
            f_out.write("Case #%i: %s won\n" % (i+1, res))
            continue
            
        # --- check diagonal ---
        d1 = [matrix[0], matrix[5], matrix[10], matrix[15]]
        d2 = [matrix[3], matrix[6], matrix[9], matrix[12]]
        
        res = Check([d1,d2])
        if res == None:
            if '.' in matrix:
                f_out.write("Case #%i: Game has not completed\n" % (i+1))
            else:
                f_out.write("Case #%i: Draw\n" % (i+1))
        else:
            f_out.write("Case #%i: %s won\n" % (i+1, res))
    
    ##f.read(1)



