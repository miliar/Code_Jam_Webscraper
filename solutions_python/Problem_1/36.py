f = file('A-large.in', 'r')
#f = file('test.in', 'r')

N = int(f.readline())

for n in range(N):
    eng = {}
    S = int(f.readline())
    for s in range(S):
        eng[s] = f.readline().strip()
    Q = int(f.readline())
    queries = []
    for q in range(Q):
        queries.append(f.readline().strip())

    if Q == 0:
        print "Case #%d: %d" % (n+1, 0)
        continue

    table = []
    for s in range(S):
        if queries[Q-1] == eng[s]:
            row = [0]
        else:
            row = [1]
        for q in range(Q-2, -1, -1):
            if queries[q] == eng[s]:
                row.append(0)
            else:
                row.append(row[-1] + 1)
        table.append(list(reversed(row)))

    pos = 0
    c = -1
    while pos < Q:
        next = 0
        for s in range(S):
            if next < table[s][pos]:
                next = table[s][pos]
        c += 1
        pos += next
    
    print "Case #%d: %d" % (n+1, c)
    
