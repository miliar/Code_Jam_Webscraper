#!/usr/bin/python

def calc_min_time(length, walk_speed, run_speed, run_sec, walkways):
    # Insert boost=0 walkway for areas with no walkways.
    walkway_len = sum(end - beg for beg, end, boost in walkways)
    assert walkway_len <= length
    walkways.append((0, length - walkway_len, 0))

    # Run on slowest walkways.
    walkways.sort(key=lambda (beg, end, boost): boost)
    # print walkways
    run_left = run_sec
    total_time = 0.0
    for beg, end, boost in walkways:
        run_time = (end - beg) * 1.0 / (run_speed + boost)
        walk_time = 0.0
        if run_time > run_left:
            run_time = run_left
            run_dist = run_time * (run_speed + boost)
            walk_dist = end - beg - run_dist
            walk_time = walk_dist * 1.0 / (walk_speed + boost)
        # print "beg=%d end=%d boost=%d run_time=%f walk_time=%f" %\
        #         (beg, end, boost, run_time, walk_time)
        run_left -= run_time
        total_time += run_time + walk_time
    # print "total time %f" % total_time
    return total_time



if __name__ == "__main__":
    import sys
    tests = int(sys.stdin.readline())
    for t in range(tests):
        length, walk_speed, run_speed, run_sec, n =\
                map(int, sys.stdin.readline().split())
        walkways = []
        for i in range(n):
            beg, end, boost = map(int, sys.stdin.readline().split())
            walkways.append((beg, end, boost))
        min_time = calc_min_time(length, walk_speed, run_speed,
                                 run_sec, walkways)
        print "Case #%d: %f" % (t + 1, min_time)


