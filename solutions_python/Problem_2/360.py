import fileinput

def hours_mins_to_mins (hh_mm):
    (hh, mm) = hh_mm.split(':')
    return int(hh) * 60 + int(mm)

def mins_to_hours_min (mm): return '%02d:%02d' % (mm / 60, mm % 60)

fitr = iter (fileinput.input())

for case in range (int(fitr.next())):
    turnaround = int(fitr.next())

    (na, nb) = (int(x) for x in fitr.next().split())

    (a_sched, b_sched) = ([], [])

    for (depart, arrive) in (fitr.next().split() for i in range(na)):
        a_sched.append ((hours_mins_to_mins (depart), 1))
        b_sched.append ((hours_mins_to_mins (arrive) + turnaround, -1))

    for (depart, arrive) in (fitr.next().split() for i in range(nb)):
        b_sched.append ((hours_mins_to_mins (depart), 1))
        a_sched.append ((hours_mins_to_mins (arrive) + turnaround, -1))

    a_sched.sort()
    b_sched.sort()

    a_req = 0
    acc = 0

    for flag in (x[1] for x in a_sched):
        acc += flag
        if acc > 0:
            a_req += acc
            acc = 0
    
    b_req = 0
    acc = 0

    for flag in (x[1] for x in b_sched):
        acc += flag
        if acc > 0:
            b_req += acc
            acc = 0

    print 'Case #%d: %d %d' % (case + 1, a_req, b_req)
