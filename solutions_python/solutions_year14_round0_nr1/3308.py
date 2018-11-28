import sys

import sys
from collections import defaultdict

def read_int():
    return int(raw_input())

def read_line():
    return sys.stdin.readline().rstrip("\n")

def read_int_line(num):
    l = [int(x) for x in read_line().split()]
    assert len(l) == 4
    return l

def read_table():
    return [read_int_line(4),
            read_int_line(4),
            read_int_line(4),
            read_int_line(4)]

ncases = read_int()

for case in xrange(ncases):
    a1 = read_int() - 1
    t1 = read_table()
    a2 = read_int() - 1
    t2 = read_table()
    i = list(set(t1[a1]) & set(t2[a2]))
    if len(i) == 1:
        print "Case #{}: {}".format(case + 1, i[0])
    elif len(i) > 1:
        print "Case #{}: Bad magician!".format(case + 1)
    else:
        print "Case #{}: Volunteer cheated!".format(case + 1)

# Case #1: 7
# Case #2: Bad magician!
# Case #3: Volunteer cheated!
