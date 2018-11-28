import sys
from math import floor, ceil

MAX_POSSIBLE_PANCAKES = 1000
pancake_holder = [0 for i in range(MAX_POSSIBLE_PANCAKES+1)]

class Diner:
    __slots__ = ["eaters", "max_pancake"]
    def __init__(self, num_eaters, eaters):
        self.eaters = pancake_holder[:]
        self.max_pancake = 0
        for plate in list(map(int, eaters.split(" "))):
            self.eaters[plate] += 1
            if plate > self.max_pancake:
                self.max_pancake = plate

def simulate_splits(original, hiding_spot, max_pancakes):
    eaters      = original[:]
    splits      = 0
    splitting   = True
    time_needed = 0
    while splitting:
        splitting = False
        for j in reversed(range(hiding_spot + 1, max_pancakes + 1)):
            if eaters[j] > 0:
                # decrement
                eaters[j] -= 1
                # distribute:
                eaters[j - hiding_spot] += 1
                eaters[hiding_spot]     += 1
                splitting = True
                splits += 1
                break
    if max_pancakes > hiding_spot:
        return hiding_spot + splits
    else:
        for j in reversed(range(max_pancakes + 1)):
            if eaters[j] > 0:
                time_needed = splits + j
                break
        return hiding_spot + splits

def solve_diner(diner):
    # find worst plate (the one to split):
    max_pancake = diner.max_pancake
    # num splits:
    min_time = max_pancake
    for hiding_spot in range(1, max_pancake + 1):
        min_time = min(
            simulate_splits(
                diner.eaters,
                hiding_spot,
                max_pancake),
            min_time)
    return min_time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage %s [filename]" % (sys.argv[0]))
        exit(1)
    filename = sys.argv[1]

    read_file =  open(filename, "rt").read()

    number_of_sols, diners = read_file.split("\n", 1)


    diner_sols = []
    number_of_sols = int(number_of_sols)
    diners = diners.split("\n")
    number_of_lines_to_read = 2 * number_of_sols
    line_number = 0
    problem_number = 1
    while line_number < number_of_lines_to_read:
        print("Case #%d: %d" % (problem_number, solve_diner(
                    Diner(
                        diners[line_number],
                        diners[line_number+1]
                    )
                )
            )
        )
        problem_number += 1
        line_number += 2
