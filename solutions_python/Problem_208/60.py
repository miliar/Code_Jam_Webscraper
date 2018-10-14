from __future__ import division
import sys
from multiprocessing import Pool

# Add git repository with helpers to path
# The repo is publicly available at git@github.com:marcelka/cocoli.git
sys.path.append("/home/marcelka/projects/cocoli/")

def run(pool=None): # {{{
    inp=sys.argv[1]
    outp="%s.out" % inp.split(".")[0]

    with open(inp, 'r') as _file, open(outp, 'w') as out:
        _cases = int(_file.readline())
        arguments = []
        for _case in range(_cases):
            N, Q = tuple([int(x) for x in _file.readline().split(" ")])
            horses = []
            for _ in range(N):
                horses.append(tuple([int(x) for x in _file.readline().split(" ")]))
            dists = []
            for _ in range(N):
                dists.append(tuple([int(x) for x in _file.readline().split(" ")]))
            queries = []
            for _ in range(Q):
                queries.append(tuple([int(x) for x in _file.readline().split(" ")]))
            arguments.append((_case + 1, (N, Q, horses, dists, queries)))

        if pool == None:
            results = list(map(solve_wrapper, arguments))
        else:
            results = sorted(
                list(pool.imap_unordered(solve_wrapper, arguments)),
                key=lambda r: r[0])
        assert(len(results) == _cases)
        
        for _case, result in results:
            out.write("Case #%s: %s\n" % (_case, result))

def solve_wrapper(args):
    case_no, _args = args
    print("Solving case #%s" %(case_no))
    return (case_no, solve(*_args))
# }}}

from heapq import heappush, heappop

def memo(f, *args):
    cache = {}
    def memoized_f(*args):
        if args not in cache: cache[args] = f(*args)
        return cache[args]
    return memoized_f

def solve(N, Q, horses, dists, queries):
    @memo
    def neighs(i):
        e, s = horses[i]
        todo = [(0, i)]
        result = {}
        while todo:
            dist, city = heappop(todo)
            if dist > e:
                return result
            if city not in result:
                result[city] = dist / s
            for j in range(N):
                if dists[city][j] != -1 and j not in result:
                    heappush(todo, (dist + dists[city][j], j))
        return result

    def solve_query(u, v):
        todo = [(0, u)]
        done = set()
        while todo:
            time, city = heappop(todo)
            if city == v:
                return float(time)
            done.add(city)
            for ncity, ntime in neighs(city).items():
                if ncity not in done:
                    heappush(todo, (time + ntime, ncity))
                
    return " ".join("%s" % solve_query(u - 1, v - 1) for u, v in queries)

run()
#run(Pool(4))


#from random import randint
#
#for _ in range(10):
#    N = 100
#    Q = 100
#    horses = []
#    dists = []
#    queries = []
#    for i in range(N):
#        horses.append((randint(1, 10**9), 1000))
#        d = [randint(1, 10**9) for _ in range(N)]
#        d[i] = -1
#        dists.append(d)
#    for i in range(Q):
#        queries.append((randint(1, N), randint(1, N)))
#    print(solve(N, Q, horses, dists, queries))
