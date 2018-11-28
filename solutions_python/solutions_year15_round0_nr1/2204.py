from sys import argv

f = open(argv[1], 'r')

T = f.readline().rstrip()

for t, l in enumerate(f):
    shyness = l.rstrip().split(' ')[1]
    stand = invited = 0
    for level, audience in enumerate(shyness):
        while stand < level:
            invited += 1
            stand   += 1
        stand += int(audience)
    print "Case #%d: %d" % (t+1, invited)
