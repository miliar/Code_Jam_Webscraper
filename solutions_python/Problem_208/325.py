def solve(horses, distances):
    # if i use that horse, what's the fatest way to get there
    # time to get there and speed of horse
    ans = [[100000000000000, 0] for i in xrange(len(distances) + 1)]
    ans[0][0] = 0

    total_dist = 0
    for stop in xrange(len(distances)):
        

        for horse_i in xrange(stop + 1):
            endurance, speed = horses[horse_i]
            distance_between = sum(distances[horse_i: stop+1])

            if endurance >= distance_between:
                
                # this horse can reach
                
                total_time = ans[horse_i][0] + distance_between / float(speed)
                # print "horse", horse_i, "can reach", stop, distance_between, "at spede", total_time
                if total_time < ans[stop + 1][0]:

                    ans[stop + 1][0] = total_time
    return ans[-1][0]




for case in xrange(input()):
    n, q = map(int, raw_input().split(' '))
    horses = []
    for i in xrange(n):
        horses.append(map(int, raw_input().split(' ')))

    distances = []
    for i in xrange(n):
        if i == n - 1: continue
        ds = map(int, raw_input().split(' '))
        distances.append(ds[i+1])
    raw_input()
    raw_input()
    answer = solve(horses, distances)
    print "Case #%d: %f" % (case + 1, answer)



