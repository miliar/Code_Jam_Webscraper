t = int(raw_input())

for i in xrange(t):
    line = raw_input()
    max_shyness, shyses = line.split()
    max_shyness = int(max_shyness)
    shyses = [int(r) for r in list(shyses)]
    
    standing = shyses[0]
    needed = 0
    for t in xrange(1, 1 + max_shyness):
        # print (standing, shyses[t], t), t - standing,
        if standing < t:
            needed += (t - standing)
            standing += (t - standing)
        standing += shyses[t]

    print "Case #%d: %d" % (i + 1, needed)
