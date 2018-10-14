cases = int(raw_input())

for ctr in xrange(cases):
    ss = raw_input().split(" ")
    distance = int(ss[0])
    horses = int(ss[1])
    longest_time = 0.0
    for h in xrange(horses):
        ss = raw_input().split(" ")
        pos = int(ss[0])
        speed = int(ss[1])
        time = (distance - pos) / float(speed)
        if time > longest_time:
            longest_time = time
    answer = float(distance) / longest_time
    print "Case #{}: {}".format(ctr + 1, answer)
