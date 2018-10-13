#!/bin/env python

def read_data():
    case_number = int(raw_input())
    cases = []
    for i in range(case_number):
        line = raw_input()
        max_shyness, description = line.split()
        shynesses = []
        for index, amount in enumerate(description):
            shynesses.append(int(amount))
        cases.append(shynesses)
    return cases


def solve(case):
    people_required = 0
    people_up_so_far = 0
    for shyness, amount in enumerate(case):
        if people_up_so_far < shyness:
            people_required += shyness - people_up_so_far
            people_up_so_far = shyness
        people_up_so_far += amount
    return people_required

if __name__ == "__main__":
    data = read_data()
    for position, case in enumerate(data):
        solution = solve(case)
        print "Case #%s: %s" % (position + 1, solution)
