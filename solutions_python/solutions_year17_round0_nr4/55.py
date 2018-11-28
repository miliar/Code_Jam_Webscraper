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
    N,M=read_tuple(f)
    grid=[["."]*N for _ in xrange(N)]
    for _ in xrange(M):
        m,r,c=read_line(f).split()
        grid[int(r)-1][int(c)-1]=m
    return grid


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases


def calc_style(grid):
    N=len(grid)
    s=0
    for i in xrange(N):
        for j in xrange(N):
            if grid[i][j]=="o":
                s+=2
            elif grid[i][j]!=".":
                s+=1
    return s

def cc(c1, c2):
    if c1=="o" or c1==c2:
        return c2
    return "."





# def get_updatable(grid, cons):
#     N=len(grid)
#     up={}
#     for i in xrange(N):
#         for j in xrange(N):
#             if cons[i][j]!="." and cons[i][j]!=grid[i][j]:
#                 up[(i,j)]=cons[i][j]
#     return up
# def clean_updatable(up, coord, grid, cons):
#     if not up:
#         return
#     i,j=coord
#     if (i,j) in up:
#         if grid[i][j]==cons[i][j]:
#             del up[(i,j)]
#         elif up[(i,j)]!=cons[i][j]:
#             up[(i,j)]=cons[i][j]
# def up_constraints(grid, cons, coord, up=None):
#     N=len(grid)
#     i,j=coord
#     if grid[i][j] in "xo":   
#         for k in xrange(N):
#             if i!=k:
#                 cons[k][j]=cc(cons[k][j],"+")
#                 clean_updatable(up,(k,j),grid,cons)
#             if j!=k:
#                 cons[i][k]=cc(cons[i][k],"+")
#                 clean_updatable(up,(i,k),grid,cons)
#     if grid[i][j] in "+o":
#         for dk in xrange(-N,N):
#             if dk and (i+dk)>=0 and (j+dk)>=0 and (i+dk)<N and (j+dk)<N:
#                 cons[i+dk][j+dk]=cc(cons[i+dk][j+dk],"x")
#                 clean_updatable(up,(i+dk,j+dk),grid,cons)
#             if dk and (i+dk)>=0 and (j-dk)>=0 and (i+dk)<N and (j-dk)<N:
#                 cons[i+dk][j-dk]=cc(cons[i+dk][j-dk],"x")
#                 clean_updatable(up,(i+dk,j-dk),grid,cons)
# def build_constraints(grid):
#     N=len(grid)
#     cons=[["o"]*N for _ in xrange(N)]
#     for i in xrange(N):
#         for j in xrange(N):
#             up_constraints(grid,cons,(i,j))
#     return cons
# 
# def solve_greedy(grid):
#     cons=build_constraints(grid)
#     add_lst=[]
#     up=get_updatable(grid,cons)
#     while True:
#         if not up:
#             break
#         i,j=up.popitem()[0]
#         nc=cons[i][j]
#         add_lst.append((nc,i,j))
#         grid[i][j]=nc
#         up_constraints(grid,cons,(i,j),up)
#     return calc_style(grid),add_lst






# def up_constraints(grid, cons, coord):
#     N=len(grid)
#     i,j=coord
#     if grid[i][j] in "xo":   
#         for k in xrange(N):
#             if i!=k:
#                 cons[k][j]=cc(cons[k][j],"+")
#             if j!=k:
#                 cons[i][k]=cc(cons[i][k],"+")
#     if grid[i][j] in "+o":
#         for dk in xrange(-N,N):
#             if dk and (i+dk)>=0 and (j+dk)>=0 and (i+dk)<N and (j+dk)<N:
#                 cons[i+dk][j+dk]=cc(cons[i+dk][j+dk],"x")
#             if dk and (i+dk)>=0 and (j-dk)>=0 and (i+dk)<N and (j-dk)<N:
#                 cons[i+dk][j-dk]=cc(cons[i+dk][j-dk],"x")
# def build_constraints(grid):
#     N=len(grid)
#     cons=[["o"]*N for _ in xrange(N)]
#     for i in xrange(N):
#         for j in xrange(N):
#             up_constraints(grid,cons,(i,j))
#     return cons
# 
# def get_updates(grid, cons):
#     N=len(grid)
#     up=set()
#     for i in xrange(N):
#         for j in xrange(N):
#             c,g=cons[i][j],grid[i][j]
#             if (c=="o" and g in ".+") or (c=="x" and g=="."):
#                 up.add((i,j,"x"))
#             if (c=="o" and g in ".x") or (c=="+" and g=="."):
#                 up.add((i,j,"+"))
#     return up
# def get_conflicts(up, N):
#     all_confs={}
#     for (i,j,c) in up:
#         if c=="x":
#             cconf=set()
#             for dk in xrange(-N,N):
#                 if dk and i+dk>=0 and i+dk<N and ((i+dk,j,"x") in up):
#                     cconf.add((i+dk,j))
#                 if dk and j+dk>=0 and j+dk<N and ((i,j+dk,"x") in up):
#                     cconf.add((i,j+dk))
#             all_confs[(i,j,"x")]=cconf
#         if c=="+":
#             cconf=set()
#             for dk in xrange(-N,N):
#                 if dk and i+dk>=0 and i+dk<N and j+dk>=0 and j+dk<N and ((i+dk,j+dk,"+") in up):
#                     cconf.add((i+dk,j+dk))
#                 if dk and i+dk>=0 and i+dk<N and j-dk>=0 and j-dk<N and ((i+dk,j-dk,"+") in up):
#                     cconf.add((i+dk,j-dk))
#             all_confs[(i,j,"+")]=cconf
#     return all_confs
# 
# def del_update(all_confs, sup):
#     cconf=all_confs.pop(sup)
#     for (i,j) in cconf:
#         all_confs[(i,j,sup[2])].remove(sup[:2])
# def up_conflicts(all_confs, sup):
#     cconf=all_confs[sup]
#     for (i,j) in cconf.copy():
#         del_update(all_confs,(i,j,sup[2]))
#     del all_confs[sup]





