from decimal import *
    
def cut_lawn(lawn, N, M):
    lawnT = []
    c_max = [0]*M
    r_max = [0]*N
    
    for i in range(N):
        r_max[i] = max(lawn[i])

    for j in range(M):
        rowT = []
        for i in range(N):
            rowT.append(lawn[i][j])
        lawnT.append(rowT)
        c_max[j] = max(lawnT[j])
    
    for i in range(N):
        for j in range(M):
            if lawn[i][j] < r_max[i] and lawn[i][j] < c_max[j]:
                return 'NO'

    return 'YES'
    
out = ''  
    
fin = open('C:/Users/Thomas/Downloads/B-large.in', 'r')
tests = int(fin.readline())
fout = open('C:/Users/Thomas/Downloads/output.out', 'w')
print 'Tests: ' + str(tests)

for test in range(tests):
    lawn = []
    nm = fin.readline()
    [N, M] = [int(x) for x in nm.split()]
    for i in range(N):
        line = fin.readline()
        lawn.append([int(x) for x in line.split()])

    res = cut_lawn(lawn, N, M)

    ans = 'Case #' + str(test+1) + ': ' + res + '\n'
    print ans
    out = out + ans

fin.close()
fout.write(out)
fout.close()
