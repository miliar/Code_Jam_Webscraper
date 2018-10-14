import sys, fractions

def lcm(a, b):
    return (a*b)/(fractions.gcd(a, b))

def is_valid(n, pd, pg):
    if pd > 0 and pg == 0:
        return False
    if pd == 100:
        return True
    if pg == 100 and pd < 100:
        return False
    if pd == 0:
        return True
    if lcm(pd, 100)/pd <= n:
        return True
    return False    

def solve(l, casen):
    res = False
    n, pd, pg = map(int, l.split(' '))
    valid = is_valid(n, pd, pg)
    print "Case #%d: %s" % (casen, 'Possible' if valid else 'Broken')

if __name__ == '__main__':
    with open(sys.argv[1], 'rU') as f:
        lines = f.readlines()
        ncases = int(lines[0])
        lines = lines[1:]
        for i in xrange(ncases):
            solve(lines[i].strip(), i+1)
