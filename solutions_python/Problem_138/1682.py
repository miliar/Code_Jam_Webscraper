import sys


def start():
    magic = Blocks()
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
        self.blocks_each = 0
        self.naomis_blocks = None
        self.kens_blocks = None

    def parse_lines(self, lines):
        self.blocks_each = int(lines[0])
        self.naomis_blocks = [float(block) for block in lines[1].split(" ")]
        self.kens_blocks = [float(block) for block in lines[2].split(" ")]

    def play_war(self):
        ken_copy = set(self.kens_blocks[:])
        naomi_copy = self.naomis_blocks[:]
        naomis_points = 0
        kens_points = 0
        for nblock in naomi_copy:
            potential_kblocks = set([block for block in ken_copy if block > nblock])
            if len(potential_kblocks) == 0:
                chosen_kblock = min(ken_copy)
            else:
                chosen_kblock = min(potential_kblocks)
            if chosen_kblock > nblock:
                kens_points += 1
            else:
                naomis_points += 1
            ken_copy.remove(chosen_kblock)

        return naomis_points


    def play_deceit_war(self):
        ken_copy = set(self.kens_blocks[:])
        naomi_copy = self.naomis_blocks[:]
        naomis_points = 0
        kens_points = 0
        for nblock in sorted(naomi_copy):
            potential_kblocks_real = set([block for block in ken_copy if block > nblock])
            potential_real_smaller = set([block for block in ken_copy if block < nblock])
            #if no potential bigger blocks, play honestly
            if len(potential_kblocks_real) > 0 and len(potential_real_smaller) == 0:
                nsays = max(potential_kblocks_real) - 0.000001
            elif len(potential_kblocks_real) > 0 and len(potential_real_smaller) > 0:
                #pick huge, throw small away
                nsays = 10 - 0.000001
            else:
                nsays = nblock

            potential_kblocks = set([block for block in ken_copy if block > nsays])

            if len(potential_kblocks) == 0:
                chosen_kblock = min(ken_copy)
            else:
                chosen_kblock = min(potential_kblocks)
            if chosen_kblock > nblock:
                kens_points += 1
            else:
                naomis_points += 1
            ken_copy.remove(chosen_kblock)

        return naomis_points

class Blocks(Base):

    def __init__(self):
        super().__init__()
        self.test_cases = []

    def parse_input(self):
        self.num_tests = int(input())
        for x in range(0, self.num_tests*3):
            line = input()
            self.input_rows.append(line)


    def run_case(self, test_case):

        return str(test_case.play_deceit_war()) + " " + str(test_case.play_war())


    def run(self):
        for x in range(0, self.num_tests):
            new_test = TestCase()
            new_test.parse_lines(self.input_rows[0 + (x * 3) : 3 + (x * 3)])
            self.test_cases.append(new_test)

        for test_case in self.test_cases:
            self.output_rows.append(self.run_case(test_case))


if __name__ == "__main__":
    start()