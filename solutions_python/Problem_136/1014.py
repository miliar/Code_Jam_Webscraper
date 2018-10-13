def solve_case(case):
    """
    Repeatedly compare the time it would take to get to X cookies
    by just waiting with the time it takes if you purchase one more
    cookie farm. This is sufficient since the time will monotonically
    decrease until we reach the shortest time, after which it will
    monotonically increase again, so to find the optimum we simply
    need to loop until it would start increasing.
    """

    C, F, X = case
    rate = 2.0
    time_offset = 0.0

    while True:
        # Get the current time to reach X
        current_time = X/rate

        # See how long it would take if we purchased a farm
        farm_time = C/rate
        new_time = farm_time + X/(rate + F)

        # If the time is faster, increase our rate
        if new_time < current_time:
            rate += F
            time_offset += farm_time
        else:
            # We found the optimum; return it
            return time_offset + current_time



def parse_cases(f):
    """
    Yields a series of (C, F, X) suitable for passing to solve_case.
    """

    cases = int(f.readline())
    for i in xrange(cases):
        yield map(float, f.readline().split())


if __name__ == "__main__":
    import sys
    for i, case in enumerate(parse_cases(sys.stdin)):
        print "Case #{}: {:.7f}".format(i+1, solve_case(case))