import os
import sys

ifile = open(sys.argv[1])
ofile = open(sys.argv[2], 'w')

cases = int(ifile.readline())
for c in range(0, cases):
    line = ifile.readline().split()
    n = int(line[0])
    k = int(line[1])
    #print "---> ", n, " ", k
    
    #initialise a list with an OFF state for every snapper
    snapper_chain = [0 for x in range(0, n)]
    
    #start snapping ;)
    for i in range(0, k):
        #determine snappers to switch (those with power)
        power_index = []
        count = 0  
        for s in snapper_chain:
            if not count:  #first snapper always has power, so add it to power index
                power_index.append(count)
                count = count+1
                continue
            if snapper_chain[count-1]:
                power_index.append(count)
            else:
                break
            count = count+1

        #print "P: ", power_index

        # switch the snappers with power
        for p in power_index:
            snapper_chain[p] = 0 if snapper_chain[p] else 1

        #print "C: ", snapper_chain

    #determine if the light will be on after all snaps are done
    state = "ON"
    for s in snapper_chain:
        if not s:
            state = "OFF"

    ofile.write("Case #%s: %s\n" % (c+1, state))

ifile.close()
ofile.close()
