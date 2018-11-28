import sys
from itertools import izip, takewhile

costs = {}

def cost(d, N):
    if (d, N) not in costs:
        costs[(d,N)] =  d*N - ((d*(d-1)) // 2)
    return costs[(d, N)]

def build_map(Ms):

    events = {}
    
    for o, e, p in Ms:
        origin = events.get(o) or (0, 0)
        events[o] = (origin[0] + p, origin[1])
        exit = events.get(e) or (0, 0)
        events[e] = (exit[0], exit[1] + p)

    m = []

    start = 0
    total = 0

    events = events.items()
    events.sort()

    for s, (enter, leave) in events:
        if s != start:
            m.append((s - start, total))
            start = s
        total += (enter - leave)
   
    return m 

def solve(N, Ms):
    normal_cost = sum(p * cost(e - o, N) for (o, e, p) in Ms)

    m = build_map(Ms)
    routes = []

    while m:
        r = list(takewhile((lambda (d, p): p > 0), m))

        if r:
            distance = sum(d for (d, p) in r)
            people = min(p for (d, p) in r)

            for idx in xrange(len(r)):
                (d, p) = m[idx]
                m[idx] = (d, p-people)

            routes.append((distance, people))
        else:
            m = m[1:]

    new_cost = sum(p * cost(d, N) for (d, p) in routes)

    return normal_cost - new_cost

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for test in xrange(1, T+1):
        
        N, M = map(int, sys.stdin.readline().strip().split())

        Ms = [map(int, sys.stdin.readline().strip().split()) 
              for m in xrange(M)]

        loss = solve(N, Ms)

        sys.stdout.write("Case #{}: {}\n".format(test, loss % 1000002013))
        
