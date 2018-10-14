import sys
import math


class BathroomStalls:

    def __init__(self):
        self.read_file()
        self.resolve_cases()
        self.write_file()

    def read_file(self):
        with open(sys.argv[1]) as fin:
            lines = fin.readlines()[1:]
            lines = [line.replace("\n", "") for line in lines]

        self.lines = lines

    def resolve_cases(self):
        solutions = []
        for line in self.lines:
            solution = self.resolve_case(line)
            solutions.append(solution)

        self.solutions = solutions

    def resolve_case(self, case):
        (stalls, person_n) = [int(c) for c in case.split(" ")]

        divisions = 2 ** math.floor(math.log(person_n) / math.log(2))
        max_size = int(math.ceil((stalls - person_n + 1) / float(divisions)))
        maxLR = max_size / 2
        minLR = int(math.ceil(max_size / 2.0) - 1)

        solution = "{} {}".format(maxLR, minLR)
        return solution

    def write_file(self):
        (file_path, extension) = sys.argv[1].split(".")
        file_path = "{}_solved.{}".format(file_path, extension)

        with open(file_path, "w") as fout:
            for case in range(len(self.solutions)):
                fout.write("Case #{}: {}\n".format(case + 1, self.solutions[case]))


if __name__ == "__main__":
    bathrom_stalls = BathroomStalls()
