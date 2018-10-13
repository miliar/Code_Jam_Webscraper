import sys,string

BIG = 1000000

def mat_str(m):
    return string.join([string.join([str(x) for x in row], " ") for row in m], "\n")            
    

class Matrix:
    def __init__ (self, mat):
        self.mat = mat
        self.rows = len(mat)
        self.cols = len(mat[0])
    def __call__ (self, i, j):
        return self.mat[i][j]
    # up, left, down, right (north, west, esat, south)
    def get_neigh (self, i, j):
        l = []
        if i > 0:
            l.append((i-1,j))
        if j > 0:
            l.append((i,j-1))
        if j < self.cols - 1:
            l.append((i,j+1))
        if i < self.rows - 1:
            l.append((i+1,j))
        return l
    def get_min_neigh (self, i, j):
        (ni,nj) = i,j
        for (xi,xj) in self.get_neigh(i,j):
            if self(xi,xj) < self(ni,nj):
                (ni,nj) = (xi,xj)
        return (ni,nj)
    def __str__ (self):
        return mat_str(self.mat)


def make_mat(rows, cols):
     l = []
     for i in xrange(rows):
        l.append([])
        for j in xrange(cols):
            l[-1].append([])
     return l
     
def make_mat_val (rows, cols, value):
     l = []
     for i in xrange(rows):
        l.append([value] * cols)
     return l
        
def build_drain_tree( mat ):
     basins = []
     tree = make_mat(mat.rows, mat.cols)
     for i in xrange(mat.rows):
        for j in xrange (mat.cols):
            (ni,nj) = mat.get_min_neigh(i, j)
            if (ni,nj) == (i,j):
                basins.append( (i,j) )
            else:
                tree[ni][nj].append( (i,j) )
     return (basins,tree)
 
def recr_color_mat (out, color, tree, i,j): 
    assert out[i][j] == None, "%d %d %d %d" % (i, j, out[i][j], color)
    out[i][j] = color    
    for ni,nj in tree[i][j]:
        recr_color_mat(out, color, tree, ni, nj)
 
def color_mat (mat, basins, tree):
    out = make_mat_val(mat.rows, mat.cols, None)
    for color,b in enumerate(basins):
        recr_color_mat(out, color, tree, b[0], b[1])
    return out
        
def recolor_mat (mat):
    color_dict = {}
    max_color = 0
    for i in range (len(mat)):
        for j in range (len(mat[i])):
            if not color_dict.has_key(mat[i][j]):
                color_dict[mat[i][j]] = chr(ord('a') +  max_color)
                max_color += 1
            mat[i][j] = color_dict[mat[i][j]]
    return mat

def read_matrix(f, rows, cols):
    mat = []
    for i in range(rows):
        mat.append([int(x) for x in f.readline().strip().split(' ')])
    return mat
    
   
    
def read_file (filename):
    with open(filename) as f:
        T = int(f.readline().strip())
        for i in range(T):
            print "Case #%d:" % (i + 1)
            (rows,cols) = [int(x) for x in f.readline().strip().split(' ')]
            mat = Matrix(read_matrix(f,rows,cols))
            #print mat
            (basins,tree) = build_drain_tree(mat)
            output = recolor_mat(color_mat(mat, basins,tree))
            print mat_str(output)
            #test(mat.mat, output)
            
 

 
def test (input, output):
    def get(mat, i, j):
        if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
            return BIG
        return mat[i][j]
    def drains_to(m,i,j):
        l = [(i,j), (i-1,j),(i,j-1),(i,j+1),(i+1,j)]
        #print l, [get(m,x,y) for (x,y) in l]
        mn = min ( [get(m,x,y) for (x,y) in l] )
        res = [(x,y) for (x,y) in l if get(m,x,y) == mn][0]
        #print "point=(%d %d) drains to=(%d %d) with mn=%d" % (i,j,res[0],res[1], mn)
        return res

    for i in range(len(input)):
        for j in range(len(input[0])):
            ci,cj = i,j
            si,sj = drains_to(input,ci,cj)
            while (si,sj) != (ci,cj):
                ci,cj = si,sj
                si,sj = drains_to(input,ci,cj)
            #print "point=(%d %d) utlimately drains to=(%d %d)" % (i,j,si,sj)
            assert output[i][j] == output[ci][cj], "point=(%d %d) utlimately drains to=(%d %d)" % (i,j,si,sj)
            
    
    
read_file(sys.argv[1])