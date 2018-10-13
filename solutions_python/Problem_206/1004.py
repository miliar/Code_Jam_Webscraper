from __future__ import print_function, division

T = int(raw_input())  # read a line with a single integer
for case in xrange(1, T + 1):
    destination, horses = raw_input().split(" ")
    destination = float(destination)
    horses = int(horses)
    times = []
    for i in xrange(horses):
        position_0, speed = raw_input().split(" ")
        position_0 = float(position_0)
        speed = float(speed)
        time = (destination - position_0)/speed
        times.append(time)
    max_time = max(times)
    maxspeed = destination/max_time
    print("Case #{0}: {1:.6f}".format(case, maxspeed))
