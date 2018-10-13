#!/usr/bin/env python

import sys
import re

lines = sys.stdin.readlines()
lines = lines[1:]
i =0
for line in lines:
    i += 1
    ret = ""
    d = {}

    m = re.match(r"\d+ ([A-Z]*) ?\d+ ([A-Z]*) ?\d+ ([A-Z]+)", line)
    (tr, rp, st) = m.groups()

    if len(tr) > 0:
        tr1 = tr[0] + tr[1]
        tr2 = tr[1] + tr[0]
    else:
        tr1=""
        tr2=""

    s = set()
    while st:
        ret += st[0]
        s.add(st[0])
        st = st[1:]
        
        if len(ret) > 1:
            if ret[-2:] == tr1 or ret[-2:] == tr2:
                ret = ret[:-2] + tr[2]
                s = set([c for c in ret])
                continue

        if rp:
            if rp[0] in s and rp[1] in s:
                ret = ""
                s = set()

    print >>sys.stdout, "Case #%d: [%s]" % (i,", ".join(ret))

