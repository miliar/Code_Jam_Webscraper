## Begin GCJ Library
abc = "abcdefghijklmnopqrstuvwxyz"
dirs = ((0,-1),(1,0),(0,1),(-1,0))

def memoizing(func):
    """Function decorator to cache a function's output."""
    memos = dict()
    def memoize(*args):
        if args in memos:
            return memos[args]
        res = func(*args)
        memos[args] = res
        return res
    return memoize
    
def cheapest_first_search(initial, max_cost, iter_func, test_func):
    if test_func(initial):
        return (0, initial)
    nodes = dict()
    new_nodes = {initial: 0}
    while len(new_nodes) > 0:
        node, cost = min(new_nodes.items(), key=lambda (k,v): v)
        new_nodes.pop(node)
        if node in nodes:
            continue
        if test_func(node):
            return (cost, node)
        nodes[node] = cost
        for nnode, ncost in iter_func(node):
            if not nnode in nodes and (not nnode in new_nodes or new_nodes[nnode] < cost + ncost):
                new_nodes[nnode] = cost + ncost

    return (None, None) 

def first(iter):
    for i, v in enumerate(iter):
        if v: return i
    return None
@memoizing
def factorial(k): return k <= 1 and 1 or k * factorial(k-1)
@memoizing
def combination(n, k): return n**k // factorial(k)
@memoizing
def permutation(n, k): return factorial(n) // factorial(n-k)

def tuple_replace(T, i, V):
    return tuple(n != i and T[n] or V for n in xrange(len(T)))

def tuple_replace2(T, i, j, V):
    return tuple_replace(T, i, tuple_replace(T[i], j, V))
    
def grid_get_points_where(G, func, func_takes_coords=False):
    for r in xrange(len(G)):
        for c in xrange(len(G[r])):
            if coords_as_args and func(G[r][c],r,c) or func(G[r][c]):
                yield (r,c)

def run_one(num_args):
    from time import time
    num, args = num_args
    start = time()
    res = solve_problem(*args)
    end = time()
    print "done %s in %2.2fs" % (num, end-start)
    return res

def run_all(multicore=False):
    from sys import argv
    fin = open(argv[1])
    fout = open(argv[1].replace("in", "out"), "w")
    numProblems = int(fin.readline())
    problem_list = [get_problem(lambda:fin.readline().strip('\n')) for i in range(numProblems)]
    
    if multicore:
        from multiprocessing import Pool
        p = Pool(8)
        solution_list = p.map(run_one, enumerate(problem_list))
    else:
        solution_list = map(run_one, enumerate(problem_list))
    for i, s in enumerate(solution_list):
        fout.write("Case #%s: %s\n" % (i + 1, s))
   
        
## END GCJ LIBRARY

def get_problem(get_line):
    K = int(get_line())
    B = [map(int, get_line().strip().split(' ')) for m in xrange(K)]
    return (K,B)
    
def convolve(B):
    A = dict()
    for x, r in B.items():
        for y in r.keys():
            if y-1 in r or (x-1 in B and y in B[x-1]):
                if not x in A: A[x] = dict()
                A[x][y] = 'S'
            if not y+1 in r and (x-1 in B and y+1 in B[x-1]):
                if not x in A: A[x] = dict()
                A[x][y+1] = 'G'
    return A
    
def solve_problem(N,B):
    grid = dict()
    for xa, ya, xb, yb in B:
        for x in xrange(xa, xb+1):
            if not x in grid: grid[x] = dict()
            for y in xrange(ya, yb+1):
                grid[x][y] = 1
    t = 0
    while len(grid) > 0:
        t+=1
        #print t
        #printgrid(6, grid)
        grid = convolve(grid)
        
    
    
    return t

def printgrid(S,A):
    for i in xrange(1,S+1):
        if not i in A:
            print '0' * S
        else:
            print ''.join(str(j in A[i] and A[i][j] or '0') for j in xrange(1,S+1))












    
if __name__ == '__main__': run_all(True)
