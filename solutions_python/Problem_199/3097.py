#/bin/env python3


def get_result(pancakes, k):
    flips = 0
    while not all_happy(pancakes):
        flip_index = pancakes.index('-')
        if flip_index + k > len(pancakes):
            return 'IMPOSSIBLE'
        pancakes = flip(pancakes, flip_index, k)
        flips += 1
    return flips


def all_happy(pancakes):
    return '-' not in pancakes


TRANSLATION_MAP = {ord('+'): '-', ord('-'): '+'}


def flip(pancakes, start, k):
    middle = pancakes[start:start+k].translate(TRANSLATION_MAP)
    return pancakes[:start] + middle + pancakes[start+k:]


results = []
with open('large.in') as input_file:
    with open('large.out', 'w') as output_file:
        T = int(input_file.readline())

        for i in range(T):
            line = input_file.readline().split()
            result = get_result(line[0], int(line[1]))
            output_file.write('Case #' + str(i+1) + ': ' + str(result) + '\n')
