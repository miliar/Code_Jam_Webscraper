def handle_case(case_num, c, f, x, t=0, farms=0):
    """
    c: Cost of a cookie farm
    f: Number of cookies the farm produces per sec
    x: Target number of cookies

    Return the number of seconds it takes to get to x
    with the optimal strategy
    """
    while True:
        cookies_per_sec = 2 + (farms * f)
        time_to_goal = x / cookies_per_sec
        time_to_farm = c / cookies_per_sec
        time_with_new_farm = time_to_farm + (x / (cookies_per_sec + f))
        if time_to_farm >= time_to_goal or time_with_new_farm >= time_to_goal:
            print "Case #%d: %.7f" % (case_num, t + time_to_goal)
            return
        else:  # Buy a farm
            t += time_to_farm
            farms += 1


def main():
    n_cases = int(raw_input())
    for case in range(1, n_cases + 1):
        c, f, x = (float(x) for x in raw_input().split())
        handle_case(case, c, f, x)

if __name__ == '__main__':
    main()
