f = open('A-large.in')
output = open('A-large.out', 'w')

N = int(f.readline())
for n in range(1,N+1):
    S = int(f.readline())
    search_engs = dict()
    for s in range(0,S):
        search_engs[f.readline().strip('\n')] = None
    Q = int(f.readline())
    query_lst = []
    for q in range(0,Q):
        next = f.readline().strip('\n')
        query_lst.append(next)
        if search_engs[next] == None:
            search_engs[next] = query_lst.index(next)
        
    output.write('Case #%u: ' % n)
    switches = 0
    
    while len(query_lst) > 1:
        if None in search_engs.values():
            break
        else:
            last = max(search_engs.values())
            query_lst = query_lst[last:]
            for s in search_engs.iterkeys():
                if s in query_lst:
                    search_engs[s] = query_lst.index(s)
                else:
                    search_engs[s] = None
            switches += 1
                        
    output.write('%u\n' % switches)
output.close()
