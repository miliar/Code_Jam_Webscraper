fin = open('E:\\cj\\C-large.in', 'r')
lines = fin.readlines()
fin.close()

fout = open('E:\\cj\\c.out', 'w')

case = 0
cases = int(lines[0])
lp = 1
for case in xrange(1, cases + 1):
    l = lines[lp]
    R, k, N = [int(x) for x in l.split()]
    l = lines[lp + 1]
    g = [int(x) for x in l.split()]

    y = 0

    # goes first means how many euros list
    gfe = []
    # goes first means who goes first next list
    gfn = []
    for i in xrange(0, len(g)):
        euros = g[i]        
        j = (i + 1) % N
        while euros < k and j != i:
            if euros + g[j] <= k:
                euros += g[j]
                j = (j + 1) % N
            else:
                break
        gfe.append(euros)
        gfn.append(j)

    seen = set()

    who = 0
    seen.add(who)
    y0 = y
    y1 = y
    cycle_length = -1
    full_cycles = -1
    for rnd in xrange(R):
        y0 += gfe[who]
        who = gfn[who]

        if who in seen:
            # establish the cycle info
#            print 'Cycle! at %d by %d followed by %d' % (rnd, who, gfn[who])
            cwho = gfn[who]
            count = 1
            cycle_euros = [gfe[who]]

            while cwho != who:
                count += 1                
                cycle_euros.append(gfe[cwho])
                cwho = gfn[cwho]

            cycle_length = count
            # work out the euros earned
            left = R - rnd - 1
            full_cycles = left / count
            y0 += sum(cycle_euros) * full_cycles

            #who = gfn[who]
            for i in xrange(rnd + full_cycles * count + 1, R):
                y0 += gfe[who]
                who = gfn[who]
            break
        else:
            seen.add(who)

##    who = 0
##    hep = 0
##    for rnd in xrange(R):
##        y1 += gfe[who]
##        hep = who
##        who = gfn[who]
###        if rnd == R - 1:
###            print who
##        
##    if y1 != y0:
##        print 'mismatch!', cycle_length, full_cycles, y1, y0, hep, whogga, y1 - y0#, gfe[gfn[whogga]]
##    else:
##        print 'good!', cycle_length, full_cycles
    fout.write('Case #%d: %s\n' % (case, y0))
    lp += 2

fout.close()
    
