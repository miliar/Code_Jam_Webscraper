#!/usr/bin/env python
'''
      
'''

import sys
from pprint import pprint
import string


gibr = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
tran = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"


d = {} 
def create_mapping():
    for i in string.lowercase:
        if i in ['z','q']: continue
        if i not in gibr:
            print i, "screwup"
            sys.exit()
        assert i not in d 
        #print "gibr char:", i, "tran char index:",  tran.index(i), "gibr char:", gibr[tran.index(i)]
        d[i] = gibr[tran.index(i)]
    d['q'] = 'z'
    d['z'] = 'q'
    d[' '] = ' '
    for i in string.lowercase:
        if i not in d.values(): print "Yo, you missed", i
    global m
    m = string.maketrans("".join([d[i] for i in string.lowercase]), string.lowercase)

    #print d
           
def do_one_case(csn, l):
    print "Case #"+str(csn)+":", l.translate(m) 

def main():
    create_mapping()
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        l = sys.stdin.readline().strip()
        #print W,H,T
        do_one_case(i+1, l)


if __name__ == "__main__":
    main()
