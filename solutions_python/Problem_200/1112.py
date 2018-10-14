#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    s = raw_input()
    for i in xrange(len(s)-1, 0, -1):
        if s[i] < s[i-1]:
            for j in xrange(i-1, -1, -1):
                if s[j] > 0:
                    s = s[:j] + str(int(s[j])-1) + '9'*(len(s)-j-1)
                    break
    print s if s[0] != '0' else s[1:]

