from operator import xor
import sys

it = iter(sys.stdin.readlines())
it.next()
index = 1
while(True):
    try:
        it.next()
    except StopIteration:
        break
    values = map(int, it.next().split())
    
    if reduce(xor, values):
        print "Case #%s: NO" % index
    else:
        print "Case #%s: %s" % (index, sum(values) - min(values))
    index += 1
