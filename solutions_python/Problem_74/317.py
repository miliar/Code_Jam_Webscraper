from pprint import pprint

T = int(raw_input().strip())        # grabs an integer from stdin

for case in range(1,T+1):
    line = raw_input().strip().split(' ')
    orders = zip(line[1::2],map(int,line[2::2]))

    last_t = {'O':0, 'B':0 }
    last_p = {'O':1, 'B':1 }
    time = 0

    for robot, position in orders:
        dist = abs(position - last_p[robot])  # travel time
        ready_by = last_t[robot] + dist       # earliest robot is in position
        go_at = max(ready_by,time)            # take TotalOrder into account
        last_t[robot] = time = go_at + 1      # pressing takes 1s, robot busy 'til then
        last_p[robot] = position              # robot now at position

    print "Case #%d: %d" % (case, time)

