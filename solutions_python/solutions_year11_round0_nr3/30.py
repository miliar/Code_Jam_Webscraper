import sys

infile = sys.stdin

T = int(infile.readline())
for i in xrange(T):
    infile.readline() # ignore length
    values = list(map(int, infile.readline().split()))
    xor = reduce(lambda a,b: a^b, values)
    if xor==0:
        result = sum(values) - min(values)
    else:
        result = 'NO'
    print("Case #%d: %s" % (i+1, result))