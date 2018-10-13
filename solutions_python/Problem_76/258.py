import sys, operator

file_prefix = sys.argv[1]
with open(file_prefix + '.in', 'r') as f_in:
    t = int(f_in.readline())
    with open(file_prefix + '.out', 'w') as f_out: 
        for i in xrange(t):
            f_in.readline()
            x = map(int, f_in.readline().split(' '))
            sx = sum(x)
            if reduce(operator.xor, x) == 0:
                r, z = 0, None
                for j in xrange(len(x)):
                    if x[j] == reduce(operator.xor, x[:j] + x[j+1:]) and sx - x[j] > r:
                        r = sx - x[j]
            else:
                r = 'NO'
            f_out.write('Case #%s: %s\n' % (i + 1, r))
