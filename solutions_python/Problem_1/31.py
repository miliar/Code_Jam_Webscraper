from sys import stdin

read_int = lambda: int(stdin.readline().strip())
read_text = lambda: stdin.readline().strip()

N = read_int()

for n in range(N):
    S = read_int()
    engines = [read_text() for s in range(S)]
    # print engines
    Q = read_int()
    possibilities = engines[:]
    change = 0
    queries = [read_text() for q in range(Q)]
    # print queries
    for query in queries:
        try:
            possibilities.remove(query)
        except ValueError:
            pass
        if not possibilities:
            change += 1
            possibilities = engines[:]
            possibilities.remove(query)
    print 'Case #%d: %d' % (n+1, change)

