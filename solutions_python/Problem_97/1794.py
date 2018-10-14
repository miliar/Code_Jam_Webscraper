def spins(s):
    for i in xrange(len(s)):
        yield s[i:] + s[:i]

def recycled_pairs(n, B):
    used = set()
    nstr = str(n)
    for mstr in spins(nstr):
        m = int(mstr)
        if m > n and m <= B:
            used.add((n, m))
    return len(used)

def solve(A, B):
    count = 0
    for n in xrange(A, B):
        count += recycled_pairs(n, B)
    return count

T = int(raw_input())
for t in xrange(1, T+1):
    line = raw_input()
    A, B = (int(w) for w in line.split())
    solution = solve(A, B)
        
    print "Case #%d: %d" % (t, solution)
