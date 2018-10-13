# Timothy Courrejou
# GCJ2011 - QC

import itertools

def xor_list(l):
    r = 0
    for le in l:
        r ^= le
    return r

def get_max(candy):
    candy.sort()
    if xor_list(candy) != 0:
        return "NO"

    for i in range(1, len(candy)):
        for j in range(1, i+1):
            for k in itertools.combinations(candy[0:i], j):
                for l in k:
                    candy.remove(l)
                return sum(candy)

    return "NO"

f = open("C-large.in", "r")
T = int(f.readline())

for i in range(0,T):
    N = int(f.readline())
    vals = []
    for val in f.readline().split():
        vals.append(int(val))

    print "Case #" + str(i+1) + ":",
    print get_max(vals)

f.close()
