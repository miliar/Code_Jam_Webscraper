"""gcj"""

def solve():
    """solve"""

    with open("A-small.in") as in_file:
        with open("A.out", "w+") as out_file:

            num_cases = int(in_file.readline())
            for case_index in xrange(num_cases):

                result = ""
                print(
                    "Case #" + str(case_index + 1) + ": " + result + " - done"
                )

                out_file.write(
                    "Case #" + str(case_index + 1) + ": " + result + "\n"
                )

def solve_a():
    """solve_a"""

    import math

    with open("A-small-attempt0.in") as in_file:
        with open("A.out", "w+") as out_file:

            num_cases = int(in_file.readline())
            for case_index in xrange(num_cases):
                (in_r, in_t) = tuple([float(i) for i in in_file.readline().split()])

                tmp = 2.0 * in_r - 1
                res = int((math.sqrt(tmp * tmp  + 8.0 * in_t) - tmp) / 4.0)

                result = str(res)
                print(
                    "Case #" + str(case_index + 1) + ": " + result + " - done"
                )

                out_file.write(
                    "Case #" + str(case_index + 1) + ": " + result + "\n"
                )

def main():
    """main"""
    solve_a()

if __name__ == "__main__":
    main()