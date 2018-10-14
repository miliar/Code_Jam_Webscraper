infile = open('goro.in')
outfile = open('goro.out', 'w')

T = int(infile.readline().strip())

for i in xrange(T):
    N = int(infile.readline().strip())
    starting = infile.readline().strip().split()
    distinct_count = 0
    for j in xrange(N):
        if int(starting[j]) != j + 1:
            distinct_count += 1
    answer = (float(distinct_count) if distinct_count >= 2 else 0.0)
    outfile.write('Case #%d: %f\n' % (i + 1, answer))

