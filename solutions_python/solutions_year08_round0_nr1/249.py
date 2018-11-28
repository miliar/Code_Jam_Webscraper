import sys
from pprint import pprint

def solve (engines, queries, costs):
    prev_best = engines[0]

    for query in queries:
        d = {}
        best = (sys.maxint, engines[0])

        for engine in engines:
            if engine == query:
                d[engine] = sys.maxint
            else:
                not_changing = costs[-1][engine]
                changing = 1 + costs[-1][prev_best]

                d[engine] = min(not_changing, changing)
            best = min(best, (d[engine], engine))

        costs.append(d)
        prev_best = best[1]


n = int(raw_input())

for i in range(n):
    s = int(raw_input())
    engines = [raw_input() for _ in range(s)]
    q = int(raw_input())
    queries = [raw_input() for _ in range(q)]

    costs = [dict((engine, 0) for engine in engines)]
    solve(engines, queries, costs)

    print 'Case #%i: %i' % (i+1, min(costs[-1].values()))
