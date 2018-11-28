import numpy

FILENAME = 'A-small-attempt1'


def parse_input():
    data = []
    with open(FILENAME + ".in", "r") as f:
        for line in f:
            data.append(line.strip("\n"))

    T = int(data[0])
    cases = []
    index = 1
    for t in range(T):
        R, C = data[index].split(" ")
        index += 1
        cases.append([])
        for r in range(int(R)):
            cases[-1].append(data[index])
            index += 1
    return cases


def get_area(matrix, letter, ld):
    area_max = (0, [])
    other_letters = list(ld.keys())
    other_letters.remove(letter)
    w = numpy.zeros(dtype=int, shape=matrix.shape)
    h = numpy.zeros(dtype=int, shape=matrix.shape)
    for r in range(matrix.shape[0]):
        for c in range(matrix.shape[1]):
            if matrix[r][c] in other_letters:
                continue
            if r == 0:
                h[r][c] = 1
            else:
                h[r][c] = h[r - 1][c] + 1
            if c == 0:
                w[r][c] = 1
            else:
                w[r][c] = w[r][c - 1] + 1
            minw = w[r][c]
            for dh in range(h[r][c]):
                minw = min(minw, w[r - dh][c])
                area = (dh + 1) * minw
                if area > area_max[0] and r-dh <= ld[letter][0] <= r and c - minw + 1 <= ld[letter][1] <= c:
                    area_max = (area, [r - dh, c - minw + 1, r, c])
    return area_max


def get_largest_area(matrix, done, ld):
    max_area = (0, [])
    max_letter = None
    for letter in ld.keys():
        if letter in done:
            continue
        area = get_area(matrix, letter, ld)
        if area[0] > max_area[0]:
            max_area = area
            max_letter = letter
    return max_letter, max_area


def solve_case(case):
    done = []
    ld = dict()
    for r, row in enumerate(case):
        for l, letter in enumerate(row):
            if letter != '?':
                ld[letter] = (r, l)

    nrows = len(case)
    ncols = len(case[0])
    matrix = numpy.fromiter(''.join(case), dtype='<U3').reshape(nrows, ncols)

    while "?" in matrix:
        letter, area = get_largest_area(matrix, done, ld)
        matrix[area[1][0]:area[1][2]+1, area[1][1]:area[1][3]+1] = letter
        done.append(letter)
    return matrix


def solve():
    cases = parse_input()
    with open(FILENAME + ".out", 'w') as f:
        for c, case in enumerate(cases):
            solution = solve_case(case)
            f.write("Case #{}:\n".format(c+1))
            for line in solution:
                f.write("".join(line) + "\n")

solve()
#solve_case(["?A??", "?B??", "?C??"])
