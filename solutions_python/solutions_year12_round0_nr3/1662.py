#!/usr/bin/env python

import sys

inp = open(sys.argv[1], "r")
out = open("output.txt", "w+")

count = int(inp.next())
for index in range(count):
    result_count = {}
    A, B = map(int, inp.next().split())
    for n in xrange(A, B+1):
        str_n = str(n)
        length = len(str_n)
        for i in xrange(length,0,-1):
            shift_n = int(str_n[i:length]+str_n[0:i])
            if (shift_n >= A) and (shift_n < n):
                for m in xrange(A, n):
                    if shift_n == m:
                        result_count[(shift_n, n)] = 1
    out.writelines("Case #%d: %d\n" % (index+1, len(result_count)))
    
inp.close()
out.close()