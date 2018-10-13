#!/usr/bin/env python2.6
import sys
import itertools

def solve_case(data):
    places_to_be = {
        "O": [],
        "B": []
    }
    
    for robot, position in data:
        places_to_be[robot].append(position)
    
    to_do = list(data)
    
    t = 0
    
    current_positions = {
        "B": 1,
        "O": 1
    }
    
    while to_do:
        req_robot, req_position = to_do.pop(0)
        pressed = False
        
        while not pressed:
            t += 1
            
            for robot in "O", "B":
                if not places_to_be[robot]:
                    continue
                
                offset = places_to_be[robot][0] - current_positions[robot]
                
                if offset > 0:
                    current_positions[robot] += 1
                elif offset < 0:
                    current_positions[robot] -= 1
                elif req_robot == robot:
                    pressed = True
                    places_to_be[robot].pop(0)
    
    return t

def parse_line(line):
    parts = line.strip().split()
    
    return list(zip(parts[1::2], map(int, parts[2::2])))
    

for n, line in enumerate(sys.stdin):
    if n == 0:
        continue # number of cases
    
    solution = solve_case(parse_line(line))
    
    print "Case #{0}:".format(n), solution
