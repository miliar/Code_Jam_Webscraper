import sys
import string

filename = sys.argv[1]
f = open(filename, "r")
lines = map(string.strip, f.readlines())
T = int(lines[0])


for t in range(T):
    line = lines[t + 1]
    smax, shyness = line.split()
    smax = int(smax)

    total = 0
    min_guest = 0
    # if t + 1 == 7:
    #     import pudb; pudb.set_trace()
    for i, c in enumerate(shyness):
        if total < i:
            added_guests = i - total
            total += int(c) + added_guests
            min_guest += added_guests
        else:
            total += int(c)

    print "Case #%s: %s" % (t + 1, min_guest)
