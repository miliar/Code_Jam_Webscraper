#! /usr/bin/python

# train scheduler problem
# google code jam 2008 qualifier round
# some code copy-and-pasted from search_engine_switch.py,
# which was submitted for problem #1

def make_trips_from_input(trip_list):

    return [[int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in x.split()] for x in trip_list]
    
def get_n_trains( train_turnaround, there_trips, back_trips ):

    trains_here = []
    trains_there = []

    trains_starting_here = 0
    trains_starting_there = 0

    t_trips = [[trip, 'there'] for trip in there_trips]
    b_trips = [[trip, 'back'] for trip in back_trips]

    all_trips = t_trips + b_trips
    all_trips.sort()
    print all_trips

    for trip in all_trips:

        if trip[1] == 'there':
            if trains_here == []:
                trains_starting_here = trains_starting_here + 1
                trains_there.append(trip[0][1] + turnaround)
                trains_there.sort()
                
            elif min(trains_here) <= trip[0][0]:
                trains_here = trains_here[1:]
                trains_there.append(trip[0][1] + turnaround)
                trains_there.sort()
                
            else:
                trains_starting_here = trains_starting_here + 1
                trains_there.append(trip[0][1] + turnaround)
                trains_there.sort()
                

        else:
            if trains_there == []:
                trains_starting_there = trains_starting_there + 1
                trains_here.append(trip[0][1] + turnaround)
                trains_here.sort()
                
            elif min(trains_there) <= trip[0][0]:
                trains_there = trains_there[1:]
                trains_here.append(trip[0][1] + turnaround)
                trains_here.sort()
                
            else:
                trains_starting_there = trains_starting_there + 1
                trains_here.append(trip[0][1] + turnaround)
                trains_here.sort()

    return [trains_starting_here, trains_starting_there]

import sys

if len(sys.argv) != 3:
    print 'Please use the following syntax:'
    print '  [./train_scheduler.py] [input_file_name] [output_file_name]'
    sys.exit()
    
input_file_data = file(sys.argv[1]).read().split("\n")

n_cases = int(input_file_data[0])
file_progress = 1
n_cases_done = 0

out_handle = file(sys.argv[2], 'w')

while n_cases_done < n_cases:

    # load queries
    turnaround = int(input_file_data[file_progress])
    [n_ab_trips, n_ba_trips] = [int(x) for x in input_file_data[file_progress + 1].split()]
    
    ab_trips = make_trips_from_input(input_file_data[file_progress + 2: file_progress + 2 + n_ab_trips])
    ab_trips.sort()
    file_progress = file_progress + 2 + n_ab_trips
    
    ba_trips = make_trips_from_input(input_file_data[file_progress: file_progress + n_ba_trips])
    ba_trips.sort()
    file_progress = file_progress + n_ba_trips
    print turnaround
    print ab_trips
    print ba_trips

    out_string = 'Case #' + str(n_cases_done + 1) + ': ' + ' '.join([str(x) for x in get_n_trains(turnaround, ab_trips, ba_trips)]) + "\n"
    out_handle.write(out_string)
    print out_string # dual output for easy debugging.  Hooray!

    # move on to next case
    n_cases_done = n_cases_done + 1

out_handle.close()
