a = [['' for i in range (1, 12)] for j in range (1, 12)]
b = [['' for i in range (1, 12)] for j in range (1, 12)]
def check(a):
    for i in range (1, r+1):
        if a[i][1] == 1:
            can = True
            for j in range (2, c+1):
                if a[i][j] != 1:
                    can = False
                    break
            if can:
                for j in range(1, c+1):
                    b[i][j] = 1
    for j in range (1, c+1):
        if a[1][j] == 1:
            can = True
            for i in range (2, r+1):
                if a[i][j] != 1:
                    can = False
                    break
            if can:
                for i in range(1, r+1):
                    b[i][j] = 1
    m = True
    for i in range (1, r+1):
        for j in range (1, c+1):
            if a[i][j] == 1 and b[i][j] == 0:
                return 'NO'
    return 'YES'

file = open('B-small-attempt0.in')
outwrite = open('R2.txt', mode = 'w')
n = int(file.readline())
for m in range(1, n+1):
    size = file.readline().split(' ')
    r = int(size[0])
    c = int(size[1])
    for i in range (1, r+1):
        line = file.readline()
        for j in range(1, c+1):
            a[i][j] = int(line[(j-1)*2])
            b[i][j] = 0
    outwrite.write('Case #' + str(m)+ ': ' + check(a) + '\n')

file.close()
outwrite.close()
