import sys
import collections

infile = sys.stdin

def compute_time(num_boosters, booster_time, num_planets, cycle):
    cycle_dist = sum(cycle)
    num_cycles = num_planets // len(cycle)
    end_segment = cycle[0:N%len(cycle)]
    total_dist = num_cycles*cycle_dist + sum(end_segment)
    #print "***", total_dist, cycle_dist
    if (total_dist<=booster_time or num_boosters==0): return total_dist
    # travel before booster, get number of cycles traversed and remaining part of cycle with booster
    cycles_before_booster = booster_time // cycle_dist
    dist_into_cycle = booster_time % cycle_dist
    start_segment = collections.deque(cycle)
    while dist_into_cycle>0:
        if dist_into_cycle >= start_segment[0]:
            dist_into_cycle -= start_segment.popleft()
        else:
            start_segment[0] -= dist_into_cycle
            dist_into_cycle = 0
            
    remaining_cycles = num_cycles - cycles_before_booster - 1
    
    remainder = list(start_segment) + (remaining_cycles * cycle) + end_segment
    #print "***", booster_time, remaining_cycles, start_segment, remainder
    remainder.sort()
    #print "*** sorted ", remainder
    # booster works on max num_boosters
    for i in xrange(num_boosters):
        remainder[-i-1] //= 2
    
    #print "***", remainder
    return booster_time + sum(remainder)
    

T = int(infile.readline())
for i in xrange(T):
    tokens = infile.readline().split()
    L, t, N, C = map(int, tokens[0:4])
    # scale distances by 2 so we stay in integers
    cycle = [2*int(s) for s in tokens[4:]]
    
    result = compute_time(L, t, N, cycle)
    print("Case #%d: %d" % (i+1, result))
