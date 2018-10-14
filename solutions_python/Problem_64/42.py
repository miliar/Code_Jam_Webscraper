M = 0
N = 0
MAX_M = 512

row_match = [None]*MAX_M
for size in range(2, MAX_M):
    t = 1
    arrF = [0]*size
    arrT = [1]*size
    for i in range(1, size):
        arrF[i] = t
        t ^= 0x1
        arrT[i] = t
    row_match[size] = [arrF, arrT]

#print row_match

def check_set(rows, i, j, size):
    if i + size > M or j + size > N:
        return False
    first = rows[i][j]
    for ii in range(i, i + size):
        if rows[ii][j:j+size] != row_match[size][first]:
            return False
        first ^= 0x1
    return True

def check_edges(rows, i, j, size, frl):
    if i + size > M or j + size > N:
        return False
    c = frl
    col_edge = j + size - 1
    for ii in range(i, i + size):
        if c != rows[ii][col_edge]:
            return False
        c ^= 0x1
    row_edge = i + size - 1
    c = frl
    for jj in range(j, j + size - 1):
        if c != rows[row_edge][jj]:
            return False
        c ^= 0x1
    return True

def get_largest_board(rows):
    largest_side = 0
    largest_pos = (-1, -1)
    for i in range(M):
        for j in range(N):
            if rows[i][j] != 2:
                if largest_side == 0:
                    largest_side = 1
                    largest_pos = (i, j)  
                size = largest_side + 1
                if not check_set(rows, i, j, size):
                    continue
                first = rows[i][j]
                while 1:
                    largest_side = size
                    size += 1
                    frl = ((~(size & 0x1)) & 0x1) if not first else (size & 0x1)
                    if not check_edges(rows, i, j, size, frl):
                        break
                largest_pos = (i, j)
                        
                    
                    
                    
    if largest_side == 0:
        return -1
    Mi = largest_pos[0]
    Ni = largest_pos[1]
    for i in range(Mi, Mi + largest_side):
        for j in range(Ni, Ni + largest_side):
            rows[i][j] = 2
    return largest_side
                    
                

f = open('C-small-attempt1.in', 'r')
T = int(f.readline().strip())
for case in range(T):
    M, N = map(int, f.readline().strip().split())
    rows = [0]*M
    for i in range(M):
        s = f.readline().strip()
        col = []
        for c in s:
            bits = int(c, 16)
            col.extend([1 if bits & 0x8 else 0,
                        1 if bits & 0x4 else 0,
                        1 if bits & 0x2 else 0,
                        1 if bits & 0x1 else 0])
        rows[i] = col
    #for row in rows:
    #    print row
    ls = get_largest_board(rows)
    counts = [0]*MAX_M
    while ls != -1:
        counts[ls] += 1
        ls = get_largest_board(rows)
    tcount = 0
    for i in range(MAX_M - 1, -1, -1):
        if counts[i] != 0:
            tcount += 1
    print "Case #%d: %d" % (case + 1, tcount)
    for i in range(MAX_M - 1, -1, -1):
        if counts[i] != 0:
            print i, counts[i]
        
    
            
        
