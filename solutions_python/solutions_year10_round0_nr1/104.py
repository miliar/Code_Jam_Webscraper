import sys
stream = open(sys.argv[1])

T = int(stream.readline())

for case in range(T):
    N, K = [int(x) for x in stream.readline().split()]
    state = (K+1) % 2**N == 0
    print "Case #%d: %s" % (case+1, "ON" if state else "OFF")
