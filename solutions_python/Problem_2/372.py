#!/usr/bin/env python
"""
Google Code Jam: Train Timetable
http://code.google.com/codejam/contest/dashboard?c=agdjb2RlamFtcg8LEghjb250ZXN0cxjqOQw

n = # of test cases
t = turnaround time
da, aa, db, ab:
  * d = depart; a = arrive
  * a = station a; b = station b
suma, sumb = "sum" of trains at a and b, where
  * train arriving: +1
  * train departing: -1
"""

from time import strptime       # Replace with datetime.strptime
from datetime import datetime, timedelta


for i in xrange(input()):
    t = timedelta(minutes=input())
    addt = lambda as: [at+t for at in as]
    nab, nba = [int(x) for x in raw_input().split()]
    mktime = lambda tstr: datetime(*strptime(tstr, "%H:%M")[0:6])
    da, ab, db, aa = [], [], [], []
    if nab > 0:
        da, ab = zip(*[[mktime(ta) for ta in raw_input().split()]
                       for x in xrange(nab)])
    if nba > 0:
        db, aa = zip(*[[mktime(tb) for tb in raw_input().split()]
                       for x in xrange(nba)])
    times = [(x, 'da') for x in da]
    times.extend((x, 'ab') for x in addt(ab))
    times.extend((x, 'db') for x in db)
    times.extend((x, 'aa') for x in addt(aa))
    times.sort()        # Rely on {aa, ab} sorting before {da, db}

    suma, sumb = 0, 0
    nta, ntb = 0, 0
    for _, op in times:
        if   op == 'da': suma -= 1
        elif op == 'aa': suma += 1
        elif op == 'db': sumb -= 1
        elif op == 'ab': sumb += 1
        else: raise ValueException(op)
        if suma < 0:
            suma += 1
            nta += 1
        if sumb < 0:
            sumb += 1
            ntb += 1

    print "Case #%d: %d %d" % (i+1, nta, ntb)
