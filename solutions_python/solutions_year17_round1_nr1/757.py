import sys
T = int(sys.stdin.readline().strip())

for t in range(T):
    R, C = [int(i) for i in sys.stdin.readline().strip().split()]
    grid = [list(sys.stdin.readline().strip()) for r in range(R)]
    done = set()
    for row in range(R):
        for col in range(C):
            if grid[row][col] == '?': continue
            if grid[row][col] in done: continue
            done.add(grid[row][col])
            # try lr
            l = col-1
            while (l >= 0):
                if grid[row][l] != '?': break
                l -= 1
            l += 1
            r = col+1
            while (r < C):
                if grid[row][r] != '?': break
                r += 1
            r -= 1
            u = row-1
            while u >= 0:
                found = False
                for i in range(l,r+1):
                    if grid[u][i] != '?':
                        found  = True
                        break
                if found:
                    break
                u -= 1
            u += 1
            d = row+1
            while d < R:
                found = False
                for i in range(l,r+1):
                    if grid[d][i] != '?':
                        found  = True
                        break
                if found:
                    break
                d += 1
            d -= 1
            lr = (l, r, u, d)
            lrArea = (r-l+1)*(d-u+1)
            #print(lr)
            #print('lr =',lrArea)
            # try ud
            u = row-1
            while u >= 0:
                if grid[u][col] != '?': break
                u -= 1
            u += 1
            d = row+1
            while d < R:
                if grid[d][col] != '?': break
                d += 1
            d -= 1
            l = col-1
            while l >= 0:
                found = False
                for i in range(u,d+1):
                    if grid[i][l] != '?':
                        found = True
                        break
                if found:
                    break
                l -= 1
            l += 1
            r = col + 1
            while r < C:
                found = False
                for i in range(u, d+1):
                    if grid[i][r] != '?':
                        found = True
                        break
                if found:
                    break
                r += 1
            r -= 1
            udArea = (r-l+1)*(d-u+1)
            rect = (l, r, u, d) if udArea > lrArea else lr
            l, r, u, d = rect
            for i in range(l,r+1):
                for j in range(u, d+1):
                    grid[j][i] = grid[row][col]
    grid = '\n'.join([''.join(r) for r in grid])
    print('Case #{}:'.format(t+1))
    print(grid)
