'''
Created on 13.04.2013

@author: Alex
'''

def solve1Or2(matrix, r, c, m):
    matrix[r-1][c-1] = 'c'
    if c < r or c == 1 or r == 1:
        currentM = 0
        for i in range(0, r):
            for j in range(0, c):
                if currentM < m:
                    currentM += 1
                    matrix[i][j] = '*'
                else:
                    break
    else:         
        currentM = 0
        for j in range(0, c):
            for i in range(0, r):
                if currentM < m:
                    currentM += 1
                    matrix[i][j] = '*'
                else:
                    break
                
def solve(matrix, r, c, m):
    matrix[r-1][c-1] = 'c'
    currentM = 0
    currentI = 0
    currentJ = 0
    for i in range(0, r-3):
        for j in range(0, c):
            if currentM < m:
                currentI = i
                currentJ = j
                currentM += 1
                matrix[i][j] = '*'
            else:
                break
    # print(str(currentI) + ' ' + str(currentJ))
    if currentJ == c-2 and currentI < r-1:
        matrix[currentI][currentJ] = '.'
        matrix[currentI+1][0] = '*'
    if currentM < m:
        newCount = 0
        for j in range(0, c-3):
            for i in range(r-3, r):
                if currentM < m:
                    currentI = i
                    currentJ = j
                    currentM += 1
                    newCount += 1
                    matrix[i][j] = '*'
                else:
                    break
        if newCount % 3 == 2:
            matrix[currentI][currentJ] = '.'
            matrix[currentI-1][currentJ+1] = '*'
    if currentM < m:
        if m - currentM == 1:
            matrix[r-3][c-3] = '*'
        if m - currentM == 3:
            matrix[r-3][c-3] = '*'
            matrix[r-2][c-3] = '*'
            matrix[r-1][c-3] = '*'
        if m - currentM == 5:
            matrix[r-3][c-3] = '*'
            matrix[r-2][c-3] = '*'
            matrix[r-1][c-3] = '*'
            matrix[r-3][c-2] = '*'
            matrix[r-3][c-1] = '*'
        if m - currentM == 8:
            matrix[r-3][c-3] = '*'  
            matrix[r-2][c-3] = '*'
            matrix[r-1][c-3] = '*'
            matrix[r-3][c-2] = '*'
            matrix[r-2][c-2] = '*'
            matrix[r-1][c-2] = '*'
            matrix[r-3][c-1] = '*'
            matrix[r-2][c-1] = '*'              
def isPossible(a, b, m):
    # print('bad nr of mines = ' + str(list(map(lambda x: a*b-x, [2,3,5,7]))))
    if a == 2 and m == a * b - 2:
        return False
    elif a == 2 and m % 2 == 1 and m != a * b - 1:
        return False
    elif a > 2 and m in map(lambda x: a*b-x, [2,3,5,7]):
        return False
    return True 

if __name__ == '__main__':
    fileIn = open('in/C-large.in', mode='r')
    fileOut = open('out/C-large.out', mode='w')
    n = int(fileIn.readline())
    for i in range(1, n+1):
        line = fileIn.readline()
        time = 0
        r = int(line.split()[0])
        c = int(line.split()[1])     
        m = int(line.split()[2])
        # init matrix
        matrix = []
        for j in range(0, r):
            row = []
            for k in range(0, c):
                row.append('.')
            matrix.append(row)
        # solve
        possible = isPossible(min(r, c), max(r, c), m)
        if possible:
            if min(r, c) == 1 or min(r,c) == 2:
                solve1Or2(matrix, r, c, m)
            else:
                solve(matrix, r, c, m)
        # write result
        fileOut.write('Case #' + str(i) + ':\n')
        if not possible:
            fileOut.write('Impossible\n')
        else:
            for j in range(0, r):
                for k in range(0, c):
                    fileOut.write(matrix[j][k])
                fileOut.write('\n')
