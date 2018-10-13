import sys
sys.setrecursionlimit(10000)

def read_line(f):
    while True:
        s=f.readline().strip()
        if s:
            return s
def read_list(f):
    return [int(x) for x in read_line(f).split()]
def read_tuple(f):
    return tuple(read_list(f))

def load_single_case(f):
    R,_=read_tuple(f)
    return [list(f.readline().strip()) for _ in xrange(R)]


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases




# def fill_cells(i0, j0, grid):
#     R,C=len(grid),len(grid[0])
#     cc=None
#     for i in xrange(i0,R):
#         for j in xrange(j0,C):
#             if grid[i][j]!="?":
#                 cc=i,j
#                 break
#         if cc:
#             break
#     print (i0,j0),cc
#     if cc:
#         n=grid[cc[0]][cc[1]]
#         for i in xrange(i0,cc[0]+1):
#             for j in xrange(j0,cc[1]+1):
#                 grid[i][j]=n
#     else:
#         if i0>0:
#             grid[i0][j0]=grid[i0-1][j0]
#         else:
#             grid[i0][j0]=grid[i0][j0-1]

# 
# def find_max_rect(i0, j0, grid):
#     
#     for i in xrange(i0,R):
#         for j in xrange(j0,C):
#             if grid[i][j]!="?":
# def fill_cells(i0, j0, grid):
#     R,C=len(grid),len(grid[0])
#     cc=None
#     for i in xrange(i0,R):
#         for j in xrange(j0,C):
#             if grid[i][j]!="?":
#                 cc=i,j
#                 break
#         if cc:
#             break
#     cc=cc or (R,C)
#     n=grid[i0][j0]
#     for i in xrange(i0,cc[0]+1):
#         for j in xrange(j0,cc[1]+1):
#             grid[i][j]=n


def spread_lett(i0, j0, grid):
    R,C=len(grid),len(grid[0])
    n=grid[i0][j0]
    #fill line before
    if j0>0 and grid[i0][j0-1]=="?":
        for j in xrange(j0):
            grid[i0][j]=n
    #fill line after
    for j in xrange(j0+1,C):
        if grid[i0][j]=="?":
            grid[i0][j]=n
        else:
            break

def spread_row(i0, grid):
    R,C=len(grid),len(grid[0])
    #fill rows before
    if i0>0 and grid[i0-1][0]=="?":
        for i in xrange(i0):
            for j in xrange(C):
                grid[i][j]=grid[i0][j]
    #fill rows before
    for i in xrange(i0+1,R):
        if grid[i][0]=="?":
            for j in xrange(C):
                grid[i][j]=grid[i0][j]
        else:
            break

def solve(case):
    grid=case
    R,C=len(grid),len(grid[0])
    for i in xrange(R):
        for j in xrange(C):
            if grid[i][j]!="?":
                spread_lett(i,j,grid)
    for i in xrange(R):
        if grid[i][0]!="?":
            spread_row(i,grid)
#     for i in xrange(R-1,-1,-1):
#         for j in xrange(C-1,-1,-1):
#             if grid[i][j]=="?":
#                 if i<R-1:
#                     grid[i][j]=grid[i+1][j]
#                 else:
#                     grid[i][j]=grid[i][j+1]
    return grid






def outcome_string(outcome):
    return "\n"+"\n".join(["".join(r) for r in outcome])


def save_outcomes(path, outcomes):
    with open(path,'w') as f:
        for n,o in enumerate(outcomes):
            f.write("Case #{0}: {1}\n".format( n+1 , outcome_string(o) ))
def process(path_in, path_out=None):
    if path_out==None:
        path_out=path_in.rsplit(".",1)[0]+".out"
    cases=load_cases(path_in)
    outcomes=[solve(c) for c in cases]
    save_outcomes(path_out, outcomes)
    





########## SOLUTIONS TESTING ##########


def verify_outcome(case, outcome):
    ### IMPLEMENT ###
    return outcome==solve(case)

def test_solutions(path_in, until_first_fail=True):
    cases=load_cases(path_in)
    for cn,c in enumerate(cases):
        o=solve(c)
        if not verify_outcome(c,o):
            print "Wrong outcome!"
            print "Case #{0}:".format(cn)
            print c
            print "Outcome:"
            print o
            if until_first_fail:
                return c
            else:
                print "\n\n"
                
def gen_cases():
    ### IMPLEMENT ###
    return []

def test_solutions_gen(until_first_fail=True):
    cases=gen_cases()
    for cn,c in enumerate(cases):
        o=solve(c)
        if not verify_outcome(c,o):
            print "Wrong outcome!"
            print "Case #{0}:".format(cn)
            print c
            print "Outcome:"
            print o
            if until_first_fail:
                return c
            else:
                print "\n\n"