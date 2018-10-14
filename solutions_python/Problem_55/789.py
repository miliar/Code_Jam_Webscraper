import sys
import os

ifile = open(sys.argv[1])
ofile = open(sys.argv[2], "w")

cases = int(ifile.readline())

for c in range(0, cases):
    line = ifile.readline().split()
    R = int(line[0])
    k = int(line[1])
    N = int(line[2])

    groups = ifile.readline().split()
    queue = []
    #fucked up python! doesn't allow queue = groups!!
    for g in groups:
        queue.append(g)
    dosh = 0
    print "--> Rid:", R, ", Cap:", k, " : ", groups
    
    #start rides!
    for r in range(0, R):
        coaster_fullness = 0
        coaster_peeps = []
        # fit groups
        for g in groups:
            if coaster_fullness + int(g) <= k:
                coaster_fullness = coaster_fullness + int(g)
                queue.remove(g)
                coaster_peeps.append(g)
                dosh=dosh+int(g)
            else:
                #GO!!
                break;

        #Add peeps back onto queue after ride
        queue.extend(coaster_peeps)

        groups = []
        for q in queue:
            groups.append(q)

    ofile.write("Case #%s: %s\n" % (c+1, dosh))
    #print dosh


ifile.close()
ofile.close()
