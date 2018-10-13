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
    N,=read_tuple(f)
    lines=[read_line(f) for _ in xrange(N)]
    return lines


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases





def blockable(ms, ws):
    if not ms:
        return True
    if not ws:
        return False
    for m in ws[0]:
        if blockable(ms-{m},ws[1:]):
            return True
def valid(w2m):
    for w,ms in w2m.iteritems():
        ws=[w2m[i] for i in xrange(len(w2m)) if i!=w]
        if blockable(ms,ws):
            return False
    return True
def s2w(s, N):
    w2m=dict([ (i,set()) for i in xrange(N) ])
    for i in xrange(N):
        for j in xrange(N):
            if s[i*N+j]=="1":
                w2m[i].add(j)
    return w2m
def s2s(s):
    r=set()
    for i,c in enumerate(s):
        if c=="1":
            r.add(i)
    return r
        

def valid_idx_table(N):
    fmt="{:0"+str(N*N)+"b}"
    t=[]
    p=2**(N**2-2)
    for i in xrange(2**(N**2)):
        s=fmt.format(i)
        w2m=s2w(s,N)
        if valid(w2m):
            t.append(s2s(s))
        if (i+1)%p==0:
            print "#"
    return t

vidxts=[valid_idx_table(n) for n in [1,2,3,4]]

def solve(case):
    lines=case
    N=len(lines)
    s=s2s("".join(lines))
    vt=vidxts[N-1]
    minp=N**2+1
    for v in vt:
        if s<v:
            minp=min(minp,len(v-s))
        elif s==v:
            return 0
    return minp






def outcome_string(outcome):
    ### IMPLEMENT ###
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