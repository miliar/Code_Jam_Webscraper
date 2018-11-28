
def solve_test(line, g):

    line = line.rstrip()
    # orig = int(line)
    line = list(line)
    idx  = len(line) - 1

    def check(nr):

        nr  = str(nr)
        idx = len(nr) - 1
        while idx >= 1:
            # print nr[idx], nr[idx-1]
            if int(nr[idx - 1]) > int(nr[idx]):
                return False
            idx -= 1
        return True

    # print check(1000)
    # exit(0)

    last_split = -1

    while idx >= 0:

        digit = int(line[idx])

        if idx == 0:

            if last_split != -1:
                line = line[:last_split] + ['9'] * (len(line) - last_split)

            if digit != 0:
                sol = line
            else:
                sol = line[1:]

            # cnr = orig
            # while not check(cnr):
            #     cnr -= 1

            g.write("".join(sol))
            return

        prev_digit = int(line[idx - 1])

        if digit == 0 or prev_digit > digit:
            last_split    = idx
            line[idx - 1] = str(prev_digit - 1)

        idx -= 1



def solve(file):

    with open(file) as f:
        with open("res", "w") as g:
            for idx, line in enumerate(f.readlines()[1:]):
                g.write("Case #" + str(idx + 1) + ": ")
                solve_test(line, g)
                g.write("\n")


def main():
    # solve("B-small-attempt1.in")
    solve("B-large.in")


if __name__ == "__main__":
    main()

