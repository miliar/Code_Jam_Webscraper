#!/usr/bin/env python
import sys

def algorithm(line):
    list = [int(x) for x in line.split()]
    bin_sum = reduce(lambda x,y: x^y, list)    
    if (bin_sum > 0):
        return 'NO'
    else:
        list.remove(min(list))
        return str(reduce(lambda x,y: x+y, list))



fin = open(sys.argv[1])
fout = open(sys.argv[2],'w')
n = fin.readline()
case_n = 0
while fin.readline():
    case_n += 1
    line  = fin.readline()
    algorithm(line)
    fout.write('Case #%d: %s\n' % (case_n, algorithm(line)))