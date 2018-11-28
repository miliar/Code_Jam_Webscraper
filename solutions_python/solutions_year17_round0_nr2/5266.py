

def solve(N):
    for i in range(N, 0, -1):
        if [int(c) for c in list(str(i))] == sorted([int(c) for c in list(str(i))]):
            return i
    return 1


if __name__ == "__main__":
    import fileinput

    f = fileinput.input('B-small-attempt0.in')

    """The first line of the input gives the number of test cases,
    T. T test cases follow.
    """

    T = int(f.readline())

    for case in range(1, T + 1):
        N = f.readline()
        solution = solve(int(N))
        print("Case #{0}: {1}".format(case, solution))

