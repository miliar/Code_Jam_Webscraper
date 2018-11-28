#!/usr/bin/env python
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()


def distances(slot_length: int):
    _max = slot_length // 2
    _min = math.ceil(slot_length / 2) - 1
    return _max, _min


def solve(number_of_stalls: int, people: int) -> str:
    print(f"Placing {people} persons in {number_of_stalls} stalls...")
    slots = dict([(number_of_stalls, 1)])
    last_distances = (0, 0)
    for i in range(people):
        slot = 0
        to_delete = []
        for slot_length, count in slots.items():
            if count:
                slot = slot_length
                slots[slot] -= 1
                break
            else:
                to_delete.append(slot_length)
        for slot_length in to_delete:
            del slots[slot_length]

        last_distances = distances(slot)

        try:
            slots[last_distances[0]] += 1
        except KeyError:
            slots[last_distances[0]] = 1

        try:
            slots[last_distances[1]] += 1
        except KeyError:
            slots[last_distances[1]] = 1
    return " ".join(map(str, last_distances))


solutions = []
with open(f'{args.filename}.in', 'r') as input_file:
    input_file.readline()
    for line in input_file:
        solutions.append(solve(*map(int, line.strip().split())))

with open(f'{args.filename}.out', 'w') as output_file:
    for line in (f'Case #{i}: ' + solution for i, solution in enumerate(solutions, start=1)):
        output_file.write(line + '\n')
