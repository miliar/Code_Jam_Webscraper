from sys import stdin

T = int(stdin.readline())
for t in xrange(0, T):
    N = int(stdin.readline())
    line = [int(x) for x in stdin.readline().split(' ')]
    xorsum = 0 
    for x in line:
        xorsum = xorsum ^ x
    if (xorsum != 0):
        print 'Case #' + str(t + 1) + ': NO'
    else:
        print 'Case #' + str(t + 1) + ': ' + str(sum(line) - min(line))

