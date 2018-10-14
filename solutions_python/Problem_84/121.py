import sys

def new_matrix(n, c):
    return [[['.']for j in range(c)]for i in range(n)]

def rep(m):
    if m == 'Impossible':return m + '\n'
    rv = ''
    for team in m:
        rv += ''.join(team) + '\n'
    return rv

def change(matrix, r, c):
    first = True
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '#' :
                matrix[i][j] = '/'
                try:
                    if matrix[i][j + 1] != '#' or matrix[i + 1][j] != '#' or matrix[i + 1][j + 1] != '#':
                        return 'Impossible'
                    else:
                        matrix[i][j + 1] = '\\'
                        matrix[i + 1][j] = '\\'
                        matrix[i + 1][j + 1] = '/'
                except IndexError:
                    return 'Impossible'
            
                    
    return matrix


def solve(f):
    f = open(f)
    w = open('out.txt', 'w')
    # Read the number of cases
    T = int(f.readline())
    for t in range(T):
        R, C = map(int, f.readline().split())
        matrix = new_matrix(R, C)

        for r in range(R):
            matrix[r] = list(f.readline().rstrip())
#        print rep(matrix)
#        print 'After'
#        print rep(change(matrix, R, C))
        #N teams
        
        
        #Print output to file
        output = 'Case #{}:\n{}'.format(t + 1, rep(change(matrix, R, C)))
        print output
        w.write(output)
    
    f.close()
    w.close()




        
if __name__ == '__main__':
    solve('a-large.in')

    
