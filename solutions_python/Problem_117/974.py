import re

class lawn:
    def __init__(self, matrix, N, M):
        self.l = matrix
        self.rows = N
        self.cols = M

        
    def check_lawn(self):
        fail1 = False
        fail2 = False
        colBounds = []
        rowBounds = []
        for i in range(self.rows):
            rowBounds.append(-1)
        for i in range(self.cols):
            colBounds.append(-1)

        for i,row in enumerate(self.l):
            m = max(row)
            rowBounds[i] = m
            for j,elt in enumerate(row):
                if elt < m:
                    colBounds[j] = elt
                    
        
        for i in range(self.rows):
            for j in range(self.cols):
                if rowBounds[i] != -1 and colBounds[j] != -1:
                    if self.l[i][j] != min([rowBounds[i], colBounds[j]]):
                        fail1 = True
            
        colBounds = []
        rowBounds = []
        for i in range(self.rows):
            rowBounds.append(-1)
        for i in range(self.cols):
            colBounds.append(-1)
        for i in range(self.cols):
            col = []
            for row in self.l:
                col.append(row[i])
            m = max(col)
            colBounds[i] = m
            for j,elt in enumerate(col):
                if elt < m:
                    rowBounds[j] = elt

        for i in range(self.rows):
            for j in range(self.cols):
                if rowBounds[i] != -1 and colBounds[j] != -1:
                    if self.l[i][j] != min([rowBounds[i], colBounds[j]]):
                        fail2 = True

        if fail1 and fail2:
            return 'NO'
        else:
            return 'YES'
    
def solve(filename, output):
    results = []
    f = open(filename, 'r')
    p = re.compile(r'([0-9]+)')
    nCases = int(p.match(f.readline()).group())
    for i in range(nCases):
        m = p.findall(f.readline())
        rows  = int(m[0])
        cols = int(m[1])
        matrix = []
        for j in range(rows):
            m = p.findall(f.readline())
            matrix.append([])
            for k in range(cols):
                matrix[j].append(int(m[k]))
        l = lawn(matrix, rows, cols)
        results.append(l.check_lawn())
    f.close()
    f = open(output, 'w')
    for i,res in enumerate(results):
        f.write('Case #{}: '.format(i+1) + res + '\n')
    f.close()
