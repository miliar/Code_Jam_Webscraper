#!/usr/bin/env python

import sys
import bisect

def is_lookup(i):
    idx = bisect.bisect_left(lookup_table, i)
    if(idx >= lookup_table_len):
        return False
    if(lookup_table[idx] == i):
        return True
    return False

def lookup(i):
    idx = bisect.bisect_left(lookup_table, i)
    if(idx >= lookup_table_len):
        return (False, 0)
    if(lookup_table[idx] == i):
        return (True, idx)
    return (False, idx)


lookup_table = []

ftable = open('data/C-large.table', 'r')
for line in ftable:
    lookup_table.append(int(line.rstrip()))
ftable.close()
lookup_table.sort()
lookup_table_len = len(lookup_table)
print lookup_table

f = open('/home/zinuzoid/Downloads/C-large-1.in', 'r')
fout = open('/home/zinuzoid/Downloads/c.out', 'w')
cases =  int(f.readline())
for case in range(cases):
    raw = f.readline().split()
    cstart = int(raw[0])
    cstop = int(raw[1])
    count = 0
    
#    i=cstart
#    while i <= cstop:
#        if(is_lookup(i)):
#            count += 1
#            print i
#        i += 1
        
    for i in lookup_table:
        if(cstart <= i and i <= cstop):
            count += 1
            #print i
        
#    for i in range(cstart, cstop + 1):
#        if(is_lookup(i)):
#            count += 1
#            print i
            
    s = 'Case #' + str(case + 1) + ': ' + str(count)
    print s
    fout.write(s + '\n')
    
fout.close()
f.close()

