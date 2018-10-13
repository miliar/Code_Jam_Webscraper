import sys


class TestCase(object):
    def __init__(self, pancakes, flipper_size):
        self._pancakes = pancakes
        self._flipper_size = flipper_size

    def _is_aligned(self, pancakes):
        for p in pancakes:
            if p == "-":
                return False

        return True

    def flip(self, pancakes, start_index, flip_size):
        for i in xrange(start_index, start_index+flip_size):
            if pancakes[i] == "+":
                pancakes[i] = "-"
            else:
                pancakes[i] = "+"

    def _trim_aligned(self, pancakes):
        length = len(pancakes)
        first_blank_index = length
        for i, pancake in enumerate(pancakes):
            if pancake == "-":
                first_blank_index = i
                break

        return pancakes[first_blank_index:]

    def _solve_aux(self, pancakes):
        if len(pancakes) == 0:
            return 0

        if self._is_aligned(pancakes):
            return 0

        if len(pancakes) < self._flipper_size:
            return -1

        count_with_flip = -1
        count_without_flip = -1

        # with flip
        pancakes_with_flip = list(pancakes) # copy
        self.flip(pancakes_with_flip, 0, self._flipper_size)
        count_with_flip = self._solve_aux(self._trim_aligned(pancakes_with_flip))
        if count_with_flip != -1:
            count_with_flip += 1

        # without_flip
        if pancakes[0] == "+":
            pancakes_without_flip = list(pancakes)[1:]
            count_without_flip = self._solve_aux(self._trim_aligned(pancakes_without_flip))

        if count_with_flip == -1 and count_without_flip == -1:
            return -1
        elif count_with_flip == -1:
            return count_without_flip
        elif count_without_flip == -1:
            return count_with_flip
        return min(count_with_flip, count_without_flip)

    def solve(self):
        flip_count = self._solve_aux(self._pancakes)
        if flip_count == -1:
            return "IMPOSSIBLE"
        return flip_count

    def __str__(self):
        return "Panckaes: {0}    ;   Flipper: {1}".format("".join(self._pancakes), self._flipper_size)


def parse(input_file_path):
    test_cases = []

    with open(input_file_path, "r") as input_file:
        test_cases_number = int(input_file.readline())
        for i in xrange(test_cases_number):
            line = input_file.readline()
            values = line.split(" ")
            test_case = TestCase(pancakes=list(values[0]), flipper_size=int(values[1]))
            test_cases.append(test_case)

    return test_cases


def main(input_file_path):
    test_cases = parse(input_file_path)

    for i, test_case in enumerate(test_cases):
        solution = test_case.solve()
        print "Case #{0}: {1}".format(i+1, solution)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))