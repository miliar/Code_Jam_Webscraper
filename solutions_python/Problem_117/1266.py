class Cell:
    def __init__(self, n):
        self.n = n
        self.hway = 1
        self.vway = 1
    
    def __cmp__(self, other):
        return cmp(self.n, other.n)
    
    def __str__(self):
        return '({},{:d},{:d})'.format(self.n, self.hway, self.vway)
    
    def __repr__(self):
        return '({},{:d},{:d})'.format(self.n, self.hway, self.vway)

# read the source
f = open('B-large.in')
ncases = int(f.readline())
ret = ''
for icase in range(ncases):
    ret += 'Case #{}: '.format(icase+1)
    [N,M] = [int(x) for x in str(f.readline()).split(' ')]
    mat = [[]] * N
    # N = rows
    # M = cols
    for row in range(N):
        mat[row] = [Cell(int(x)) for x in str(f.readline()).split(' ')]
    
    for row in mat:
        cmax = max(row)
        for c in row:
            c.hway = c.n >= cmax.n
    
    for col in [[row[i] for row in mat] for i in range(M)]:
        cmax = max(col)
        for c in col:
            c.vway = c.n >= cmax.n
    
    valid = True
    for row in mat:
        for c in row:
            if not valid: break
            if c.vway+c.hway == 0: 
                valid = False
                break
    if valid: ret += 'YES'
    else: ret += 'NO'
    
    ret += '\n'

f.close()

# write the solution
f = open('out.txt', 'w')
f.write(ret)
f.close()
print ret