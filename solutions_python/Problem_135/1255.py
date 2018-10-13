from __future__ import print_function

BAD_MAGITIAN = "Bad magician!"
BAD_VOLUNTEER = "Volunteer cheated!"


def response(case, common_elements):
    if not common_elements:
        result = BAD_VOLUNTEER
    elif len(common_elements) == 1:
        result = common_elements.pop()
    else:
        result = BAD_MAGITIAN

    return "Case #%d: %s" % (case, result)


def jump_lines(fp, lines):
    for i in range(lines):
        fp.readline()


def round(fp):
    row = int(fp.readline())
    jump_lines(fp, row - 1)
    line = set([int(x) for x in fp.readline().split(' ')])
    jump_lines(fp, 4 - row)
    return line


def solver(filename):
    with open(filename, 'r') as fp:
        cases = int(fp.readline())
        for case in range(cases):
            row_1 = round(fp)
            row_2 = round(fp)

            yield response(case + 1, row_1.intersection(row_2))

if __name__ == "__main__":
    with open("solution.txt", "w") as fp:
        for result in solver("A-small-attempt0.in"):
            fp.write("%s\n" % result)
