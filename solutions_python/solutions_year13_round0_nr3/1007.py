import math


def is_pal(x):
    s = str(x)
    return s == s[::-1]

def solve(a, b):
    # import pdb; pdb.set_trace()
    n = 0
    for x in xrange(a,b+1):
        z = int(math.sqrt(x))
        if z * z != x:
            continue
        if is_pal(x) and is_pal(z):
            # print x,z
            n += 1 
    return n

def solve2(a, b):
    # import pdb; pdb.set_trace()
    n = 0
    la = int(math.sqrt(a))
    lb = int(math.sqrt(b))+1
    for z in xrange(la,lb+1):
        if any(x for x in str(z) if int(x)>3) or not is_pal(z):
            continue
        if z*z <= b and z*z>=a and is_pal(z * z):
            # print z*z, z
            n += 1 
    return n

if __name__ == '__main__':
    import sys
    l = [x.strip() for x in open(sys.argv[1]).readlines()[1:] if x.strip()]
    for i, t in enumerate(l):
        a, b = map(int, t.split())
        n = solve(a, b)
        print "Case #%s: %s" % (i+1, n)
        cor = solve2(a, b)
        if n != cor:
            print "Problem: %s, %s, got %s, need %s" % (a,b,n,cor)
