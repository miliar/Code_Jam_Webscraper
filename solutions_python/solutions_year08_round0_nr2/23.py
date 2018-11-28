testcase = """2
5
3 2
09:00 12:00
10:00 13:00
11:00 12:30
12:02 15:00
09:00 10:30
2
2 0
09:00 09:01
12:00 12:02"""

import re

def parsescheduleline(line):
    t = re.compile("(\d{2}):(\d{2})\s+(\d{2}):(\d{2})").match(line).groups()
    depart = int(t[0])*60+int(t[1])
    arrive = int(t[2])*60+int(t[3])
    return (depart,arrive)

def solvetrains(atimes, btimes, turnaroundtime):
    a_depart = {}
    b_depart = {}
    a_ready = {}
    b_ready = {}
    for atime in atimes:
        a_depart[atime[0]] = a_depart.get(atime[0],0)+1
        b_ready[atime[1]+turnaroundtime] = b_ready.get(atime[1]+turnaroundtime,0)+1
    for btime in btimes:
        b_depart[btime[0]] = b_depart.get(btime[0],0)+1
        a_ready[btime[1]+turnaroundtime] = a_ready.get(btime[1]+turnaroundtime,0)+1
    #print atimes,btimes
    #print a_depart, b_depart
    #print a_ready, b_ready
    num_a_avail = 0
    num_b_avail = 0
    num_a_needed = 0
    num_b_needed = 0
    for t in range(24*60):
        num_a_avail += a_ready.get(t,0)
        num_b_avail += b_ready.get(t,0)
        num_a_depart = a_depart.get(t,0)
        num_b_depart = b_depart.get(t,0)
        if num_a_depart > num_a_avail:
            num_a_needed += num_a_depart - num_a_avail
            num_a_avail = 0
        else:
            num_a_avail -= num_a_depart
        if num_b_depart > num_b_avail:
            num_b_needed += num_b_depart - num_b_avail
            num_b_avail = 0
        else:
            num_b_avail -= num_b_depart
    return (num_a_needed,num_b_needed)
    
#lines = testcase.splitlines()
lines = open("B-large.in").readlines()
ntestcases = int(lines[0])
offset = 1
for i in xrange(ntestcases):
    turnaroundtime = int(lines[offset])
    offset += 1
    na,nb = tuple([int(x) for x in lines[offset].split()])
    offset += 1
    atimes = []
    for x in range(na):
        atimes.append(parsescheduleline(lines[offset]))
        offset+=1
    btimes = []
    for x in range(nb):
        btimes.append(parsescheduleline(lines[offset]))
        offset+=1
    na,nb = solvetrains(atimes,btimes,turnaroundtime)
    print "Case #%d: %d %d" % (i+1, na, nb)

