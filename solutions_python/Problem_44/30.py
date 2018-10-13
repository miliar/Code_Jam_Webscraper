import sys
import math
from itertools import izip

def memoize(func):
    results = {}
    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return wrapper

def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return [uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx]

def scalar(u, v):
    return sum(u[i]*v[i] for i in xrange(3))

def vlen(v):
    return math.sqrt(sum(e * e for e in v))

def closest(swarm):
    sums = [0, 0, 0, 0, 0, 0]
    for fly in swarm:
        for i in xrange(6):
            sums[i] += fly[i]
    m0 = sums[:3]
    sv = sums[3:]
    sys.stderr.write('m0 %s\n' % (m0))
    sys.stderr.write('sv %s\n' % (sv))

    if vlen(sv) == 0.0:
        t = 0.0
	d = vlen(m0) / len(swarm)
    else:
        x1 = [-m0[i] for i in xrange(3)]
        x2 = [-(m0[i] + sv[i]) for i in xrange(3)]
        sys.stderr.write('%s %s\n' % (x1, x2))
        c = cross(x1, x2)
        sys.stderr.write('c: %s\n' % c)
        lc = vlen(c)
        sys.stderr.write('lc: %s\n' % lc)
        lv = vlen(sv)
        sys.stderr.write('lv: %s\n' % lv)
        d = lc / lv / len(swarm)
        sys.stderr.write('d: %s\n' % d)
        t = -scalar(m0, sv) / (vlen(sv)*vlen(sv))
        if t < 0.0:
            t = 0.0
	    d = vlen(m0) / len(swarm)
    
    return "%.8f %.8f" % (d, t)

def do_one_test_case(file):
    N = int(file.readline())
    swarm = [[int(n) for n in file.readline().split()] for _ in xrange(N)]
    #s = file.readline().strip()
    #bases = list(int(b) for b in s.split())
    #bases.reverse() # Larger bases reduce faster (?)
    return closest(swarm)

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline().strip())
    sys.stderr.write('Cases: %d\n' % cases)
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d: %s\n' % (i+1, do_one_test_case(f)))
        sys.stderr.write('%d of %d done\n' % (i+1, cases))
    f.close()
    if len(argv) > 2:
        expected_f = open(argv[2], 'r')
        expected_list = expected_f.readlines()
        expected_list = [line.strip()+'\n' for line in expected_list[0:-1]]
        if (output_list == expected_list):
            print 'Everything matched!'
        else:
            print 'Actual: %s' % output_list
            print 'Expected: %s' % expected_list
    else:
        print ''.join(output_list)

def test():
    print 'Usage: scriptname.py infile [outfile]'
    print 'I\'ll run the doctests instead!'
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        test()
    else:
        main(sys.argv)
