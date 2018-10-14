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
    return read_tuple(f)


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases




def find_place(stalls):
    def calc_dist(row):
        o=-1
        d=[]
        for i,r in enumerate(row):
            if r:
                d.append(0)
                o=i
            else:
                d.append(i-o)
        return d
    dls=calc_dist(stalls)
    drs=calc_dist(stalls[::-1])[::-1]
    dss=zip(dls,drs)
    rnk=[(-min(dl,dr),-max(dl,dr),i) for (i,(dl,dr)) in enumerate(dss)]
    rnk.sort()
    return -rnk[0][0],-rnk[0][1],rnk[0][2]
def solve_bf(case):
    N,K=case
    stalls=[False]*N
    for _ in xrange(K):
        dmin,dmax,i=find_place(stalls)
        stalls[i]=True
    return dmax-1,dmin-1
def solve(case):
    N,K=case
    parts={N:1}
    while True:
        nmax=max(parts.keys())
        cnt=parts[nmax]
        if K>cnt:
            K-=cnt
            parts[nmax//2]=parts.get(nmax//2,0)+cnt
            parts[(nmax-1)//2]=parts.get((nmax-1)//2,0)+cnt
            del parts[nmax]
        else:
            return nmax//2,(nmax-1)//2






def outcome_string(outcome):
    return "{} {}".format(*outcome)


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