f = open('B-large.in')
out = open('out', 'w')

n = int(f.readline())

for i in xrange(1, n+1):
    n, m = map(int, f.readline().strip().split())

    lawn = []
    for j in xrange(n):
        lawn.append(map(int, f.readline().strip().split()))

    cop = [[100]*m]*n

    for j in xrange(len(cop)):
        m = max(lawn[j])
        cop[j] = map(lambda b: min(m, b), cop[j])

    for j in xrange(len(cop[0])):
        m = max([ p[j] for p in lawn ])
        for y in xrange(len(cop)):
            if cop[y][j] > m: cop[y][j] = m
        
    if cop == lawn:
        out.write('Case #' + str(i) + ': YES\n')
    else:
        out.write('Case #' + str(i) + ': NO\n')
    


