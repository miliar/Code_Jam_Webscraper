f = open('B-large.in', 'r')
g = open('output.txt', 'w')

n = int(f.readline())
count = 1

while count <= n:
    dim = f.readline().split()
    x, y = int(dim[0]), int(dim[1])
    matrix = []

    for i in xrange(x):
        line = f.readline()
        if '\n' in line:
            line = line[:-1]
        matrix.append([int(i) for i in line.split()])

    tryMatrix = [[100]*y for i in xrange(x)]
        
    for i in xrange(x):
        maxVal = max(matrix[i])
        for j in xrange(y):
            tryMatrix[i][j] = min(tryMatrix[i][j], maxVal)
        
    for j in xrange(y):
        maxVal = -1
        for i in xrange(x):
            maxVal = max(maxVal, matrix[i][j])
            
        for i in xrange(x):
            tryMatrix[i][j] = min(tryMatrix[i][j], maxVal)

    if matrix == tryMatrix:
        g.write("Case #" + str(count) + ": " + "YES" + '\n')
    else:
        g.write("Case #" + str(count) + ": " + "NO" + '\n')
        
    count += 1
    
f.close()
g.close()