import sets
import itertools

def xorsum(l):
    if len(l) == 0: return
    if len(l) == 1: return l[0]
    else:
        res = l[0]

        for i in xrange(1, len(l)):
            res ^= l[i]

        return res

def all_combinations(l):
    ret = []

    for n in range(1, len(l)):
        for comb in itertools.combinations(l, n):
            ret.append(comb)
    return ret
    

def algo(c):
    m = 0

    c = [int(x) for x in c]
    cs = sets.Set(c)

    p = all_combinations(c)

    for i in p:
        cr = c[:]
        [cr.remove(y) for y in i]

        if xorsum(i) == xorsum(cr) and len(i) > 0 and len(cr) > 0:
            ss = sum(i)
            if ss > m: m = ss


    if m == 0: return "NO"
    else: return m


f = open("b.in", "r")
content = f.readlines()

T =  int(content[0])

for i in xrange(2, 2*T+1, 2):
    candies = content[i].rstrip("\n").split(" ")

    print "Case #{0}: {1}".format(i/2, algo(candies))