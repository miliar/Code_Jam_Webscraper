from sys import *

def coast(_, R, k, peeps):
    print "Case #%d:" %(_ + 1),

    euros = 0
    for i in range(R):
        capacity = k
        peeps_onboard = []
        while((len(peeps) > 0) and (capacity >= peeps[0])):
            euros += peeps[0]
            capacity -= peeps[0]
            peeps_onboard.append(peeps.pop(0))
        peeps.extend(peeps_onboard)

    print euros

cases = int(raw_input())
for _ in xrange(cases):
    R, k, N = stdin.readline().split()
    peeps = [int(x) for x in stdin.readline().split()]
    coast(_, int(R), int(k), peeps)
