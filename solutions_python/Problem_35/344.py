#vim: fileencoding=utf-8 :
import sys, string 

sinks=[]
alpha, map, matrix=None, None, None
MAX_LATTITUDE=20000

def read_n():
    return [int(n) for n in sys.stdin.readline().split()]

def read_map():
    h,w=read_n()
    map=[]
    for j in range(h):
        map.append(read_n())
    assert len(map)==h
    return h,w,map

def main():
    for casenum in range(read_n()[0]):
        one_case(casenum)

def one_case(casenum):
    global alpha, ialpha, matrix, map, W, H
    H,W,map=read_map()
    ialpha=alpha_iter()
    
    matrix=make_matrix(W,H)
    alpha=ialpha.next()
    for i in range(H):
        for j in range(W):
            flow(i, j, [])
    print 'Case #%d:' % (casenum+1)
    print_matrix() 

def flow(i, j, trails):
    global alpha, ialpha
    #print_matrix()
    try:
        mark(i,j,alpha)
    except ValueError:
        #print 'meet drainage basins'
        # 같은 drainage basins를 만났다 
        v=matrix[i][j]
        for row,col in trails: 
            matrix[row][col]=v   
        return

    smallest=map[i][j]
    dir=None
    dirs=[
        ('N', (i-1, j)),
        ('W', (i, j-1)),
        ('E', (i, j+1)),
        ('S', (i+1, j)),
    ]
    for d, (row, col) in dirs:
        if (row>=0 and col>=0) and (row<H and col<W):
            #print 'W, H, row, col, len(map), len(map[0])', W, H, row, col, len(map), len(map[0])
            altitude=map[row][col]
            if altitude < smallest:
                #print 'd, altitude, smallest', d, altitude, smallest
                smallest=altitude
                dir=d
    if dir:
        row,col=dict(dirs)[dir]
        #print 'dir, row, col: ', dir, row, col
        trails.append((i,j))
        flow(row, col, trails)
    else:
        sinks.append((i,j))
        alpha=ialpha.next()

def mark(row, col, alpha):
    assert row>=0 and col>=0
    #print 'matrix size, row, col', len(matrix), len(matrix[row]), row, col
    if matrix[row][col]!=0:
        raise ValueError('already marked')
    matrix[row][col]=alpha

def make_matrix(w, h):
    return [[0]*w for i in xrange(h)]

def alpha_iter():
    for c in string.lowercase:
        yield c

def print_matrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print matrix[i][j],
        print 

if __name__=='__main__':
    main()


