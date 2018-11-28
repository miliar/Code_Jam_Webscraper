import sys

letters = 'abcdefghijklmnopqrstuvwxyz'
CURRENT_LETTER = -1

def test_cases(file):
    f = open(file)
    total = int(f.readline())
    for i in range(0,total):
        dims = f.readline().split()
        H = int(dims[0])
        W = int(dims[1])
        matrix = []
        for j in range(0,H):
            row = f.readline().split()
            row = map(lambda x: int(x), row)
            matrix.append(row)
        case = (H,W,matrix) 
        yield case
    f.close()

def init_solution(H,W):
    solution = []
    
    for i in range(0,H):
        row = []
        for j in range(0,W):
            row.append(None)
        solution.append(row)
    
    return solution

def is_marked(solution,pos):
    i,j = pos
    return solution[i][j] != None

def do_trail(trail, solution, letter):
    for pos in trail:
        i,j = pos
        solution[i][j] = letter

def next_letter():
    global CURRENT_LETTER
    CURRENT_LETTER += 1
    return letters[CURRENT_LETTER]

def sink(matrix, solution, i, j, H, W):
    trail = []
    next = (i,j)
    letter = None
    
    while next is not None:
        if is_marked(solution, next):
            i,j = next
            letter = solution[i][j]
            break
        trail.append(next)
        ni,nj = next
        next = next_move(matrix,ni,nj,H,W)
    
    if letter is None:
        letter = next_letter()
    
    do_trail(trail, solution, letter)
    
def next_move(matrix,i,j,H,W):
    next = None
    min = matrix[i][j]
    
    if i > 0 and matrix[i-1][j] < min:
        next = (i-1,j)
        min = matrix[i-1][j]
    if j > 0 and matrix[i][j-1] < min:
        next = (i,j-1)
        min = matrix[i][j-1]
    if j != (W-1) and matrix[i][j+1] < min:
        next = (i,j+1)
        min = matrix[i][j+1]
    if i != (H-1) and matrix[i+1][j] < min:
        next = (i+1,j)
        min = matrix[i+1][j]
    
    return next

def solve(case):
    H, W, matrix = case
    solution = init_solution(H,W)
    global CURRENT_LETTER
    CURRENT_LETTER = -1
    
    for i in range(0,H):
        for j in range(0,W):
            if solution[i][j] is None:
                sink(matrix,solution,i,j,H,W)
    
    return solution

def do_B(file):
    cases = test_cases(file) 
    for case in cases:
        solution = solve(case)
        yield solution

def output(solutions):
    f = open('C:\\output_B.txt', 'w')
    i = 1
    for solution in solutions:
        f.write("Case #%s:\r\n" % i)
        for row in solution:
            for col in row:
                f.write('%s ' % col)
            f.write('\r\n')
        i += 1
    f.close()

if __name__ == '__main__':
    solutions = do_B(sys.argv[1])
    output(solutions)