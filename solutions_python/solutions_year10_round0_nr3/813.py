import sys
import itertools

with file(sys.argv[1]) as f:
    lines = f.readlines()[1:]

for j, i in enumerate(range(0, len(lines), 2)):
    rides, seats = map(int, lines[i].split()[:2])
    groups = map(int, lines[i+1].split())

    grp_len = len(groups)
    grp_iter = itertools.cycle(groups)
    money = 0
    left = 0
    for _ in range(rides):
        curr_ride = 0
        if left > seats:
            continue
        curr_ride += left
        left = 0
        grp_ctr = 0
        while curr_ride < seats and grp_ctr < grp_len:
            n = grp_iter.next()
            if curr_ride + n <= seats:
                curr_ride += n
                grp_ctr += 1
            else:
                left = n
                break
        money += curr_ride
    print "Case #%i: %i" % (j+1, money)
