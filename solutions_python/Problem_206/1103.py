t = int(raw_input())
for i in xrange(1, t + 1):
    d, h = raw_input().split(" ")
    horses = {}
    for j in xrange(1, int(h) +1):
        horses[j] = raw_input().split(" ")

    max_left = 0
    for id, horse in horses.iteritems():
        left = (float(d) - float(horse[0])) / float(horse[1])
        # print left
        if left > max_left:
            max_left = left
            # print "Found"

    # print left
    a = float(d) / max_left
    print "Case #{}:".format(i),
    print "%.6f" % a
