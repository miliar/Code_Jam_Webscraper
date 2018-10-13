import fileinput 
import sys
import math

stdin = fileinput.input()
debug = False

def one_pair(N, horses, routes, start, stop):
    assert(start == 0);
    assert(stop == N - 1);
    min_times = [ float("inf") for _ in range(N) ]
    min_times[start] = 0
    for i in range(N):
        if debug: print "i:", i
        min_time = min_times[i]
        if debug: print "min_time for {}: {}".format(i, min_time)
        (max_dist, speed) = horses[i]
        total_dist = 0 
        for j in range(i+1, N):
            if debug: print "j:", j
            one_step_dist = routes[j-1][j]
            assert(one_step_dist != -1);
            if debug: print one_step_dist
            if debug: print speed
            total_dist += one_step_dist;
            if debug: print "total dist:", total_dist
            if total_dist <= max_dist:
                if debug: print total_dist
                time_for_this_horse = min_time + total_dist / float(speed)
                if debug: print time_for_this_horse
                if debug: print j
                if debug: print min_times[j]
                min_times[j] = min(min_times[j], time_for_this_horse)
            if debug: print min_times
    return min_times[stop]

def do_case(N, horses, routes, city_pairs):
    return [ one_pair(N, horses, routes, start, stop) for (start, stop) in city_pairs ]

T = int(next(stdin))
print "T:", T

for case_num in range(1, T+1):
    case_input = next(stdin)
    N, Q = case_input.split(' ')
    N, Q = int(N), int(Q)
    print "{} cities".format(N)
    print "{} pairs of cities".format(Q)
    horses = []
    for i in range(N):
        case_input = next(stdin)
        E, S = case_input.split(' ')
        E, S = int(E), int(S)
        horses.append((E, S))
    routes = []
    for i in range(N):
        case_input = next(stdin)
        routes.append([ int(x) for x in case_input.split(' ') ])
    city_pairs = []
    for i in range(Q):
        case_input = next(stdin)
        U, V = [ int(x) for x in case_input.split(' ') ]
        city_pairs.append((U - 1, V - 1))
    print "horses: ", horses
    print "routes: ", routes
    print "city_pairs: ", city_pairs
    x = do_case(N, horses, routes, city_pairs)
    print "Case #{}: {}".format(case_num, " ".join([str(y) for y in x]))
    sys.stdout.flush()

