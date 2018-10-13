import sys

n = int(sys.stdin.readline())
search_engines = {}

for c in range(n):
    result = 0
    s = int(sys.stdin.readline())
    for i in range(s):
        name = sys.stdin.readline().strip()
        search_engines[name] = 0;
    q = int(sys.stdin.readline())
    matches = 0
    for i in range(q):
        query = sys.stdin.readline().strip()
        if search_engines[query] == 0:
            matches += 1
            search_engines[query] = 1
            if matches == s:
                result += 1
                for name in search_engines:
                    search_engines[name] = 0;
                search_engines[query] = 1
                matches = 1
    print "Case #%d: %d" % (c+1, result)
