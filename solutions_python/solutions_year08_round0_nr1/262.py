def solve(engines,queries):
    """Solves the problem for one input instance."""
    notused=set(engines)
    lastengine=None
    switches=0
    first=False
    for query in queries:
        if query not in engines:
            continue
        notused-=set((query,))
        if not notused: #notused is empty
            lastengine=query
            switches+=1
            notused=set(engines)
            notused.remove(lastengine)
        else:
            pass
    return switches

if __name__=='__main__':
    import sys
    f=open(sys.argv[1],'rt')
    N=None
    S=0
    Q=0
    solutions=[]
    line=f.readline().strip()
    while not line=="":
        N=int(line)
        for i in range(N):
            S=int(f.readline().strip())
            engines=[]
            for j in range(S):
                engines.append(f.readline().strip())
            Q=int(f.readline().strip())
            queries=[]
            for j in range(Q):
                queries.append(f.readline().strip())
            solutions.append(solve(engines,queries))
        line=f.readline().strip()
    for (i,solution) in enumerate(solutions):
        print "Case #%(case_number)s: %(solution)s" % {
                'case_number': i+1,
                'solution': solution,
                }
