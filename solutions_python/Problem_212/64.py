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
    _,P=read_tuple(f)
    return P,read_list(f)


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases




def solve2(groups):
    ne=len([g for g in groups if g%2==0])
    no=len(groups)-ne
    return ne+(no+1)//2

def solve3(groups):
    n0=len([g for g in groups if g%3==0])
    n1=len([g for g in groups if g%3==1])
    n2=len([g for g in groups if g%3==2])
    return n0+min(n1,n2)+(abs(n1-n2)+2)//3

def solve4(groups):
    n0=len([g for g in groups if g%4==0])
    n1=len([g for g in groups if g%4==1])
    n2=len([g for g in groups if g%4==2])
    n3=len([g for g in groups if g%4==3])
    Ntot=n0
    Ntot+=min(n1,n3)
    nodd=abs(n1-n3)
    n2+=nodd//2
    Ntot+=n2//2
    if ((nodd%2)>0) or ((n2%2)>0):
        Ntot+=1
    return Ntot

def solve(case):
    P,groups=case
    if P==2:
        return solve2(groups)
    if P==3:
        return solve3(groups)
    if P==4:
        return solve4(groups)
    assert False






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