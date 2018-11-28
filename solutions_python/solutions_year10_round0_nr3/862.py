#! /usr/bin/python

import sys

def prepare_string(string):
    string = string.split(' ')
    for i in range(len(string)):
        string[i] = string[i].strip('\n')
        string[i] = int(string[i])
    return string

def lets_roll(rides, cap, n_groups, groups):
    euros = 0
    for i in range(rides):
        tmp = cap
        on_ride = []
        elements = 0
        for i in groups:
            tmp = tmp - i
            if tmp >= 0:
                on_ride.append(i)
                euros += i
                elements += 1
                continue
            else:
                groups = groups[elements:]
                groups.extend(on_ride) 
                break

    return euros

f = file(sys.argv[1], 'r')
cases = int(f.readline())

for times in range(cases):
    conf = prepare_string(f.readline())
    rides = conf[0]
    cap = conf[1]
    n_groups = conf[2]
    groups = prepare_string(f.readline())
    answer = lets_roll(rides, cap, n_groups, groups)
    print 'Case #' + str(times + 1) + ': ' + str(answer)
