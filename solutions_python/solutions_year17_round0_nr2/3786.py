#!/usr/bin/env python2
def untidy_pos(numstr):
    for idx, dig in enumerate(numstr[1:]):
        idx +=1
        last_dig = numstr[idx-1]
        if int(dig) < int(last_dig):
            return idx -1
    return -1

def tidy(numstr, pos):
    prefix = int(numstr[:pos+1])
    prefix -= 1
    prefix = str(prefix)
    return prefix.lstrip("0") + ("9" * (len(numstr)-pos-1))


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = raw_input()
    while -1 != untidy_pos(n):
        n = tidy(n, untidy_pos(n))
    print "Case #{}: {}".format(i, n)
    # check out .format's specification for more formatting optionsa
