#!/usr/bin/python

import sys, re


def run():
    file = open(sys.argv[1],'r')

    laps = int( file.next())
    for lap in range(1,laps+1):
        turntime = int(file.next())

        m = re.match('(\d+) (\d+)', file.next())
        (na, nb) = map(int, m.groups())

        table = []
        for i in range(na+nb):
            m = re.match('(\d\d):(\d\d) (\d\d):(\d\d)', file.next())
            a, b, c, d = map(int, m.groups())
            table.append((a*60+b, c*60+d))
        (a, b) = zip(*table)

        print "Case #%d: %d %d" % (lap,
                                   calculate(a[:na], b[na:], turntime),
                                   calculate(a[na:], b[:na], turntime),
                                   )

def calculate(tout, tin, turn):
    # print tout, tin, turn
    leave = [(t,1) for t in tout]
    leave.extend([(t+turn,-1) for t in tin])
    leave.sort()
    
    used = 0
    peak = 0
    for (time, leave) in leave:
        used += leave
        peak = max(peak, used)
    return peak


run()
