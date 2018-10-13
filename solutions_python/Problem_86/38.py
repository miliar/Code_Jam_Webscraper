from itertools import combinations

def parse(f):
    rows = [r.strip().split(' ') for r in open(f).read().split('\n') if r]
    num_tests = int(rows.pop(0)[0])
    case = 1
    for i in xrange(num_tests):
        r = map(int,rows.pop(0))
        N = r[0]
        L = r[1]
        H = r[2]
        frequencies = map(int,rows.pop(0))
        solve(N,L,H,frequencies,case)
        case += 1

def solve(N,L,H,frequencies,case):
    result = 'NO'
    for i in xrange(L,H+1):
        test = frequencies + [i]
        if all((i % f == 0 or f % i == 0) for f in frequencies):
            result = i
            break
    print 'Case #%d: %s' % (case, result)


f = 'C-small-attempt0.in'
parse(f)
