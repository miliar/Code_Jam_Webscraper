#!/usr/bin/python

import sys

def debug(msg):
#    return
    sys.stderr.write("\x1b[33;1m"+str(msg)+"\x1b[0m\n")

nb = int(raw_input())

res2 = 0
tres2 = 0

for case in xrange(1, nb+1):
    nb_plates = int(raw_input())
    mem = raw_input()

    plates = [ int(p) for p in mem.split() ]

    debug("\n\n\n%d"%(case))
    plates.sort(reverse=True)
    debug("start")
    debug(plates)

    etape = 0
    time = 0
    mm = plates[0]
    res = time+mm
    tres = time+mm

    while(plates[0] > 1):
        old_time=time
        old_mm=mm
        next_etape = (mm / 2 ) + (mm & 0x01)
        while(plates[0] > next_etape):
            time += 1
            temp = plates[0] / 2
            plates[0] -= temp
            plates.append(temp)

            plates.sort(reverse=True)
            tres = min(tres, time+plates[0])
            debug("    "+str(plates))

        etape += 1
        mm = plates[0]
        debug("Etape %d, time=%d" % (etape, time))
        debug(plates)
        res = time+mm

        if old_time+old_mm < time+mm:
            res = old_time+old_mm
            break

    # hjqhqsjkhdqs
    plates = [ int(p) for p in mem.split() ]

    debug("\n\n\n%d"%(case))
    plates.sort(reverse=True)
    debug("start")
    debug(plates)

    etape = 0
    time = 0
    mm = plates[0]
    res2 = time+mm
    tres2 = time+mm

    while(plates[0] > 2):
        old_time=time
        old_mm=mm
        if mm == 9:
            next_etape = (mm *2/ 3 )
        else:
            next_etape = (mm / 2 ) + (mm & 0x01)
        while(plates[0] > next_etape):
            time += 1
            if plates[0] == 9:
                temp = plates[0] / 3
            else:
                temp = plates[0] / 2
            plates[0] -= temp
            plates.append(temp)

            plates.sort(reverse=True)
            tres2 = min(tres2, time+plates[0])
            debug("    "+str(plates))

        etape += 1
        mm = plates[0]
        debug("Etape %d, time=%d" % (etape, time))
        debug(plates)
        res2 = time+mm

        if old_time+old_mm < time+mm:
            res2 = old_time+old_mm
            break


    print "Case #%d: %d" % (case, min(res, tres, res2, tres2))
