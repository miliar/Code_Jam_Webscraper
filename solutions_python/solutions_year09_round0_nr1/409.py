
import sys
import re

input = open(sys.argv[1])
L, D, N = input.readline().strip().split(' ')

words = [input.readline().strip() for x in xrange(int(D))]

for i in xrange(1, int(N)+1):
    test = input.readline().strip().replace('(','[').replace(')',']')
    testMatch = re.compile(test)

    print "Case #%s: %s" % (i, len(filter(None, [testMatch.match(word) for word in words])))


