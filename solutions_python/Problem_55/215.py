import sys
import fractions

num_cases = int(sys.stdin.readline())

lines = sys.stdin.readlines()

if (2*num_cases) != len(lines):
    raise Exception("num of cases don't match");

def get_revenue(r, k, n, g):
    
    jumps = [None] * n
    for i in xrange(n):
        ride_total = 0
        for j in xrange(n):
            if (ride_total + g[(i+j) % n] > k):
                break
            ride_total += g[(i+j) % n]
        jumps[i] = (ride_total, (i+j) % n)
    
    total_revenue = 0
    mark = 0
    for _ in xrange(r):
        ride_total, jump = jumps[mark]
        total_revenue += ride_total
        mark = jump
    
    return total_revenue

for i in xrange(num_cases):
    r, k, n = [int(e) for e in lines[2*i].split()]
    g = [int(e) for e in lines[2*i+1].split()]
    
    if n != len(g):
        raise Exception("num of g's don't match");
    
    print "Case #%s: %s" % (i+1, get_revenue(r, k, n, g))
    i += 1
