#!/usr/bin/env python3


def go_deeper(n_stalls, n_people):
    even_stalls = n_stalls % 2 == 0
    even_people = n_people % 2 == 0

    n_left_stalls = (n_stalls-1) // 2
    n_right_stalls = (n_stalls) // 2
    # print(n_stalls, n_people, n_stalls-n_people, n_left_stalls, n_right_stalls, end=' ')
    assert n_stalls >= n_people
    assert n_stalls == n_left_stalls + n_right_stalls + 1

    if n_people == 1:
        # print('Branch A')
        return sorted([n_left_stalls, n_right_stalls], reverse=True)
    elif even_stalls == even_people:
        # print('Branch B')
        return go_deeper(n_right_stalls, n_people - (n_people+1) // 2)
    else:
        # print('Branch C')
        return go_deeper(n_left_stalls, n_people - (n_people+1) // 2)


filename = 'C-large.in'

with open(f'{filename.split(".")[0]}.in', 'rt') as f:
    input_lines = [l.strip() for l in f.readlines()]

assert int(input_lines[0])+1 == len(input_lines)
input_lines = input_lines[1:]

solutions = []
for case_number, line in enumerate(input_lines, start=1):
    N, K = map(int, line.split())
    # print('Start', N, K)
    n_left, n_right = go_deeper(N, K)
    solutions.append(f'Case #{case_number}: {n_left} {n_right}')

print(*solutions, sep='\n')
with open(f'{filename.split(".")[0]}.out', 'wt') as f:
    f.write('\n'.join(solutions))
