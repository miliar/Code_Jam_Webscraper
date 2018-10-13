modn=1000002013*2

# case = (N, [(o,e,p)])
def load_single_case(f):
    [N,M]=[int(n) for n in f.readline().split()]
    travels=[]
    for _ in xrange(M):
        [o,e,p]=[int(n) for n in f.readline().split()]
        travels.append((o,e,p))
    return (N,travels)


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases



def build_map(travels): # mp=( stations, flows, conn ); stations=[x]*n; flows=[f]*(n-1); 
    stations=set()
    for o,e,p in travels:
        stations.add(o)
        stations.add(e)
    stations=list(stations)
    stations.sort()
    st_dict=dict([(s,i) for i,s in enumerate(stations)])
    flows=[0]*(len(stations)-1)
    for o,e,p in travels:
        oi=st_dict[o]
        ei=st_dict[e]
        for i in xrange(oi,ei):
            flows[i]=flows[i]+p
    conns=[]
    start=0
    for i in range(len(flows)):
        if flows[i]==0:
            if start!=i:
                conns.append((start,i))
            start=i+1
    if start!=len(stations)-1:
        conns.append((start,len(stations)-1))
    return ( stations, flows, conns)

def del_max_conn(stations, flows, conns):
    max_l=conns[0][1]-conns[0][0]
    max_n=0
    for n,c in enumerate(conns[1:]):
        if c[1]-c[0]>max_l:
            max_l=c[1]-c[0]
            max_n=n
    if max_l==0:
        raise ValueError()
    o,e=conns[max_n]
    min_fl=min(flows[o:e])
    breaks=[]
    for i in xrange(o,e):
        flows[i]=flows[i]-min_fl
        if flows[i]==0:
            breaks.append(i)
    del conns[max_n]
    pb=o
    for b in breaks:
        if pb!=b:
            conns.append((pb,b))
        pb=b+1
    if pb!=e:
        conns.append((pb,e))
    return ((stations[e]-stations[o])**2*min_fl)
    
    

def solve(case):
    N,travels=case
    hon_gain=0
    for o,e,p in travels:
        hon_gain=(hon_gain+(e-o)**2*p) % modn
    mp=build_map(travels)
    ch_gain=0
    while len(mp[2]):
        ch_gain=(ch_gain+del_max_conn(*mp)) % modn
    return ((ch_gain-hon_gain) % modn)/2
    




def outcome_string(outcome):
    return str(outcome)


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