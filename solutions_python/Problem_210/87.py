#!/usr/bin/python

def solve(c_free_time, j_free_time, c_active_c, j_active_c, times):
    sorted_start_times = sorted(times.iterkeys())
    start_times_c = len(sorted_start_times)
    j_possible_free_times = []
    c_possible_free_times = []
    forced_change_c = 0
    gap_times = []
    total_gap_time = 0
    #print "times: " + str(times)
    #print "sorted_start_times: " + str(sorted_start_times)
    #print "start_times_c: " + str(start_times_c)
    for i in xrange(start_times_c):
        if i == start_times_c - 1:
            start_time = sorted_start_times[i]
            next_stat_time = sorted_start_times[0]
            time_diff = (1440 - times[start_time]["end_time"]) + next_stat_time
        else:
            start_time = sorted_start_times[i]
            next_stat_time = sorted_start_times[i+1]
            time_diff = next_stat_time - times[start_time]["end_time"]
        #print "time_diff: " + str(time_diff)
        if times[start_time]["owner"] == times[next_stat_time]["owner"]:
            possible_free_time_add = time_diff
            if times[start_time]["owner"] == "J":
                j_possible_free_times.append(possible_free_time_add)
            else:
                c_possible_free_times.append(possible_free_time_add)
        else:
            forced_change_c += 1
            gap_time = time_diff
            if gap_time > 0:
                gap_times.append(gap_time)
                total_gap_time += gap_time
    sorted_j_possible_free_times = sorted(j_possible_free_times)
    sorted_c_possible_free_times = sorted(c_possible_free_times)
    #print "total_gap_time: " + str(total_gap_time)
    j_left_free_times = []
    total_j_possible_left = 0
    for j_possible_free_time in sorted_j_possible_free_times:
        if j_free_time + j_possible_free_time <= 720:
            j_free_time += j_possible_free_time
        else:
            j_left_free_times.append(j_possible_free_time)
            total_j_possible_left += j_possible_free_time
    #print "total_j_possible_left: " + str(total_j_possible_left)
    if j_free_time + total_gap_time + total_j_possible_left >= 720:
        return forced_change_c + 2 * len(j_left_free_times)
    c_left_free_times = []
    total_c_possible_left = 0
    for c_possible_free_time in sorted_c_possible_free_times:
        if c_free_time + c_possible_free_time <= 720:
            c_free_time += c_possible_free_time
        else:
            c_left_free_times.append(c_possible_free_time)
            total_c_possible_left += c_possible_free_time
    #print "total_c_possible_left: " + str(total_c_possible_left)
    assert c_free_time + total_gap_time + total_c_possible_left >= 720, "something is wrong!1!"
    return forced_change_c + 2 * len(c_left_free_times)


import sys
input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

i=1
current_line = 1
while len(stripped_input_lines) > current_line:
    #print "new test!!!!!!!!!!!"
    test_line = stripped_input_lines[current_line]
    #print test_line
    c_active_c = int(test_line.split()[0])
    j_active_c = int(test_line.split()[1])
    current_line += 1
    times = {}
    c_free_time = 0
    j_free_time = 0
    current_test_line = 0
    while current_test_line < c_active_c:
        test_line = stripped_input_lines[current_line + current_test_line]
        start_time = int(test_line.split()[0])
        end_time = int(test_line.split()[1])
        time = {"start_time" : start_time, "end_time" : end_time, "owner" : "C"}
        times[start_time] = time
        c_free_time += end_time - start_time
        current_test_line += 1
        #print test_line
    current_line += c_active_c
    current_test_line = 0
    while current_test_line < j_active_c:
        test_line = stripped_input_lines[current_line + current_test_line]
        start_time = int(test_line.split()[0])
        end_time = int(test_line.split()[1])
        time = {"start_time" : start_time, "end_time" : end_time, "owner" : "J"}
        times[start_time] = time
        current_test_line += 1
        j_free_time += end_time - start_time
        #print test_line
    current_line += j_active_c
    result = solve(c_free_time, j_free_time, c_active_c, j_active_c, times)
    print "Case #"+str(i)+": "+str(result)
    i+=1
