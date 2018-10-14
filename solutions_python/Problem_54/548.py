import sys
import os
import operator
import fractions

def warning(list_map):
    listmap = []
    for iterator in range(1, len(list_map)):
        listmap.append(operator.abs(list_map[iterator] - list_map[iterator-1]))
    if len(listmap) == 1:
       rec_gcd = listmap[0]
    else:
       rec_gcd = reduce(lambda x,y: fractions.gcd(x,y), listmap)
    term = min(list_map)
    if term % rec_gcd == 0 :
	retval = 0
    elif term <= rec_gcd:
       retval = rec_gcd - term
    else :
       retval = (rec_gcd - (term % rec_gcd))
    return retval

def input():
    testcases = int( raw_input())
    for i in xrange(0, testcases) :
	val = raw_input()
        inp = map(int,val.split())
        list_map = inp[1:]
        date  = warning(list_map)
        print "Case #%d: %s" %(i+1, date)

if __name__=="__main__":    
    input()


