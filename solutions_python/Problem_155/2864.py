#!/usr/bin/env python
import sys
import re

def read_input():
    r = {}
    r['problems'] = []
    input_lines = sys.stdin.read().splitlines()
    for line_index, line in enumerate(input_lines):
        if line_index == 0:
            r['t'] = int(line)
            continue
        problem = {}
        problem['line'] = line
        x = re.split(' ',  line)
        problem['smax'] = int(x[0])
        problem['array'] = [int(i) for i in x[1]]
        r['problems'].append(problem)
    return r

def solve_problem(x):
    r = []
    for problem in x['problems']:
        people = []
        for i in range(problem['smax'] + 1):
            shyness_level = i
            num_of_people = problem['array'][i]

            person = {
                'shyness_level': i
            }
            for j in range(num_of_people):
                people.append(person)
        clapping_people = 0
        need = 0
        for person in people:
            if person['shyness_level'] == 0:
                clapping_people = clapping_people + 1
                continue
            if clapping_people >= person['shyness_level']:
                clapping_people = clapping_people + 1
                continue

            requirement = abs(clapping_people - person['shyness_level'])
            need = need + requirement
            clapping_people = clapping_people + requirement + 1
        r.append({
            'audience_count': len(people),
            'clapping_people': clapping_people,
            'need': need
        })
    return r

def print_output(r):
    for i in range(len(r)):
        print "Case #%d: %d" % (i + 1, r[i]['need'])



x = read_input()
x = solve_problem(x)
print_output(x)