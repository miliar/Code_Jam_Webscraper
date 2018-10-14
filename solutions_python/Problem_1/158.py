def solve(names, queries):
    switches = []
    engines2 = load(names, queries, True)
    engines3 = load(names, queries, False)
    l = (get_switches(engines2, queries, sortd),
         get_switches(engines3, queries, sortd),
         get_switches(engines2, queries, distance),
         get_switches(engines3, queries, distance))
    return min(l)

def get_switches(engines, queries, sort_method):
    switches = 0
    v = sort_method(queries, engines)
    if len(queries) == 0:
        return 0
    engine = switch(v, queries[0])
    for i,query in enumerate(queries):
        if query == engine:
            v = sort_method(queries[i+1:], engines)
            engine = switch(v, query)
            switches += 1
        engines[query] -= 1
    return switches

def load(names, queries, flag=False):
    engines = {}
    for name in names:
        if flag:
            engines[name] = 0
        else:
            engines[name] = queries.count(name)
    if flag:
        old = ""
        for query in queries:
            if old != query:
                engines[query] += 1
            old = query
    return engines

def removed(lis):
    old = None
    new_list = []
    for i in lis:
        if i == old:
            continue
        new_list.append(i)
        old = i
    return new_list

def switch(v, query):
    for name in v:
        if name != query:
            return name

def distance(queries, engines):
    l = []
    for query in queries: 
        if query not in l:
            l.append(query)
    for engine in engines:
        if not engine in l:
            l.append(engine)
    l.reverse()
    return l

def sortd(queries, engines):
    items=engines.items()
    backitems=[ [v[1],v[0]] for v in items]
    backitems.sort()
    return [ backitems[i][1] for i in range(0,len(backitems))]

def read_input():
    from sys import stdin
    N = int(stdin.readline())
    switches = []
    for n in range(N):
        S = int(stdin.readline())
        names = [ stdin.readline().strip() for i in range(S) ]
        Q = int(stdin.readline())
        queries = [ stdin.readline().strip() for i in range(Q) ]
        switches.append(solve(names, queries))
    for i, switch in enumerate(switches):
        print "Case #%d: %d" % (i+1, switch)

read_input()
