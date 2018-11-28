import os
import sys


class cookieclicker:
    class case:
        """
        contains a solution to a particular case of the cookieclicker problem!
        """
        def __init__(self, C, F, X):
            # calculate the time it takes to buy i farms
            def c_part(i):
                f = float(F)
                c = float(C)
                return c*sum([1.0/(2.0 + j*f) for j in range(i)])

            def x_part(i):
                return float(X)/(2.0 + i*float(F))

            def time_using_i_farms(i):
                return c_part(i) + x_part(i)

            n = 0
            # increment # of farms until we won't get a shorter total time
            # anymore
            while (time_using_i_farms(n) > time_using_i_farms(n+1)):
                n += 1

            self.result = str(time_using_i_farms(n))

    def __init__(self, filename):
        """
        solve a cookieclicker problem!
        """
        self.cases = self.parse(filename)
        filename = os.path.splitext(filename)
        output_filename = filename[0] + "_output" + filename[1]

        output_file = open(output_filename, "w")
        for case, index in zip(self.cases, range(len(self.cases))):
            output_file.write("Case #" + str(1+index) + ": "
                              + case.result + "\n")

        output_file.close()

    def parse(self, filename):
        cases = []
        f = open(filename)
        n = int(f.readline())

        for i in range(n):
            data = f.readline().replace("\n", "").split(" ")
            cases.append(self.case(data[0], data[1], data[2]))

        return cases


if __name__ == "__main__":
    solution = cookieclicker(sys.argv[1])
