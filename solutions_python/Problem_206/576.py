#!/usr/bin/python

def get_horse_time(distance, horse):
    distance_left = distance - horse["location"]
    time_left = float(distance_left) / float(horse["speed"])
    #print "location: " + str(horse["location"])
    #print "distance_left: " + str(distance_left)
    #print "time_left: " + str(time_left)
    return time_left

def solve(distance, horses):
    slowest_horse_time = 0
    for horse in horses:
        horse_time = get_horse_time(distance, horse)
        if horse_time > slowest_horse_time:
            slowest_horse_time = horse_time
        #print "slowest_horse_time: " + str(slowest_horse_time)
        #print "distance: " + str(distance)
    return float(distance) / float(slowest_horse_time)

import sys
input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

i=1
current_line = 1
while len(stripped_input_lines) > current_line:
    #print "new test!!!!!!!!!!!"
    horses = []
    test_line = stripped_input_lines[current_line]
    #print test_line
    distance = int(test_line.split()[0])
    horse_c = int(test_line.split()[1])
    current_line += 1
    current_test_line = 0
    while current_test_line < horse_c:
        test_line = stripped_input_lines[current_line + current_test_line]
        horse_location = int(test_line.split()[0])
        horse_speed = int(test_line.split()[1])
        horse = {"location" : horse_location, "speed" : horse_speed}
        horses.append(horse)
        current_test_line += 1
        #print test_line
    current_line += horse_c
    result = solve(distance, horses)
    print "Case #"+str(i)+": "+str(result)
    i+=1
