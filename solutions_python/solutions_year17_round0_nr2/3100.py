from utils import pairwise


def is_tidy(number: str) -> bool:
    return all(d1 <= d2 for d1, d2 in pairwise(number))


def is_increasing(number: str) -> bool:
    return all(d1 < d2 for d1, d2 in pairwise(number))


def is_tidy_with_increasing_end(number: str) -> bool:
    return is_tidy(number) and is_increasing(number[-2:])


def solve(number: str) -> str:
    if is_tidy(number):
        return number
    length_to_decrement_and_keep = next((i for i in range(len(number) + 1)
                                         if not is_tidy_with_increasing_end(number[:i + 1])),
                                        len(number))
    return (number[:length_to_decrement_and_keep - 1] +
            chr(ord(number[length_to_decrement_and_keep - 1]) - 1) +
            '9' * len(number[length_to_decrement_and_keep:])).lstrip('0')


solutions = []
with open('B-small-attempt1.in', 'r') as input_file:
    input_file.readline()
    for line in input_file:
        solutions.append(solve(line.strip()))

with open('B-small-attempt1.out', 'w') as output_file:
    for line in (f'Case #{i}: ' + solution for i, solution in enumerate(solutions, start=1)):
        output_file.write(line + '\n')
