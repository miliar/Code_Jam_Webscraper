import sys


def do_rides(rides, capacity, groups):
    ngroups = len(groups)
    head = 0 # front of the line
    total = 0
    
    # check if everybody can fit on every ride
    nvisitors = sum(groups)
    if nvisitors < capacity:
        return nvisitors * rides
        
    # map head position to (total, ride number) so we can detect cycles
    cycles = {0 : (0, 0)}
    
    i = 0
    while i<rides:
        passengers = 0
        while True:
            if passengers + groups[head] <= capacity:
                passengers += groups[head]
                head = head+1
                if head==ngroups: head = 0
            else:
                break
        total += passengers
        i += 1
        
        if cycles:
            # if we've been at this head position before, apply the maximum number of cycles
            if head in cycles:
                prev_total, prev_ride = cycles[head]
                sys.stderr.write("Found cycle at ride=%d, total=%d: head=%d, prev_ride=%d, prev_total=%d\n" % (i, total, head, prev_ride, prev_total))
                cycle_length = i - prev_ride
                cycle_passengers = total - prev_total
                sys.stderr.write("Cycle length=%d, passengers=%d\n" % (cycle_length, cycle_passengers))
                rides_left = rides - i
                num_cycles = rides_left // cycle_length
                total += (num_cycles * cycle_passengers)
                i += (num_cycles * cycle_length)
                sys.stderr.write("Applied %d cycles: ride=%d, total=%d\n" % (num_cycles, i, total))
                # pick up the remaining rides without cycles
                cycles = None
            else:
                cycles[head] = (total, i)
        
    return total


infile = sys.stdin
ntests = int(infile.readline().strip())        
for i in xrange(ntests):
    R, k, N = map(int, infile.readline().strip().split())
    g = map(int, infile.readline().strip().split())
    result = do_rides(R, k, g)
    print("Case #%d: %d" % (i+1, result))