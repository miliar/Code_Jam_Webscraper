#!/usr/local/bin/python2.5

#Parse and convert times to integers (i.e., hours * 100 + min) so it's easier to compare
#Each output begins at max values (i.e., NA and NB), subtract when find suitable train with proper turnaround
#How to save train schedule, whether tuple of (departure, arrival) or what

#Issues: a train could be gone already so problem of keeping track of where a train is
#Case:
        #10
        #2 2
        #9 10
        #11 12
        #11:30 12
        #11:50 13 - could get fooled by this one if just comparing to '10' arrival

def read_trips(number_trips, file):
    counter = 0
    schedule = []
#    print 'trips:',number_trips
    while counter < number_trips:
        line = file.readline().strip()
#        print line
        (departure, arrival) = line.split(" ")
        departure_int = (int(departure[0:2]) * 100) + int(departure[3:5])
        arrival_int = (int(arrival[0:2]) * 100) + int(arrival[3:5])
        schedule.append((departure_int, arrival_int))
        counter += 1
#        print counter, number_trips
    return schedule

def need_train(current_trains, departure):
    trains_to_add = 0
#    print 'trains avail:', current_trains, 'leave:', departure
    if not current_trains:
        trains_to_add = 1
    elif current_trains and current_trains[0] > departure:
        trains_to_add = 1
    elif current_trains and current_trains[0] <= departure:
        current_trains.pop(0)
    return current_trains, trains_to_add

def calculate_trains(schedule_1, schedule_2, turnaround):
    station_1 = station_2 = 0
    current_1 = []
    current_2 = []
    while schedule_1 or schedule_2:
#        print 'schedules:',schedule_1, schedule_2
#        print 'starting trains:',station_1, station_2
#        print 'trains avail:', current_1, current_2
        if schedule_1: departure_1, arrival_1 = schedule_1[0]
        if schedule_2: departure_2, arrival_2 = schedule_2[0]
        # Leaving from both at the same time
        if schedule_1 and schedule_2 and departure_1 == departure_2:
#            print 'leaving both'
            schedule_1.pop(0)
            current_1, trains_to_add = need_train(current_1, departure_1)
            station_1 += trains_to_add
            current_1.append(arrival_2 + turnaround)
            schedule_2.pop(0)
            current_2, trains_to_add = need_train(current_2, departure_2)
            station_2 += trains_to_add
            current_2.append(arrival_1 + turnaround)
        # Leaving from station 2
        elif schedule_2 and (not schedule_1 or departure_1 > departure_2):
#            print 'leaving 2'
            schedule_2.pop(0)
            current_2, trains_to_add = need_train(current_2, departure_2)
            station_2 += trains_to_add
            current_1.append(arrival_2 + turnaround)
        # Leaving from station 1
        elif schedule_1 and (not schedule_2 or departure_1 < departure_2):
#            print 'leaving 1'
            schedule_1.pop(0)
            current_1, trains_to_add = need_train(current_1, departure_1)
            station_1 += trains_to_add
            current_2.append(arrival_1 + turnaround)
        else:
            print 'ERROR'
        # TODO: this seems like a lot of work to maintain these lists, 
        #       would inserting manually be faster?
        current_1.sort()
        current_2.sort()
    return station_1, station_2

output_file = 'B-small-attempt1.out'
input_file = 'B-small-attempt1.in'

file_output = open(output_file,'w')
file_input = open(input_file)

total_cases = int(file_input.readline().strip())
case_number = 1

try:
    while case_number <= total_cases:
#        print 'case %d' % case_number
        turnaround = int(file_input.readline().strip())
        a_trains = b_trains = 0
        (NA, NB) = file_input.readline().strip().split(" ")
        a_schedule = read_trips(int(NA), file_input)
        b_schedule = read_trips(int(NB), file_input)
        a_schedule.sort()
        b_schedule.sort()
#        print a_schedule, b_schedule
        a_trains, b_trains = calculate_trains(a_schedule, b_schedule, \
                                                  turnaround)
        file_output.write("Case #%d: %d %d\n" % (case_number, a_trains, \
                                                     b_trains))
        case_number += 1
finally:
    file_input.close()
    file_output.close()
