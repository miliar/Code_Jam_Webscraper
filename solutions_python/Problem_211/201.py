import StringIO

from ecodejam.input_parser import read_int, set_parsed_input, run_solver, next_line, read_float


def solve_small1(case_index):
    n = read_int()
    k = read_int()

    assert k == n
    next_line()

    u = read_float()
    next_line()

    p = []

    for i in xrange(n):
        p.append(read_float())

    def try_val(val):
        cost = sum(
            val - i
            for i in p
            if i <= val
        )
        return cost <= u

    start = 0.0
    end = 1.0
    mid = (end + start) / 2

#    while (end - start) >= 10 ** -7:
    for i in xrange(1000):
        mid = (end + start) / 2

        if try_val(mid):
            start = mid
        else:
            end = mid

        # print ">>>>", start, end

    print ">>>", end, start
    newp = [max(i, start) for i in p]
    print newp

    #prob = 1 - reduce(lambda x, y: x * y, [1.0 - i for i in newp], 1.0)
    prob = reduce(lambda x, y: x * y, [i for i in newp], 1.0)
    return "{:07f}".format(prob)

solve = solve_small1


SAMPLE = """
1
50 50
50.0000
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
"""

if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
