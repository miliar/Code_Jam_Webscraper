#/usr/bin/env python

import sys

DEBUG = False
def debug(string):
    if DEBUG:
        print string


in_file = sys.argv[1]
fp = open(in_file)
for case in range (1, int(fp.readline())+1):
    debug("Case %s: " % (case))
    line = fp.readline().split()
    N = int(line[0])
    Pd = int(line[1])
    Pg = int(line[2])
    debug("N=%i, Pd=%i, Pg=%i" % (N, Pd, Pg))
    
    if Pd == 0 and Pg == 100:
        result = "Broken"
    elif Pd == 100 and Pg == 0:
        result = "Broken"
    elif Pg == 0 and Pd > 0:
        result = "Broken"
    elif Pg == 100 and Pd < 100:
        result = "Broken"
    else:
        result = "Broken"
        for i in xrange(N, 0, -1):
            debug("%i * %i" % (i, Pd))
            if (i * Pd % 100) == 0:
                result = "Possible"
                break

    print "Case #%s: %s" % (str(case), result)
    debug("")