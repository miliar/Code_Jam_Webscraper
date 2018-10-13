T = int(raw_input())
for i in xrange(1,T+1):
    line = raw_input().split()
    N = int(line[0])
    K = int(line[1])
    ring = 2**N
    K %= ring
    if K == ring -1:
        print "Case #" + str(i)+ ": ON"
    else:
        print "Case #" + str(i)+ ": OFF"
