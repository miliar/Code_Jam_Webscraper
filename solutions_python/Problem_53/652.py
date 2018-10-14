#
def int2bin(n, count=30):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

for case in xrange(input()):
    N, K = [int(x) for x in raw_input().split() ]
    #print "%d %d" % (N, K)
    #print int2bin(K)
    s = int2bin(K)[30-N:30]
    sum = reduce( lambda x, y: int(x)+int(y), s, 0 )
    if sum == N:
        print "Case #%d: ON" % (case+1)
    else:
        print "Case #%d: OFF" % (case+1)
