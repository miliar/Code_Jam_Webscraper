import sys

def verify_all(matrix):
    won = '%s won'
    for i in xrange(0,4):
        row = get_row(matrix,i)
        result = verify(row,'X')
        if result != -1:
            return won % (result)
        else:
            result = verify(row,'O')
            if result != -1:
                return won % (result)
    for i in xrange(0,4):
        collumn = get_collumn(matrix,i)
        result = verify(collumn,'X')
        if result != -1:
            return won % (result)
        else:
            result = verify(collumn,'O')
            if result != -1:
                return won % (result)
    diagonal_main = get_diagonal_main(matrix)
    result = verify(diagonal_main,'X')
    if result != -1:
        return won % (result)
    else:
        result = verify(diagonal_main,'O')
        if result != -1:
            return won % (result)
    diagonal = get_diagonal_seccond(matrix)
    result = verify(diagonal,'X')
    if result != -1:
        return won % (result)
    else:
        result = verify(diagonal,'O')
        if result != -1:
            return won % (result)
    return draw_or_not_completed(matrix)

def verify(vector, player):
    result = -1
    for i in vector:
        if i == player or i == 'T':
            result = player
        else:
            result = -1
            return result
    return result

def get_collumn(matrix, n):
    collumn = []
    for i in xrange(0,4):
        collumn.append(matrix[i][n])
    return collumn

def get_row(matrix, n):
    return matrix[n]
    
def get_diagonal_main(matrix):
    diagonal = []
    for i in xrange(0,4):
        diagonal.append(matrix[i][i])
    return diagonal
    
def get_diagonal_seccond(matrix):
    diagonal = []
    for i in xrange(0,4):
        diagonal.append(matrix[3-i][i])
    return diagonal

def draw_or_not_completed(matrix):
    for row in matrix:
        for value in row:
            if value == '.':
                return 'Game has not completed'
    return 'Draw'
    
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        quantity = int(f.readline())
        for execution in xrange(quantity):
            matrix = []
            for i in xrange(0,4):
                row = f.readline()
                matrix.append((row[0],row[1],row[2],row[3]))
            f.readline()
            print 'Case #%i: %s' %(execution+1,verify_all(matrix))