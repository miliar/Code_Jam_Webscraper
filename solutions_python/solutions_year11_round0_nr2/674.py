#!/usr/bin/env python
import sys
import os
import math
with open(sys.argv[1], "r") as input:
    data = input.readlines()
with open("%s.result" % sys.argv[1], "w") as output:
    n = int(data[0])
    for i in range(n):
        string = data[i+1][:-1].split()
        clist = {}
        olist = set() 
        clen = int(string[0])
        olen = int(string[clen + 1])
        ctemp = string[1:clen + 1]
        otemp = string[clen + 2:clen + olen + 2]
        orig = ''.join(string[clen + olen + 3:])
        for v in ctemp:
            key = ''.join(sorted(v[0:2]))
            clist[key] = v[2]
        for v in otemp:
            olist.add(''.join(sorted(v)))
        res = "" 
        for v in orig:
            res += v
            key = ''.join(sorted(res[-2:]))
            if clist.has_key(key):
                res = res[:-2]
                res += clist[key]
                continue
            for k in range(len(res)):
                key = ''.join(sorted([res[k], res[-1]]))
                if key in olist:
                    res = "" 
                    break
        print>> output,  "Case #%d: [%s]" % (i + 1, ', '.join(res))
        print "Case #%d: [%s]" % (i + 1, ', '.join(res))
