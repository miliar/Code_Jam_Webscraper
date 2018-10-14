from itertools import *
import math
import string
from collections import defaultdict


def main2():
    fpath = 'A-small-attempt0.in'
    with open(fpath, 'r') as f, open(fpath + '.out', 'w') as fout:
        cases = int(f.readline().replace('\n',''))
        c = 1
        for line in f:
            
            line = line.replace('\n','')
            items = line.split(' ')
            r_init = float(items[0])
            area_remain = float(items[1]) * math.pi
            #how many can we draw?
            rings = 0
            #print 'r:',r_init,'t',paint_remaining

            while area_remain > 0:
                area_remain -= (((2.0 * r_init) + 1))
                rings += 1
                r_init += 2.0
            
            fout.write('Case #' + str(c) + ': ' + str(rings-1) + '\n')
            c += 1

main2()
