import sys

def flow_matrix(matrix):
    dir_matrix = []
    for i in range(0, len(matrix)):
        dir_matrix.append(['X']*len(matrix[i]))
                   
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            min = matrix[i][j]
            direction = 'X'
            if (i > 0 and matrix[i-1][j] < min):
                min = matrix[i-1][j]
                direction = 'N'
            if (j > 0 and matrix[i][j-1] < min):
                min = matrix[i][j-1]
                direction = 'W'
            if (j < len(matrix[i]) - 1) and (matrix[i][j+1] < min):
                min = matrix[i][j+1]
                direction = 'E'
            if (i < len(matrix)-1 and matrix[i+1][j] < min):
                min = matrix[i+1][j]
                direction = 'S'

            dir_matrix[i][j] = direction

    label_map(dir_matrix)

    return dir_matrix


def label_map(matrix):
    global index
    index = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            dfs(matrix, i, j)

def dfs(matrix, i, j):
    global index
    if (matrix[i][j] == 'X'):
        matrix[i][j] = letters[index]
        index = index + 1        
    elif (matrix[i][j] == 'N'):
        matrix[i][j] = dfs(matrix, i-1, j)
    elif (matrix[i][j] == 'W'):
        matrix[i][j] = dfs(matrix, i, j-1)
    elif (matrix[i][j] == 'E'):
        matrix[i][j] = dfs(matrix, i, j+1)
    elif (matrix[i][j] == 'S'):
        matrix[i][j] = dfs(matrix, i+1, j)
    return matrix[i][j]

def main():

    with open(r'F:\Python_tut\CodeJam2009\B\B-large.in', 'r') as f:
        n = int(f.readline())
        
        for case in range(1, n+1):
            line = f.readline()
            [m, n] = line[:-1].split()
            matrix = []
            for i in range(0, int(m)):
                line = f.readline()
                row = [int(x) for x in line[:-1].split()]
                matrix.append(row)

            mat = flow_matrix(matrix)
            print('Case #%d:' % (case))
            for i in range(0, int(m)):
                for j in range(0, int(n)):
                    sys.stdout.write("%s " % mat[i][j])
                sys.stdout.write("\n")
                           
        

letters = "abcdefghijklmnopqrstuvwxyz"
index = 0


if __name__ == '__main__':
    main()
