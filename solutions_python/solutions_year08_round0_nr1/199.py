def solve(engines, queries):
    used_engines = set()
    changes = 0
    for i in range(0, len(queries)):
        if not queries[i] in used_engines:
            used_engines.add(queries[i])
        if len(used_engines) == len(engines):
            used_engines = set([queries[i]])
            changes += 1
    return changes        

f = open("a-large.txt")
N = int(f.readline())
for n in range(0, N):
    S = int(f.readline())
    engines = [f.readline().rstrip() for s in range(0, S)]
    Q = int(f.readline())
    queries = [f.readline().rstrip() for q in range(0, Q)]
    print("Case #%d: %d" % (n + 1, solve(engines, queries)))
    
