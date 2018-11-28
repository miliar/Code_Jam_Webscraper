def read_list(f):
    return [int(x) for x in f.readline().split()]
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





def solve_4(r,c):
    if r<=2:
        return False
    return True
def solve_5(r,c):
    if r==3 and c==5: # w doesn't fit to 3x5
        return False
    return True # 3x10 or 4x5 work always
def solve_6(r,c):
    if r<=3: # 3xn doesn't work due to parity
        return False
    return True # 4x6 works always
def solve(case):
    x,r,c=case
    r,c=min(r,c),max(r,c)
    if x>=7: # hole
        return False
    if (r*c)%x!=0: # filling number
        return False
    if r<(x+1)/2: # angled piece fit
        return False
    if x<=3: # 1,2 trivial, 3 works for (3n) x m and m>1
        return True
    if x==4:
        return solve_4(r,c)
    if x==5:
        return solve_5(r,c)
    if x==6:
        return solve_6(r,c)






def outcome_string(outcome):
    return "GABRIEL" if outcome else "RICHARD"


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