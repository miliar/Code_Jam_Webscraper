##TRAIN TIMETABLE##

##Thomas Pollom##


def convert_time_to_minutes_elapsed(time):
    """
    converts time entered as string in form 'HH:MM' into an int representing
    the number of minutes elapsed since 00:00.
    """
    time = time.replace(':','')
    minutes = int(time[2:4]) + 60*int(time[0:2])
    return minutes

def calc_num_trains_needed(departure_times, arrival_times, turnaround_time):
    """
    calculates the minimum number of trains needed at a station given a list of
    departure times (a list of ints), a list of arrival times (a list of ints), and
    a turnaround time (an int). returns an int.
    """
    time_list = []
    net_trains = 0
    trains_needed = 0
    for number in departure_times:
        time_list.append([number, -1])
    for number in arrival_times:
        time_list.append([(number + turnaround_time), 1])
    time_list.sort()
    for i in range(len(time_list)):
        net_trains += time_list[i][1]
        if net_trains < 0:
            if net_trains*(-1) > trains_needed:
                if i == (len(time_list) - 1) or time_list[i][0] != time_list[i+1][0]:
                    trains_needed = net_trains*(-1)
    return trains_needed                         

# Transform file to list.

input_file = open('/Users/scotty/Desktop/input_file2.txt', 'r')
raw_lines = input_file.readlines()
input_file.close()
lines = []
for line in raw_lines:
    line = line.rstrip('\n')
    lines.append(line)

output_file = open('/Users/scotty/Desktop/output_file2.txt', 'w')

# Calculate minimum number of trains for each train for each case.
# Assumes correct format for input file.

num_cases = int(lines[0])
lines_index = 2
current_case = 1
while current_case <= num_cases:
    total_num_trips_data = lines[lines_index].split()
    num_a_trips = int(total_num_trips_data[0])
    num_b_trips = int(total_num_trips_data[1])
    a_departure_times = []
    a_arrival_times = []
    b_departure_times = []
    b_arrival_times = []
    for line in lines[(lines_index + 1):(lines_index + num_a_trips + 1)]:
        line = line.split()
        a_departure_times.append(convert_time_to_minutes_elapsed(line[0]))
        b_arrival_times.append(convert_time_to_minutes_elapsed(line[1]))
    for line in lines[(lines_index + num_a_trips + 1):(lines_index + num_a_trips + num_b_trips + 1)]:
        line = line.split()
        b_departure_times.append(convert_time_to_minutes_elapsed(line[0]))
        a_arrival_times.append(convert_time_to_minutes_elapsed(line[1]))
    num_a_trains = calc_num_trains_needed(a_departure_times, a_arrival_times, int(lines[lines_index-1]))
    num_b_trains = calc_num_trains_needed(b_departure_times, b_arrival_times, int(lines[lines_index-1]))
    output = 'Case #%s: %s %s' %(current_case, num_a_trains, num_b_trains)
    output_file.write(output)
    output_file.write('\n')
    lines_index = lines_index + num_a_trips + num_b_trips + 2
    current_case += 1

output_file.close()

print 'done'
