

def solve(distance, horses):

    horses.sort(reverse=True)
    times = []
    for start, speed in horses:
        time_taken = (distance - start) / float(speed)
        times.append((time_taken, speed))
    s = 0
    slowest_speed = -1
    for time_taken, speed in times:
        if time_taken > s:
            # This is the slowest horse
            slowest_speed = time_taken
        s += time_taken

    return distance / float(slowest_speed)


for case in xrange(input()):
    distance, num_horses = map(int, raw_input().split(' '))
    horses = []
    for n in xrange(num_horses):
        horses.append(map(int, raw_input().split(' ')))
    print "Case #%d: %f" % (case + 1, solve(distance, horses))











