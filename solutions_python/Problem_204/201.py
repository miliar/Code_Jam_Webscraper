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
    N,P=read_tuple(f)
    req=read_list(f)
    packs=[read_list(f) for _ in xrange(N)]
    return req,packs


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases



def is_comp(req, pack):
    rng=None
    for r,p in zip(req,pack):
        #mins,maxs=int(np.ceil(p/(r*1.1))),int(np.floor(p/(r*0.9)))
        mins,maxs=p/(r*1.1),p/(r*0.9)
        if rng:
            rng=max(rng[0],mins),min(rng[1],maxs)
            if rng[1]<rng[0]:
                return False
        else:
            rng=mins,maxs
    if abs(mins-round(mins))<1E-9 or abs(maxs-round(maxs))<1E-9:
        return True
    return int(maxs)>int(mins)

# def find_match_bf(req, packs):
#     N,P=len(packs),len(packs[0])
#     assert N<3
#     match=[]
#     if n in xrange(N):
#         for p in xrange(P):

def rec_match(match, i, free):
    if i>=len(match):
        return 0
    max_m=0
    for f in free:
        if match[i][f]:
            free.remove(f)
            mm=rec_match(match,i+1,free)
            free.add(f)
            max_m=max(max_m,mm+1)
    max_m=max(max_m,rec_match(match,i+1,free))
    return max_m
def find_match_2(req, packs):
    P=len(packs[0])
    match=[[False]*P for _ in xrange(P)]
    for p1 in xrange(P):
        for p2 in xrange(P):
            match[p1][p2]=is_comp(req,[packs[0][p1],packs[1][p2]])
    return rec_match(match,0,set(range(P)))

def solve(case):
    req,packs=case
    if len(req)==1:
        return len([p for p in packs[0] if is_comp(req,[p])])
    if len(req)==2:
        return find_match_2(req, packs)
    return None






def outcome_string(outcome):
    return "{}".format(outcome)


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