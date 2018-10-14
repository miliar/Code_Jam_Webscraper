filename = 'A-large'
input = open(filename + '.in',  'r')
output = open(filename + '.out',  'w')
cases = int(input.readline().rstrip())
for i in xrange(1, cases+1 ):
    P, K, L = [int(x) for x in input.readline().rstrip().split(' ')]
    freq = [int(x) for x in input.readline().rstrip().split(' ')]
    if L > P*K:
        output.write('Case #' + str(i) + ': Impossible')
    else:
        freq = [x for x in reversed(sorted(freq))]
        ret = 0
        for x in xrange(len(freq)):
            place = x/K+1
            ret += place*freq[x]
    output.write('Case #' + str(i) + ': ' + str(ret) + '\n')
input.close()
output.close()
