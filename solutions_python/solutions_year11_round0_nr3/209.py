#/usr/bin/env python

import sys
import math
from operator import xor


DEBUG = False
def debug(string):
    if DEBUG:
        print string


in_file = sys.argv[1]
fp = open(in_file)
for case in range (1, int(fp.readline())+1):
    # Init
    debug("Case %s: " % (case))
    candies_num = int(fp.readline())
    string_candies = fp.readline().split()
    candies = []
    for candy in string_candies:
        candies.append(int(candy))
    debug("%s candies -> %s" % (candies_num, candies))
    # Body
    xor_all = 0
    for candy in candies:
        xor_all = xor(xor_all, candy)
    sean = 0
    if xor_all != 0:
        sean = "NO"
    else:
        patrick = min(candies)
        candies.remove(patrick)
        for candy in candies:
            sean += candy
        
    # Finish
    print "Case #%s: %s" % (str(case), sean)
    debug("")