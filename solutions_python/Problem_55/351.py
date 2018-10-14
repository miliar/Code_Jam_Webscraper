import sys
from itertools import *
DEBUG=False
def ints(line):
    return map(lambda x: int(x.strip()), line.strip().split(' '))

def log(*args):
    if DEBUG:
        print " ".join(map(str, args))
        
def naive_solve(R, k, N , groups, case_no):
    """
    R - rides, 
    k - capcity, 
    N - length of g
    """
    print "Solving: #%s" % case_no
    total = 0
    for r in xrange(R):
        c = 0
        for i in xrange(N):
            if ((c + groups[0]) <= k):
                g = groups.pop(0)
                c += g
                groups.append(g)
            else:
                break;
        total += c
    return total

def naive2_solve(R, k, N , groups, case_no):
    """ detect cycles
    R - rides, 
    k - capcity, 
    N - length of g
    """
    def calc(idx):
        c = 0 
        for i in xrange(N):
            if ((c + groups[idx]) <= k):
                c += groups[idx]
                log(groups[idx])
                idx = (idx + 1) % N
            else:
                break;
        log(" --> ", idx, c)
        return c, idx
        
    print "Solving: #%s" % case_no
    total = 0
    idx = 0
    r = 0
    idxs = {}
    totals = []
    while (r < R):
        if idx not in idxs:
            idxs[idx] = r
            c, idx = calc(idx)
            total += c
            totals.append(total)
        else:
            log("cycle after: %s, N=%s" % (r, N), idx)
            prev_r = idxs[idx]
            mod = (r - prev_r)
            R = R - prev_r

            total_offset = totals[prev_r-1] if prev_r >= 1 else 0
            log("total_offset", total_offset)
            m = R / mod 
            total += (m-1) * (total - total_offset)

            rem = (R % mod) 
            total += (totals[prev_r+rem-1] - total_offset) if rem >= 1 else 0
            break;
        r += 1
    return total        

fn = sys.argv[1]
input = iter(open(fn, 'r'))
output = open(fn.replace('.in', '.out'), 'w')

T = int(input.next().strip())

for case_no in range(T):
    l1 = input.next()
    l2 = input.next()
    log(l1,l2,)

    R, k, N = ints(l1)
    groups = ints(l2)
    solution = naive2_solve(R, k, N , groups, case_no)
    if DEBUG:
        solution_chk = naive_solve(R, k, N , list(groups), case_no)
        log(solution, solution_chk)
        assert solution == solution_chk 
    print >>output, "Case #%d: %s"  % (case_no+1, solution)