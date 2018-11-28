import os
import sys


class magicTrick:
    class case:
        """
        contains the relevant info and the solution to a magictrick case
        """
        def __init__(self, row_a, layout_a, row_b, layout_b):
            # identify which elements are in row_a of layout_a
            num_from_first_row = 0
            magic_number = -1
            for item in layout_b[row_b]:
                if item in layout_a[row_a]:
                    num_from_first_row += 1
                    magic_number = item
            if num_from_first_row == 0:
                # volunteer cheated since no cards in common between chosen
                # rows
                self.result = "Volunteer Cheated!"
            elif num_from_first_row > 1:
                # magician is bad since he didn't separate the cards from
                # chosen row
                self.result = "Bad Magician!"
            else:
                # magician did it correctly and volunteer cheated, so the
                # "magic_number" variable is the volunteer's number
                self.result = str(magic_number)

    def __init__(self, filename):
        """
        get input and solve the problem
        """
        self.cases = self.parse(filename)
        filename = os.path.splitext(filename)
        output_filename = filename[0] + "_output" + filename[1]

        output_file = open(output_filename, "w")

        for case, index in zip(self.cases, range(len(self.cases))):
            output_file.write("Case #" + str(1+index) + ": " + case.result + "\n")

        output_file.close()

    def parse(self, filename):
        """
        parses an input file for the magic trick problem
        -returns a list of case objects
        """
        f = open(filename)
        n = int(f.readline())

        cases = []
        for i in range(n):
            # read in info for a case and add it to the cases
            # offset of 1 for index
            row_a = int(f.readline()) - 1
            layout_a = []
            for j in range(4):
                layout_a.append(f.readline().replace("\n", "").split(" "))

            # offset of 1 for index
            row_b = int(f.readline()) - 1
            layout_b = []
            for j in range(4):
                layout_b.append(f.readline().replace("\n", "").split(" "))

            cases.append(self.case(row_a, layout_a, row_b, layout_b))

        return cases

if __name__ == "__main__":
    trick = magicTrick(sys.argv[1])
