#!/usr/bin/env python

import os, sys, fileinput, re

def on(n, k):
    n, k = int(n)-1, int(k)
    while (n and k&1): n, k = n-1, k>>1
    return k&1

case, cases = 0, fileinput.input()
for line in fileinput.input():
    m = re.match("(?P<n>\d+)\s+(?P<k>\d+)\s*", line)
    if m:
        case += 1
        print("Case #%d: %s" % (case, "ON" if on(**m.groupdict()) else "OFF"))