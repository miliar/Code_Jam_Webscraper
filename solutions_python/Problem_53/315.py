import sys

for i, line in enumerate(sys.stdin.read().splitlines()[1:]):
    nb_snapper, nb_iter = map(int, line.split())
    cycle_size = 2**nb_snapper
    alight = (nb_iter % cycle_size) == cycle_size -1
    result = alight and "ON" or "OFF"
    print "Case #%d: %s" % (i+1, result)
