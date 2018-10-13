#!/usr/bin/env python
import sys

def test_cases(lines):
    num_cases = int(lines[0])
    for i in xrange(num_cases):
        case = [float(x) for x in lines[1+i].strip().split(' ')]
        yield (case[0], case[1], case[2])

def find_optimal(c, f, x):
    initial_velocity = 2.0
    max_time = x / initial_velocity
    min_time = max_time 
    i = 0
    v = []
    t0 = []
    tf = []
    while(True):
        # calculate velocity with 'i' farms
        v.append(initial_velocity + (i * f))
        # calculate incremental time to get 'i'th farm
        t0.append(c / v[i])
        # sum up the time it took to get 'i' farms, plus 
        # time to get 'x' cookies with 'i' farms
        tf.append(sum(t0[0:i]) + (x / v[i]))
        # if it's less than the minimum time, return
        if i > 0 and tf[i] > tf[i-1]:
            return tf[i-1]
        # End if the total time to accumulate 'i' farms exceeds the
        # time it would take to get 'x' cookies with 0 farms.
        if sum(t0[0:i]) > max_time:
            break
        i += 1
    return min_time

def process_file(filename):
    with open(filename, 'r') as input:
        n = 1
        for c, f, x in test_cases(input.readlines()):
            print "Case #%d: %.7f" % (n, find_optimal(c, f, x))
            n += 1

if __name__ == '__main__':
    assert len(sys.argv) == 2
    process_file(sys.argv[1])
