import psyco
psyco.full()

def best_engine(engines, queries):
    best = None
    max_noswitch = 0
    for e in engines:
        try:
            noswitch = queries.index(e)
            if noswitch > max_noswitch:
                best = e
                max_noswitch = noswitch
        except ValueError:
            return e
    return best
        

def min_switchs(engines, queries, current_engine = None):
    if len(queries) == 0:
        return 0
    elif current_engine == None or queries[0] == current_engine:
        rest = min_switchs(engines, queries[1:], best_engine(engines, queries))
        if current_engine == None:
            return rest
        else:
            return rest + 1
    else:
        return min_switchs(engines, queries[1:], current_engine)
    
if __name__ == '__main__':
    N = input()
    for n in range(N):
        S = input()
        engines = []
        for s in range(S):
            engines.append(raw_input())

        Q = input()
        queries = []
        for q in range(Q):
            queries.append(raw_input())

        print "Case #%d: %d" % (n + 1, min_switchs(engines, queries))





