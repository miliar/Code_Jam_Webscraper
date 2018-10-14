#!/usr/bin/python3
from itertools import count
from collections import defaultdict, namedtuple

def case(destination, horses):
    # all horses will cross within 10^9, as min speed is 1, and max distance is 10^9
    max_time = 0
    for next_horse in horses:
        distance_left = max(0, destination - next_horse.position)
        max_time = max(max_time, distance_left / next_horse.speed)

    return destination / max_time 

Horse = namedtuple('Horse', ('position', 'speed'))

def cases(data):
    num_cases = int(data.pop(0))
    cases = []
    while data:
        destination, num_horses = map(int, data.pop(0).split(' '))
        horses = []
        for i in range(num_horses):
            horses.append(Horse(*map(int, data.pop(0).split(' '))))
        cases.append((destination, horses))

    for case_number, params in zip(count(1), cases):
        result = case(*params)
        print("Case #{}: {:.6f}".format(case_number, result))

with open('input', 'r') as f:
    cases(f.readlines())
