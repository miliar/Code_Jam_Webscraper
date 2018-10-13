import sys

HAPPY_SIDE = '+'
BLANK_SIDE = '-'


def is_finished(pancakes):
    return len(pancakes) == pancakes.count(HAPPY_SIDE)


def flip(pancakes):
    return [
        HAPPY_SIDE if pancake == BLANK_SIDE else BLANK_SIDE
        for pancake in pancakes
    ]


def make_happy(pancakes, flip_size):
    flipped_pancakes = list(pancakes)
    count = 0
    while True:
        if is_finished(flipped_pancakes):
            return count
        first_blank = flipped_pancakes.index(BLANK_SIDE)
        end_range = first_blank + flip_size
        if end_range > len(flipped_pancakes):
            return "IMPOSSIBLE"
        pancake_range = flipped_pancakes[first_blank: end_range]
        flipped_pancakes[first_blank: end_range] = flip(
            pancake_range)
        count += 1


if __name__ == "__main__":
    data = sys.stdin.readline()
    num_cases = int(data)
    for num_case in range(num_cases):
        case = sys.stdin.readline()
        pancakes, flip_size = case.split(" ")
        min_flips = make_happy(pancakes, int(flip_size))
        print("Case #{}: {}".format(num_case+1, min_flips))