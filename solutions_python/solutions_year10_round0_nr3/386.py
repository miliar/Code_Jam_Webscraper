"""
Some people go alone; other people go in groups, and don't want to board the
roller coaster unless they can all go together.

A ride costs 1 Euro per person; your job is to figure out how
much money the roller coaster will make today.


R = number of runs of the roller coaster
k = number of people the roller coaster can hold at once.
N = number of groups
g[] = size of the N groups
T = number of test cases

Once the ride is over, all of its passengers re-queue in the same order.

The roller coaster will run R times in a day.

For example, suppose R=4, k=6, and there are four groups of people with
sizes: 1, 4, 2, 1. The first time the roller coaster goes, the first two
groups [1, 4] will ride, leaving an empty seat (the group of 2 won't fit,
and the group of 1 can't go ahead of them). Then they'll go to the back
of the queue, which now looks like 2, 1, 1, 4. The second time, the
coaster will hold 4 people: [2, 1, 1]. Now the queue looks like 4, 2, 1,
1. The third time, it will hold 6 people: [4, 2]. Now the queue looks
like [1, 1, 4, 2]. Finally, it will hold 6 people: [1, 1, 4]. The roller
coaster has made a total of 21 Euros!

1 <= T <= 50
g[i] <= k

1 <= R <= 10 ** 8
1 <= k <= 10 ** 9
1 <= N <= 1000
1 <= g[i] <= 10 ** 7
"""

from sys import stdin
try:
    import psyco
    psyco.full()
except ImportError:
    pass

def main():
    T = int(stdin.readline())
    for i in xrange(T):
        R, k, N = map(int, stdin.readline().split())
        gs = map(int, stdin.readline().split())
        #assert N == len(gs)

        tot_euros = 0
        skips = [-1] * N
        euros = [-1] * N
        euros_fullcycle = 0
        nsteps_fullcycle = 0
        fullcycle_done = False

        pos = 0
        j = 0
        while j < R:
            if pos == 0 and j > 0:
                fullcycle_done = True
            if fullcycle_done and (j + nsteps_fullcycle) < R:
                #print "X" # *******************
                assert euros_fullcycle > 0
                assert nsteps_fullcycle > 0
                tot_euros += euros_fullcycle
                j += nsteps_fullcycle
            else:
                #print "Y" # *******************
                if skips[pos] != -1:
                    #print "*", # ********************
                    tot_euros += euros[pos]

                    #print pos # ********************
                    #if pos == 0: print "**" # *************

                    if not fullcycle_done:
                        nsteps_fullcycle += 1
                        euros_fullcycle += euros[pos]

                    pos = skips[pos]
                else:
                    #print "#", # ********************
                    old_pos = pos
                    tot = 0
                    cycle = 0
                    while cycle < N:
                        if (tot + gs[pos]) <= k:
                            tot += gs[pos]
                            pos = (pos + 1) % N
                        else:
                            break
                        cycle += 1
                    tot_euros += tot
                    euros[old_pos] = tot
                    skips[old_pos] = pos

                    if not fullcycle_done:
                        nsteps_fullcycle += 1
                        euros_fullcycle += tot

                    #print pos # ********************
                    #if pos == 0: print "##" # *************
                #print pos, tot, tot_euros, cycle # ********************
                j += 1


        print ("Case #%d:" % (i+1)), tot_euros
        #print # ********************
        #print # ********************
        #print skips # ********************
        #print euros # ********************

main()