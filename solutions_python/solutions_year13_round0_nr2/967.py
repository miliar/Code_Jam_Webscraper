import numpy

f = open("input")
f_out = open('output', 'w')

def Check(matrix, n, m, max_l, max_r):
    
    for i in range(n):
        for j in range(m):
            if (matrix.base[i][j] < max_l[i]) and (matrix.base[i][j] < max_r[j]):            
                return False
    return True

isCorrect = True

for i in range(int(f.readline())):
    n, m = f.readline()[:-1].split(' ')
    n = int(n)
    m = int(m)
    matrix = []
    max_line = []
    max_row = []
    
    for j in range(n):
        line = map(int, f.readline().replace('\n', '').split(' '))
        max_line.append(max(line))
        matrix.append(line)
    
    matrix = numpy.matrix(matrix)
    max_row = [matrix[:,j].max() for j in range(m)]
    
    if Check(matrix, n, m, max_line, max_row) == True:
        f_out.write("Case #%i: YES\n" % (i + 1))
    else:
        f_out.write("Case #%i: NO\n" % (i + 1))

        
f.close()
f_out.close()
print "done"
        