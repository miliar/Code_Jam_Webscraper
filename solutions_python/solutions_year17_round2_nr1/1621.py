#!/usr/bin/env python3

filename = 'A-small-attempt0.in'

with open(f'{filename.split(".")[0]}.in', 'rt') as f:
    input_lines = [l.strip() for l in f.readlines()]

# assert int(input_lines[0])+1 == len(input_lines)
input_lines = input_lines[1:]

case_number = 1
solutions = []
i = 0
while i < len(input_lines):
    distance, n_horses = map(int, input_lines[i].split())
    i += 1

    horses = []
    for n in range(n_horses):
        start, speed = map(int, input_lines[i].split())
        i += 1
        horses.append((start, speed))

    horses = sorted(horses, key=lambda x: x[0])

    reverse_times = []
    prev_start = distance
    prev_speed = 0
    prev_time = 0
    for start, speed in horses[::-1]:
        assert prev_start > start
        to_go = distance - start
        time = to_go/speed
        if time < prev_time:
            assert prev_start < distance
            assert prev_speed > 0
            assert prev_time > 0
            time_max = (prev_start - start) / (speed - prev_speed)
            dist_max = time_max * speed
            assert dist_max < distance
            to_next = dist_max
            time = to_next/speed + (distance-to_next-start)/prev_speed
        reverse_times.append(time)
        prev_start = start
        prev_speed = speed
        prev_time = time
        print(case_number, start, time)

    solution = distance/prev_time
    solutions.append(f'Case #{case_number}: {solution}')
    case_number += 1

print(*solutions, sep='\n')
with open(f'{filename.split(".")[0]}.out', 'wt') as f:
    f.write('\n'.join(solutions))
