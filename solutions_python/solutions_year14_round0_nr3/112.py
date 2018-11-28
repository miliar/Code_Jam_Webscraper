import sys
def draw_1_dim (R, C, M):
    res = []
    for a in range(R):
        res.append(['*' for x in range(C)])
    for i in range(R):
        for j in range(C):
            if (i+j)<(R*C-M):
                res[i][j] = '.'
    res[0][0] = 'c'
    return res

def draw_2_dim (R, C, M):
    res = []
    for a in range(R):
        res.append(['*' for x in range(C)])
    if R==2:
        for i in range(C-M/2-M%2):
            res[0][i] = '.'
            res[1][i] = '.'
    else:
        for i in range(R-M/2-M%2):
            res[i][0] = '.'
            res[i][1] = '.'
    res[0][0] = 'c'
    return res

def transpose(r):
    return [list(i) for i in zip(*r)]

def draw_n_dim (R, C, M):
    res = [['.' for z in range(C)] for x in range(R)]
    emp = R*C-M
    orient = 1
    if emp <= 9:
        res[0][0] = 'c'
        for i in range(R):
            for j in range(C):
                if i>2 or j>2:
                    res[i][j] = '*'
        dm = 9 - emp
        #print 'dm %d' % dm
        if dm==1: res[2][2] = '*'
        if dm==3: res[0][2], res[1][2], res[2][2] = '*','*','*'
        if dm==5: res[0][2], res[1][2], res[2][2], res[2][0], res[2][1] = '*','*','*','*','*'
        if dm==8:
            for a in range(3):
                for b in range(3):
                    if a+b>0: res[a][b] = '*'
        if dm in (2,4,6,7): res = ['Impossible']
    else:
        dx, dy = min(R,C), max(R,C)
        dm = M    
        if dx != C:
            orient = 0
            res = transpose(res)
        while True:
            compl_lines = dm / dx
            if compl_lines > dy-3:
                compl_lines = dy-3
            #print 'dx=%d dy=%d dm=%d compl_lines=%d' % (dx, dy, dm, compl_lines)
            if compl_lines == 0:
                break
            for i in range(dy):
                if i >= dy - compl_lines:
                    for j in range(dx):
                        res[i][j] = '*'
            dy = dy - compl_lines
            dm = dm - compl_lines*dx
            if dy >= dx:
                break
            dx, dy = dy, dx
            orient = (orient + 1) % 2
            res = transpose(res)
        res[0][0] = 'c'
        if dm > 0:
            # dx <= dy && dm < dx
            for k in range(dy):
                x, y = 0, k
                while (y >= 0 and x < dx):
                    #print x, y, dx-1-x, dy-1-y
                    res[dy-1-y][dx-1-x] = '*'
                    x = x+1
                    y = y-1
                    dm -= 1
                    if dm == 0: break
                if dm == 0: break
    if orient == 0 and res[0] != 'Impossible':
        res = transpose(res)
    return res

f = sys.stdin
T = int(f.readline().strip())
for i in range(1,T+1):
    R, C, M = [int(x) for x in f.readline().strip().split(' ')]
    res = []
    if min(R,C)==1:
        res = draw_1_dim(R,C,M)
    else:
        if min(R,C)==2:
            emp = R*C-M
            if emp == 2 or (emp > 1 and emp%2==1):
                res = ['Impossible']
            else:
                res = draw_2_dim(R,C,M)
        else:
            res = draw_n_dim(R,C,M)
    sys.stdout.write('Case #%d:\n' % (i))
    #sys.stdout.write('%d %d %d\n' % (R,C,M))
    for a in range(len(res)):
        sys.stdout.write('%s\n' % (''.join(res[a])))