import sys
stream = open(sys.argv[1])

T = int(stream.readline())

def debug(s, *args):
    if 0:
        print s % args

for case in range(T):
    # R: number of rides
    # k: size of roller coaster
    # N: number of groups
    R, k, N = [int(x) for x in stream.readline().split()]
    g = [int(x) for x in stream.readline().split()]
    assert len(g) == N

    # total revenue
    revenue = 0

    if sum(g) < k:
        # special case, everyone fits on the roller coaster
        revenue = sum(g) * R
    else:
        # Now loop, until we detect a cycle or quit.  On detecting a cycle,
        # attempt to compute profit and length of cycle (or quit early).  Then count how
        # many whole cycles we can do + last partial cycle profit.
        
        def take(i): 
            # i is group number 
            # return number of people taken, and new position
            c = 0 # number of people taken
            while c + g[i] <= k:
                c += g[i]
                i = (i+1) % N
            return c, i

        # True means we have used this queue start position before
        used = [False] * N  

        rides = 0
        i = 0
        used[i] = True
        while rides < R:
            c, i = take(i)
            rides += 1
            revenue += c
            debug("Took %d people, position is %d", c, i)
            if not used[i]:
                used[i] = True
            else:
                # found a cycle!
                cyclestart = i
                break

        # Determine revenue and length of cycle (returning to same queue state)
        # Cycle can have length of at most 1000 by pigeonhole principle
        # Careful about off-by-one here!
        cycrev = []

        debug("Cycle starts at pos %d", cyclestart)
        while rides < R:
            c, i = take(i)
            debug("Took %d people, position is %d", c, i)
            rides += 1
            revenue += c
            if not cycrev:
                cycrev.append(c)
            else:
                cycrev.append(cycrev[-1] + c)
            if i == cyclestart:
                # cycle has been completed
                break

        # Need to use the calculated cycle revenue
        if rides < R:
            cyclen = len(cycrev) # number of rides in cycle
            debug("Cycle length is %d", cyclen)
            fullcyclerevenue = cycrev[-1] # profit from full cycle
            fullcycles = (R-rides) / cyclen 
            remainder = (R-rides) % cyclen 
            revenue += fullcyclerevenue * fullcycles
            if remainder > 0:
                revenue += cycrev[remainder-1]

    print "Case #%d: %d" % (case+1, revenue)



