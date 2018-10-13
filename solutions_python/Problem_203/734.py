import sys
writeln=lambda x:sys.stdout.write(str(x)+"\n")
write=lambda x:sys.stdout.write(x)
def okay(r , c):
    return 0 <= r < R and 0 <= c < C and grid[r][c] == '?'

sys.stdout = open('output.txt', 'w')
with open('A-large.in') as f:
# with open('A-small-attempt4.in') as f:
# with open('input.txt') as f:
    T = int(f.readline().rstrip());
    for t in range(T):
        alpha=[0]*26
        R,C=map(int, f.readline().split())
        pos = []
        qpos = []
        grid = [['?']*C for _ in range(R)]
        dCnt = 0

        for i in range(R):
            line = f.readline().rstrip()
            for j in range(C):
                c = line[j]
                if c != '?':
                    alpha[ord(c)-65] = 1
                    pos.append((i,j))
                else:
                    qpos.append((i, j))
                    dCnt += 1
                grid[i][j] = c
        # print("*"*50)
        # print("CHECK INPUT!!")
        # for i in range(R):
        #     for j in range(C):
        #         write(str(grid[i][j]))
        #     write("\n")
        # print("*"*50)
        qCnt = 0
        while pos:
            row, col = cur = pos.pop()
            ch = grid[row][col]
            cursor = 1; buho = 1
            while True:
                nr,nc = row, col+cursor*buho
                if okay(nr, nc):                    
                    grid[nr][nc] = ch
                    qCnt += 1
                    cursor += 1
                    continue
                else:
                    if buho == -1:
                        break
                    buho = -1; cursor = 1

        if qCnt != dCnt:
            for i in range(R):
                for j in range(C):
                    ch = grid[i][j]
                    if ch == '?':
                        continue
                    cursor = 1; buho = 1
                    while True:
                        nr, nc = i+cursor*buho, j
                        if okay(nr, nc):
                            grid[nr][nc] = ch
                            qCnt += 1
                            cursor += 1
                        else:
                            if buho == -1:
                                break
                            buho = -1; cursor = 1        
        if qCnt != dCnt:
            for row, col in qpos:
                if grid[row][col] != '?':
                    continue
                ch = '?'
                for i in range(26):
                    if not alpha[i]:
                        ch = chr(i+65)
                        alpha[i] = 1
                        break
                cursor = 1; buho = 1
                grid[row][col] = ch
                while True:
                    nr,nc = row, col+cursor*buho
                    if okay(nr, nc):
                        grid[nr][nc] = ch
                        qCnt += 1
                        cursor += 1
                        continue
                    else:
                        if buho == -1:
                            break
                        buho = -1; cursor = 1
        



        write("Case #%d:\n" % (t+1))

        for i in range(R):
            for j in range(C):
                write(str(grid[i][j]))
            write("\n")
        
sys.stdout.close()



