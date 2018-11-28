import StringIO

from ecodejam.input_parser import read_int, set_parsed_input, run_solver, next_line
from fractions import Fraction


def solve(case_index):
    print case_index
    d = Fraction(read_int(), 1)
    n = read_int()
    next_line()

    k = []
    s = []

    for i in xrange(n):
        k.append(Fraction(read_int(), 1))
        s.append(Fraction(read_int(), 1))
        next_line()


    def try_speed(test_speed):
        for i in xrange(n):
            if s[i] >= test_speed:
                continue
            if k[i] >= d:
                continue
            t = k[i] / (test_speed - s[i])
            if t * test_speed < d:
                return False
        return True

    speed_min = Fraction(0, 1)
    t_min = min(Fraction((d - k[i]), s[i]) for i in xrange(n) if k[i] <= d)
    speed_max = max(d / t_min, 10)

    TRESH = 10 ** (-7)

    while speed_max - speed_min > TRESH:
        cur_speed = (speed_min + speed_max) / 2
        if try_speed(cur_speed):
            speed_min = cur_speed
        else:
            speed_max = cur_speed
    # cur_speed = 10

    return "{:.6f}".format(float(cur_speed))


SAMPLE = """
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
"""

if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
