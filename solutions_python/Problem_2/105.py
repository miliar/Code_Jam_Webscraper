#!/usr/bin/python

import sys
data = filter(None, map(lambda x:x.strip(), open(sys.argv[1]).readlines()))

def pop_int(data):
    return int(data.pop(0))

def pop_ints(data):
    return map(int, data.pop(0).split())

def pop_rows(data, num_rows):
    result = data[:num_rows]
    for i in range(num_rows):
        data.pop(0)
    return result

def time_to_int(t):
    hours, mins = map(int, t.split(':'))
    return hours*60 + mins

def times_to_ints(s):
    return map(time_to_int, s.split())

def pop_case(data):
    turnaround = pop_int(data)
    na, nb = pop_ints(data)
    a_trips = map(times_to_ints, pop_rows(data, na))
    b_trips = map(times_to_ints, pop_rows(data, nb))
    return turnaround, a_trips, b_trips
     

def drive_greedily_from(pos, start, dest, turnaround):
    start_time, arrive_time =  start.pop(pos)
    for i, trip in enumerate(dest):
        next_start, next_arrive = trip
        if next_start >= arrive_time+turnaround:
            break
    else:
        return
    drive_greedily_from(i, dest, start, turnaround)


def drive_greedily(start, dest, turnaround):
    drive_greedily_from(0, start, dest, turnaround)

num_cases = pop_int(data)
for case_num in range(1, num_cases+1):
    turnaround, a_trips, b_trips = pop_case(data)
    a_trips.sort()
    b_trips.sort()
    num_a = num_b = 0
    while a_trips or b_trips:
        if not b_trips:
            num_a += 1
            drive_greedily(a_trips, b_trips, turnaround)
        elif not a_trips:
            num_b += 1
            drive_greedily(b_trips, a_trips, turnaround)
        elif a_trips[0][0] <= b_trips[0][0]:
            drive_greedily(a_trips, b_trips, turnaround)
            num_a += 1
        else:
            drive_greedily(b_trips, a_trips, turnaround)
            num_b += 1
    print "Case #%d: %d %d" % (case_num, num_a, num_b)
