#!/usr/bin/python

def nb_recycled_pairs(line):
    nb1, nb2 = [int(x) for x in line.split(" ")]
    
    total = 0
    length = len(str(nb1))
    n = nb1
    while n < nb2:
        all_m = []
        for i in xrange(length):
            m = int("".join([str(n)[i:], str(n)[:i]]))
            if n >= m or m > nb2 or m in all_m:
                continue
            total += 1
            all_m.append(m)
        n += 1

    return total

with open('C-large.in') as f:
    nb_tests = int(f.readline())
    i = 1
    for line in f.readlines():
        print "Case #%d: %d" % (i, nb_recycled_pairs(line))
        i += 1

