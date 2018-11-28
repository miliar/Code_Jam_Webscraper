from __future__ import with_statement
from sys import argv
from datetime import timedelta

AB = True
BA = False

def todatetimedelta(time):
    hour, minute = time.split(":")
    return timedelta(hours=int(hour), minutes=int(minute))

with open(argv[1]) as filein:
    inp = filein.read().splitlines()

nbcase = int(inp.pop(0))

for case in range(nbcase):
    turn = timedelta(minutes=int(inp.pop(0)))
    nbtrips = [int(n) for n in inp.pop(0).split()]

    trips = []
    for nbtrip, trip in zip(nbtrips, (AB, BA)):
        for timetable in inp[:nbtrip]:
            trips.append(([todatetimedelta(i) for i in timetable.split()], trip))
        del inp[:nbtrip]
    trips.sort()

    avail = {AB : [], BA : []}
    nb = {AB : 0, BA : 0}

    for (dep, ar), trip in trips:
        if not avail[trip]:
            nb[trip] += 1
        elif avail[trip][0] <= dep:
            del avail[trip][0]
        else:
            nb[trip] += 1
        avail[not trip].append(ar + turn)
        avail[not trip].sort()

    print "Case #%d: %d %d" % (case+1, nb[AB], nb[BA])
