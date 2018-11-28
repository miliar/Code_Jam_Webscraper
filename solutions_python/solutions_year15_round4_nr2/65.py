def read_list(f):
    return [float(x) for x in f.readline().split()]
def read_tuple(f):
    return tuple(read_list(f))

def load_single_case(f):
    N,V,X=read_tuple(f)
    Ri,Ci=zip(*[read_flist(f) for _ in xrange(int(N))])
    return V,X,Ri,Ci


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases




def solve_1(V,X,Ri,Ci):
    assert len(Ri)==1
    assert len(Ci)==1
    if Ci[0]==X:
        return V/Ri[0]
    return None
def solve_2(V,X,Ri,Ci):
    assert len(Ri)==2
    assert len(Ci)==2
    hh=False
    hc=False
    for c in Ci:
        if c<=X:
            hc=True
        if c>=X:
            hh=True
    if not (hh and hc):
        return None
    if Ci[0]==Ci[1]:
        return V/(Ri[0]+Ri[1])
    if Ci[0]==X:
        return V/Ri[0]
    if Ci[1]==X:
        return V/Ri[1]
    r=(Ci[1]-X)/(X-Ci[0])
    V1,V2=V*r/(1.+r),V/(1.+r)
    return max(V1/Ri[0],V2/Ri[1])
def solve(case):
    V,X,Ri,Ci=case
    if len(Ri)==1:
        return solve_1(V,X,Ri,Ci)
    return solve_2(V,X,Ri,Ci)






def outcome_string(outcome):
    if outcome is None:
        return "IMPOSSIBLE"
    return "{:.10f}".format(outcome)


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