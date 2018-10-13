# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    m = 'yhesocvxduiglbkrztnwjpfmaq'
    
    tests = int(sys.stdin.readline())
    for test in xrange(1, tests+1):
        line = sys.stdin.readline()
        r = []
        for c in line:
            if c.isalpha():
                r.append(m[int(c, 36)-int('a', 36)])
            elif c == ' ':
                r.append(' ')
        r = ''.join(r)
        print "Case #%d: %s" % (test, r)
