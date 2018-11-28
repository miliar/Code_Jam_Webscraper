def check(matrix, i, j):
    if matrix[i][j] == '#':
        if j+1 < len(matrix[i]) and matrix[i][j+1] == '#':
            if i+1 < len(matrix) and matrix[i+1][j] == '#':
                if matrix[i+1][j+1] == '#':
                    #print i, j, 1 
                    return 1
    #print i, j, 0
    return 0

def solve(matrix):
    new_matrix = {}
    for i in range(len(matrix)):
        new_matrix[i] = {}
        for j in range(len(matrix[0])):
            new_matrix[i][j] = '#'
    #print new_matrix
    
    for i, line in enumerate(matrix):
        for j, tile in enumerate(line):
            if tile == '.':
                new_matrix[i][j] = tile
                continue
            if new_matrix[i][j] != '#':
                continue
            elif tile == '#' and check(matrix, i, j):
                new_matrix[i][j] = '/'
                
                new_matrix[i][j+1] = '\\'
                
                new_matrix[i+1][j] = '\\'
                new_matrix[i+1][j+1] = '/'
    #print new_matrix

    for line in new_matrix:
        for tile in new_matrix[line]:
            if new_matrix[line][tile] == '#': return 'Impossible'
            
    return new_matrix
            
                
input = open('A-large.in', 'r')
output = open('a.out', 'w')

t = int(input.readline())
for case in range(1, t+1):
   
    rows, cols = map(int, input.readline().strip().split())

    matrix = []
    for i in range(rows):
        line = input.readline().strip()
        matrix.append(line)

    #print matrix
    
    result = solve(matrix)

    if result == 'Impossible':
        #print 'Case #'+str(case)+':', result    
        output.write("Case #%s: \n%s\n" %(case, result))
    else:
        #print 'Case #'+str(case)+':', result
        output.write("Case #%s:\n" %(case))
        for line in result:
            for tile in result[line]:
                output.write(result[line][tile])
            output.write('\n')
