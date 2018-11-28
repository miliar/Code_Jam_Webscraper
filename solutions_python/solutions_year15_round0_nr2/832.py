#!/usr/bin/env python

import sys

from math import ceil, floor


def solve_naive_test(pancakes_per_plate, minute=0):
    if not any(pancakes_per_plate):
        return minute
    else:
        splits = xrange(len(pancakes_per_plate))
        eaten_one = [(x - 1) if x > 0 else 0 for x in pancakes_per_plate]
        solutions = [solve_naive_test(eaten_one, minute + 1)]
        for split in splits:
            if pancakes_per_plate[split] > 2:
                split_one = pancakes_per_plate[:split]
                split_one.append(int(floor(pancakes_per_plate[split] / 2.0)))
                split_one.append(int(ceil(pancakes_per_plate[split] / 2.0)))
                split_one.extend(pancakes_per_plate[split + 1:])
                solutions.append(solve_naive_test(split_one, minute + 1))

        return min(solutions)

def one_eaten(plates):
    return [(x - 1) if x > 0 else 0 for x in plates]

def mean(l):
    return float(sum(l)) / len(l)

def max_split(slope, max_slope, max_count):
    for p in xrange(1, int(max_slope / 2.0) + 1):
        s = list(slope)
        for x in xrange(max_count):
            s[x] -= p
        s.extend([p] * max_count)
        #print '\t', s
        yield s



def solve(pancakes_per_plate, minute=0, log=[]):
    if not any(pancakes_per_plate):
        return (minute, log)
    else:
        slope = list(sorted(pancakes_per_plate, reverse=True))
        max_slope = max(slope)
        max_count = sum(1 for p in slope if p == max_slope)

        #print slope, max_slope, max_count

        solutions = [solve(one_eaten(slope), minute + 1, log + ['eat'])]
        if max_slope > 2:
            for split in max_split(slope, max_slope, max_count):
                solutions.append(
                    solve(
                        split,
                        minute + max_count,
                        log + ['split {x}'.format(x=max_count)],
                ))
        return min(solutions, key=lambda k: k[0])

if __name__ == '__main__':
    input_file_name = sys.argv[1]
    input_file = open(input_file_name)
    number_of_cases = int(input_file.readline().strip())

    first_case_number = 1
    for x in xrange(number_of_cases):
        sys.stderr.write("{x}\n".format(x=x))
        nonempty_plate_count = int(input_file.readline().strip())
        pancakes_per_plate = [int(d) for d in input_file.readline().strip().split()]
        #print "Input", pancakes_per_plate
        solution, log = solve(pancakes_per_plate)
        print "Case #{case_number}: {minutes_needed}".format(
            case_number=(first_case_number + x),
            minutes_needed=solution
        )
        #print log
