# from optparse import OptionParser

# parser = OptionParser()
# parser.add_option("-f", "--file", dest="filename",
#                   help="read input from FILE", metavar="FILE")
# (options, args) = parser.parse_args()

import sys
if len(sys.argv) != 2:
    raise Exception, 'bad number of arguments'

filename = sys.argv[1]
f = open(filename)
N = int(f.readline())
for i in xrange(N):
    S = int(f.readline())
    engines = set()
    for j in xrange(S):
        engine = f.readline().rstrip()
#        print "Current engine:", engine
        engines.add(engine)
    Q = int(f.readline())
    counter = 0
    Y = 0
    remaining_engines = engines.copy()
    for j in xrange(Q):
        query = f.readline().rstrip()
#        print "Current query:", query
        remaining_engines.discard(query)
        if len(remaining_engines) == 0:
            Y += 1
            remaining_engines = engines.copy()
            remaining_engines.discard(query)
    print "Case #" + str(i+1) + ": " + str(Y)
