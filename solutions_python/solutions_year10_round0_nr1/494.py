import sys
T = int(sys.stdin.readline().strip())
remt = T
while remt > 0:
    #print T
    (N, K) = (int(i) for i in sys.stdin.readline().strip().split(' '))
    # if (K + 1) contains all multiples of 2 up to N inclusive
    status = "ON"
    for i in xrange(N + 1):
        if (K + 1) % (2 ** N) != 0:
            status = "OFF"
    print "Case #" + str(T - remt + 1) + ":", status
    remt -= 1
