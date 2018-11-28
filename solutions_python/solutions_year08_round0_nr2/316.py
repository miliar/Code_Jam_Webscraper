#!/usr/bin/python
#sort the times by departure time
#
#count unmber needed at each time
#  i.e. at 9:00 there must be 1 at A, at 10:00 there must be one at A
#  at 9 there is 1 at b, which means at 10:35 there is one at a

import sys, datetime

line = sys.stdin.readline

ncases = int(line())

def cmp1(x, y):
    return cmp(x[1], y[1])

for i in range(0,ncases):
    timeline = [] #entries are [time, change in trains at a, change in trains at b]
    aq = []
    bq = []
    turnaround = datetime.timedelta(minutes = int(line()))
    [na, nb] = map(int, line().split(" "))
    astart = 0
    bstart = 0

    for a in range(0,na):
        [str1, str2] = line().split(' ')

        [h, m] = map(int, str1.split(':'))
        depart = datetime.timedelta(hours = h, minutes = m)
        timeline.append([depart, -1, 0])

        [h, m] = map(int, str2.split(':'))
        arive = datetime.timedelta(hours = h, minutes = m)
        timeline.append([arive+turnaround, 0, 1])

    for b in range(0,nb):
        [str1, str2] = line().split(' ')

        [h, m] = map(int, str1.split(':'))
        depart = datetime.timedelta(hours = h, minutes = m)
        timeline.append([depart, 0, -1])

        [h, m] = map(int, str2.split(':'))
        arive = datetime.timedelta(hours = h, minutes = m)
        timeline.append([arive+turnaround, 1, 0])

    timeline.sort()

    a=0
    b=0
    for ti in range(0,len(timeline)):
        t = timeline[ti]
        a += t[1]
        b += t[2]

        #print t[0],":",a,b

        if(ti == len(timeline)-1 or t[0] != timeline[ti+1][0]):
            if a<astart:
                astart = a
            if b<bstart:
                bstart = b
        #else:
         #   print 'x'

    sys.stdout.write ("Case #")
    sys.stdout.write (str(i+1))
    print ":",(-1*astart),(-1*bstart)
