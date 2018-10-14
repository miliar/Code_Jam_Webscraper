# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    dis, num_horse = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    horses = []
    for j in range(num_horse):
        loc, speed = [float(s) for s in raw_input().split(" ")]
        horses.append({"loc":loc, "speed":speed})

    max_time = 0.0
    for horse in horses:
        time = (float(dis) - horse["loc"]) / horse["speed"]
        if time > max_time:
            max_time = time

    ret = float(dis) / float(max_time)
    print "Case #{}: {}".format(i, ret)


