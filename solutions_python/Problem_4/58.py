import sys

def scalar_product(v1, v2):
    ret = 0
    for i in range(len(v1)):
        ret += v1[i]*v2[i]

    return ret

def all_perms(v):
    if len(v) <= 1:
        yield v
    else:
        for perm in all_perms(v[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + v[0:1] + perm[i:]

def solve(v1, v2):
    v1.sort()
    v2.sort(reverse=True)
    return scalar_product(v1, v2)

def bad():
    first = True
    minimum = 0
    for p1 in all_perms(v1):
        for p2 in all_perms(v2):
            #print p1, p2
            sp = scalar_product(p1, p2)
            if first or sp < minimum:
                minimum = sp
                first = False
    return minimum

if __name__ == '__main__':
    if (len(sys.argv)) != 2:
        print "usage: %s [inputfile]" % sys.argv[0]
        sys.exit(0)

    fin = open(sys.argv[1])

    case_n = int(fin.readline())
    for i in range(case_n):
        n = int(fin.readline())
        v1 = [int(x) for x in fin.readline().strip().replace("\n", "").split()]
        v2 = [int(x) for x in fin.readline().strip().replace("\n", "").split()]
        print "Case #%d: %d" % (i+1, solve(v1, v2))


