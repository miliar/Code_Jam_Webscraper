#!/usr/bin/env python3

filename = 'B-large.in'

with open(f'{filename.split(".")[0]}.in', 'rt') as f:
    input_lines = [l.strip() for l in f.readlines()]

assert int(input_lines[0])+1 == len(input_lines)
input_lines = input_lines[1:]

solutions = []
for case_number, line in enumerate(input_lines, start=1):
    N, = map(int, line.split())
    n_digits = len(str(N))

    if n_digits == 1:
        last_tidy = N
    else:
        S = int('1'*n_digits)

        if S > N:
            n_digits -= 1
            last_tidy = int('1'*(n_digits))
            S = int('1'*n_digits)

        current_digit = 0
        last_tidy = S
        while current_digit < n_digits:
            S = [int(x) for x in str(S)]
            for i in range(current_digit, n_digits):
                S[i] += 1
            S = int(''.join(map(str, S)))
            if N >= S:
                last_tidy = S
            else:
                current_digit += 1
                S = last_tidy

    assert last_tidy <= N
    solutions.append(f'Case #{case_number}: {last_tidy}')

print(*solutions, sep='\n')
with open(f'{filename.split(".")[0]}.out', 'wt') as f:
    f.write('\n'.join(solutions))
