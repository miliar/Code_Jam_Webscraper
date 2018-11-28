#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,string

table = string.maketrans("ejp mysljylc kd kxveddknmc re jsicpdrysi"
                         "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
                         "de kr kd eoya kw aej tysr re ujdr lkgc jv"
                         "yeqz",
                         "our language is impossible to understand"
                         "there are twenty six factorial possibilities"
                         "so it is okay if you want to just give up"
                         "aozq")

def run(line):
    return line.translate(table)
    
if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        if fname != "-":
            f = open(fname)
    N = int(f.readline())
    for _num in xrange(N):
        line = f.readline().strip()
        ret = run(line)
        print "Case #%d: %s" % (_num+1, ret)
