import sys

T = int(sys.stdin.readline())

for i in range(T):
    s = sys.stdin.readline().strip()
    N, M = s.split(' ')
    N = int(N)
    M = int(M)
    a = []
    for j in range(N):
        a.append([0]*M)
    grid = []
    for j in range(N):
        grid.append(sys.stdin.readline().strip().split(' '))

    for j in range(N):
        max_val = 0
        max_idx = []
        for k in range(M):
            if grid[j][k] > max_val:
                max_val = grid[j][k]
                max_idx = []
                max_idx.append(k)
            elif grid[j][k] == max_val:
                max_idx.append(k)
        for idx in max_idx:
            a[j][idx] = 1
    for j in range(M):
        max_val = 0
        max_idx = []
        for k in range(N):
            if grid[k][j] > max_val:
                max_val = grid[k][j]
                max_idx = []
                max_idx.append(k)
            elif grid[k][j] == max_val:
                max_idx.append(k)
        for idx in max_idx:
            a[idx][j] = 1
    ret = 'YES'
    for j in range(N):
        for k in range(M):
            if a[j][k] == 0:
                ret = 'NO'
    print "Case #" + str(i+1) + ": " + ret

        