def up_constraints(grid, cons, coord):
    N=len(grid)
    i,j=coord
    if grid[i][j] in "xo":   
        for k in xrange(N):
            if i!=k:
                cons[k][j]=cc(cons[k][j],"+")
            if j!=k:
                cons[i][k]=cc(cons[i][k],"+")
    if grid[i][j] in "+o":
        for dk in xrange(-N,N):
            if dk and (i+dk)>=0 and (j+dk)>=0 and (i+dk)<N and (j+dk)<N:
                cons[i+dk][j+dk]=cc(cons[i+dk][j+dk],"x")
            if dk and (i+dk)>=0 and (j-dk)>=0 and (i+dk)<N and (j-dk)<N:
                cons[i+dk][j-dk]=cc(cons[i+dk][j-dk],"x")
def build_constraints(grid):
    N=len(grid)
    cons=[["o"]*N for _ in xrange(N)]
    for i in xrange(N):
        for j in xrange(N):
            up_constraints(grid,cons,(i,j))
    return cons

def get_updates(grid, cons):
    N=len(grid)
    up=set()
    for i in xrange(N):
        for j in xrange(N):
            c,g=cons[i][j],grid[i][j]
            if (c=="o" and g in ".+") or (c=="x" and g=="."):
                up.add((i,j,"x"))
            if (c=="o" and g in ".x") or (c=="+" and g=="."):
                up.add((i,j,"+"))
    return up
def get_conflicts(up, N):
    all_confs={}
    for (i,j,c) in up:
        if c=="x":
            cconf=0
            for k in xrange(N):
                if k!=i and ((k,j,"x") in up):
                    cconf+=1
                if k!=j and ((i,k,"x") in up):
                    cconf+=1
            all_confs[(i,j,"x")]=cconf
        if c=="+":
            cconf=0
            for dk in xrange(-min(i,j),N-max(i,j)):
                if dk and ((i+dk,j+dk,"+") in up):
                    cconf+=1
            for dk in xrange(-min(i,N-j-1),N-max(i,N-j-1)):
                if dk and ((i+dk,j-dk,"+") in up):
                    cconf+=1
            all_confs[(i,j,"+")]=cconf
    return all_confs

def dec_conf(sup, all_confs):
    if sup in all_confs:
        all_confs[sup]=all_confs[sup]-1
def del_update(all_confs, sup, N):
    if sup not in all_confs:
        return
    del all_confs[sup]
    i,j,c=sup
    if c=="x":
        for k in xrange(N):
            dec_conf((k,j,"x"),all_confs)
            dec_conf((i,k,"x"),all_confs)
    elif c=="+":
        for dk in xrange(-min(i,j),N-max(i,j)):
            dec_conf((i+dk,j+dk,"+"),all_confs)
        for dk in xrange(-min(i,N-j-1),N-max(i,N-j-1)):
            dec_conf((i+dk,j-dk,"+"),all_confs)
def up_conflicts(all_confs, sup, N):
    i,j,c=sup
    del all_confs[sup]
    if c=="x":
        for k in xrange(N):
            del_update(all_confs,(k,j,"x"),N)
            del_update(all_confs,(i,k,"x"),N)
    elif c=="+":
        for dk in xrange(-min(i,j),N-max(i,j)):
            del_update(all_confs,(i+dk,j+dk,"+"),N)
        for dk in xrange(-min(i,N-j-1),N-max(i,N-j-1)):
            del_update(all_confs,(i+dk,j-dk,"+"),N)


def apply_ups(ups_lst, grid):
    add_set={}
    for i,j,c in ups_lst:
        if grid[i][j]==".":
            grid[i][j]=c
            add_set[(i,j)]=c
        else:
            grid[i][j]="o"
            add_set[(i,j)]="o"
    return [(c,i,j) for (i,j),c in add_set.iteritems()]
def solve_greedy(grid):
    N=len(grid)
    cons=build_constraints(grid)
    up=get_updates(grid,cons)
    all_confs=get_conflicts(up,N)
    ups_lst=[]
    while all_confs:
        minup=min([(conf,sup) for (sup,conf) in all_confs.iteritems()])[1]
        #minup=all_confs.iterkeys().next()
        up_conflicts(all_confs,minup,N)
        ups_lst.append(minup)
    old_style=calc_style(grid)
    add_lst=apply_ups(ups_lst,grid)
    new_style=calc_style(grid)
    assert old_style+len(ups_lst)==new_style
    return new_style,add_lst


def solve(case):
    return solve_greedy(case)



    
def ln2grid(ln):
    N=int(len(ln)**.5)
    return [[ln[i*N+j] for j in xrange(N)] for i in xrange(N)]
tgrid=ln2grid("...+++x..") 




def outcome_string(outcome):
    style,add_lst=outcome
    return "\n".join(["{} {}".format(style,len(add_lst))]+["{} {} {}".format(c,i+1,j+1) for (c,i,j) in add_lst])


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