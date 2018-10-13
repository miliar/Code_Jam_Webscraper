""" 
    
"""

from sets import Set
import sys

__author__ = 'Jorge Santos'
__version__ = '$Id$'

f = open(sys.argv[1])

nCases = int(f.readline())
engines = {}

for nCase in range(nCases):
    res = 0
    nEngines = int(f.readline())
    engines = Set()
    for nEngine in range(nEngines):
	engines.add(f.readline())
    free = engines.copy()
    nQueries = int(f.readline())
    for nQuery in range(nQueries):
# 	print "BEFORE:"
#  	print "len(free): %s" % len(free)
#  	print "nQuery: %s" % nQuery
	query = f.readline()
	free.discard(query)
	if len(free) == 0:
	    res += 1
	    free = engines.copy()
	    free.discard(query)
# 	print "AFTER:"
#  	print "len(free): %s" % len(free)
#  	print "nQuery: %s" % nQuery
    print "Case #%s: %s" % (nCase+1, res)
