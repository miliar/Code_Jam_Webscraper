#!/usr/bin/python

def happy(s):
    return s == "+"

def flip(s):
    if (happy(s)):
        return "-"
    else:
        return "+"

def turn(cakes, pos, k):
    ret = cakes[:pos]
    for i in xrange(k):
        ret += flip(cakes[i + pos])
    ret += cakes[pos + k:]
    return ret

def algo(cakes, k):
    turns = 0
    for i in xrange(len(cakes)):
        if (not happy(cakes[i])):
            if (len(cakes) - i < k):
                return "IMPOSSIBLE"
            else:
                cakes = turn(cakes, i, k)
                turns += 1
    return turns

for i in xrange(int(raw_input())):
    (cakes, k) = raw_input().split()
    print "Case #" + str(i + 1) + ": " + str(algo(cakes, int(k)))
