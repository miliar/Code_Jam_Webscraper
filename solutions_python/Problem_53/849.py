#!/usr/bin/env python
# -*- coding: utf-8 -*-

ts = raw_input()
for t in range(1, int(ts)+1):
    (n, k) = [int(r) for r in raw_input().split(' ')]
    print "Case #%i: %s"  % (t, "OFF" if (k+1)%(2**n) else "ON")
