filename = 'A-large'
input = open(filename + '.in',  'r')
output = open(filename + '.out',  'w')
cases = int(input.readline().rstrip())
for i in xrange(1, cases+1 ):
    dim = int(input.readline().rstrip())
    X = [int(x) for x in input.readline().rstrip().split(' ')]
    Y = [int(y) for y in input.readline().rstrip().split(' ')]
    Y = [y for y in reversed(sorted(Y))]
    S = 0
    for d in xrange(dim):
        S += sorted(X)[d]*Y[d]
    output.write('Case #' + str(i) + ': ' + str(S) + '\n')
input.close()
output.close()
print
