import sys

flip_dict = {ord('-'): '+', ord('+'): '-'}


def flip(pancakes):
    return pancakes.translate(flip_dict)


def flips(pancakes: str, flip_len):
    count = 0

    while '-' in pancakes:
        pancakes = pancakes.lstrip('+')  # Now, pancakes starts with a -

        if len(pancakes) < flip_len:
            return 'IMPOSSIBLE'

        pancakes = flip(pancakes[:flip_len]) + pancakes[flip_len:]
        count += 1

    return count


for index, line in enumerate(sys.stdin, start=0):
    if index == 0:
        continue

    (p, l) = line.split()
    print(f'Case #{index}:', flips(p, int(l)))