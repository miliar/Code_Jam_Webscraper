import sys


def start():
    magic = Magic()
    magic.parse_input()
    magic.run()
    magic.print_output()


class Base():
    def __init__(self):
        self.counter = 1
        self.input_rows = []
        self.num_tests = 0
        self.output_rows = []

    def parse_input(self):
        self.num_tests = int(input())
        for x in range(0, self.num_tests):
            line = input()
            self.input_rows.append(line)

    def run(self):
        pass

    def print_output(self):
        for row in self.output_rows:
            print("Case #%d: %s" %(self.counter, row))
            self.counter += 1


class TestCase():
    def __init__(self):
        self.first_selection = 0
        self.second_selection = 0
        self.first_grid = []
        self.second_grid = []

    def parse_lines(self, lines):
        self.first_selection = int(lines[0])
        for line in lines[1:5]:
            self.first_grid.append([int(card) for card in line.split(" ")])
        self.second_selection = int(lines[5])
        for line in lines[6:10]:
            self.second_grid.append([int(card) for card in line.split(" ")])


class Magic(Base):

    def __init__(self):
        super().__init__()
        self.test_cases = []

    def parse_input(self):
        self.num_tests = int(input())
        for x in range(0, self.num_tests*10):
            line = input()
            self.input_rows.append(line)


    def run_case(self, test_case):
        first_poss = test_case.first_grid[test_case.first_selection - 1]
        second_poss = test_case.second_grid[test_case.second_selection - 1]

        found = 0
        found_item = 0
        for item in first_poss:
            if item in second_poss:
                found += 1
                found_item = item

        if found == 1:
            return str(found_item)
        elif found > 1:
            return "Bad magician!"
        else:
            return "Volunteer cheated!"

    def run(self):
        for x in range(0, self.num_tests):
            new_test = TestCase()
            new_test.parse_lines(self.input_rows[0 + (x * 10) : 10 + (x * 10)])
            self.test_cases.append(new_test)

        for test_case in self.test_cases:
            self.output_rows.append(self.run_case(test_case))


if __name__ == "__main__":
    start()