f = open('B-large.in', 'r')
o = open('B-large.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    N = list(f.readline().strip())
    switch_index = 0
    for i in xrange(1, len(N)):
        if N[i] < N[i - 1]:
            N[switch_index] = str(int(N[switch_index]) - 1)
            for j in xrange(switch_index + 1, len(N)):
                N[j] = '9'
        elif N[i] > N[i - 1]:
            switch_index = i
    if N[0] == '0':
        N = N[1:]
    N = ''.join(N)
    s = "Case #%d: %s\n" % (t+1, N)
    o.write(s)
