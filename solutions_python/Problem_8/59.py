import os
import sys
import psyco

def factor(x):
    str_factors = os.popen("factor "+str(x)).readline().split()[1:]
    return set([long(x) for x in str_factors])

def group_range(A,B,m):
    # Mapping from prime factors to the relevant sets of prime-factors.
    groups = {}
    x = A
    cleared_groups = []
    while x  <= B:
        primes = factor(x)
        primes = [y for y in primes if y >= m]
        if len(primes) == 0:
            groups[x] = set([x])
            cleared_groups.append(groups[x])
        my_group = set()
        for p in primes:
            my_group.add(p)
            if p in groups:
                my_group = my_group.union(groups[p])                
                for k in my_group:
                    groups[k] = my_group
            groups[p] = my_group
        x += 1

    clear_groups = 0
    used_factors = set()
    for p in groups:
        if p in used_factors:
            continue
        used_factors = used_factors.union(groups[p])
        clear_groups += 1
    
    return clear_groups

psyco.full()


lines = open(sys.argv[1]).readlines()
num_cases = int(lines[0])
lines = lines[1:]
assert(len(lines) == num_cases)
for i,l in enumerate(lines):
    A,B,m = [long(x) for x in l.split()]
    print "Case #%d: %d" % (i+1,group_range(A,B,m))

        

