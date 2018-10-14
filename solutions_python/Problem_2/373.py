#!/usr/bin/python

"""
Train Timetable problem solution
(GCJ 2008, Qualification Round)
Author: madrezaan
"""

import sys

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: train_timetable.py <input file>"
    sys.exit(0)

# get number of cases
num_cases = int(in_file.readline())

# begin prosessing cases
for cur_case in range(num_cases):

    # get turnaround time
    turnaround = int(in_file.readline())

    # get NA and NB
    na_nb = in_file.readline().split(" ")
    na = int(na_nb[0])
    nb = int(na_nb[1])

    # get schedule
    a_schedule = []
    b_schedule = []
    for i in range(na):
        a_schedule.append(in_file.readline())
    for i in range(nb):
        b_schedule.append(in_file.readline())
    a_schedule.sort()
    b_schedule.sort()
    for i in range(na):
        trip_string = a_schedule[i]
        a_schedule[i] = {'start': int(trip_string[:2]) * 60 + int(trip_string[3:5]),
                         'end': int(trip_string[6:8]) * 60 + int(trip_string[9:11]),
                         }
    for i in range(nb):
        trip_string = b_schedule[i]
        b_schedule[i] = {'start': int(trip_string[:2]) * 60 + int(trip_string[3:5]),
                         'end': int(trip_string[6:8]) * 60 + int(trip_string[9:11]),
                         }

    # modelling trips
    cur_time = 0
    a_trains_num = 0
    b_trains_num = 0
    a_trains_waiting = 0
    b_trains_waiting = 0
    a_arrive_queue = []
    b_arrive_queue = []
    while len(a_schedule) > 0 or len(b_schedule) > 0:
        if len(a_schedule) > 0:
            a_start =  a_schedule[0]['start']
        else:
            a_start = 1441
        if len(b_schedule) > 0:
            b_start =  b_schedule[0]['start']
        else:
            b_start = 1441
        if a_start < b_start:
            cur_trip = a_schedule.pop(0)
            cur_time = cur_trip['start']
        else:
            cur_trip = b_schedule.pop(0)
            cur_time = cur_trip['start']
        while len(a_arrive_queue) > 0 and a_arrive_queue[0] <= cur_time:
            a_arrive_queue.pop(0)
            a_trains_waiting += 1
        while len(b_arrive_queue) > 0 and b_arrive_queue[0] <= cur_time:
            b_arrive_queue.pop(0)
            b_trains_waiting += 1
        if a_start < b_start:
            if a_trains_waiting == 0:
                a_trains_num += 1
            else:
                a_trains_waiting -= 1
            b_arrive_queue.append(cur_trip['end'] + turnaround)
            b_arrive_queue.sort()
        else:
            if b_trains_waiting == 0:
                b_trains_num += 1
            else:
                b_trains_waiting -= 1
            a_arrive_queue.append(cur_trip['end'] + turnaround)
            a_arrive_queue.sort()

    # print result
    print "Case #%d: %d %d" % (cur_case + 1, a_trains_num, b_trains_num)
    
in_file.close()
