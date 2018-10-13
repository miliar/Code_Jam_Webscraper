#!/usr/bin/env python

def replace(s, n, c):
    new = s[0:n] + c + s[n+1:]
#    print "replacing %s with %s; n=%s, c=%s" % (s, new, n, c)
    return new

def decrement(c):
    return chr(ord(c) - 1)

def decrement_in_place(s, n):
    return s[:n] + decrement(s[n]) + s[n+1:]

def make9s(s, n):
    return s[:n] + (len(s) - n) * '9'

t = int(raw_input())
for i in xrange(1, t + 1):
    n, = [s for s in raw_input().split(" ")]
    inflection_point = -1
    repeat_index = 0
    repeat_value = -1
    for j in xrange(len(n)):
#        print j, 'a', n
        if j+1 < len(n):
            if n[j] == n[j+1]:
                if n[j] != repeat_value:
                    repeat_index = j
                    repeat_value = n[j]
            elif int(n[j]) > int(n[j+1]):
#                print n[j], n[j+1], j
                n = decrement_in_place(n, repeat_index)
                n = make9s(n, repeat_index+1)
            else:
                repeat_index = j+1
                repeat_value = n[j+1]

    print "Case #{}: {}".format(i, int(n))
