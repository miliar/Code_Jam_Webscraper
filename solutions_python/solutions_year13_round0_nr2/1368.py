def read_grass():
    n,m = raw_input().split()
    n = int(n)
    m = int(m)
    grass = list()
    for i in xrange(n):
        row = [int(i) for i in raw_input().split()]
        grass.append(row)
    return n, m, grass

def check_line(n,m,grass, i, j):
    return grass[i][j] == max(grass[i])

def check_column(n,m,grass, i, j):
    column = [ grass[x][j] for x in xrange(n) ]
    return grass[i][j] == max(column)

def analyse_grass(grass):
    n, m, grass = grass
    for i in xrange(n):
        for j in xrange(m):
            if not(check_line(n,m,grass,i,j) or check_column(n,m,grass,i,j)):
                return False
    return True
   
n_test_case = input()
for i in xrange(1, n_test_case+1):
    possible = analyse_grass(read_grass())
    print 'Case #%d: %s' % (i, 'YES' if possible else 'NO')

