import fileinput

def main():
    case_num = 1
    for line in fileinput.input():
        if fileinput.isfirstline():
            continue
        C, F, X = [float(f) for f in line.strip().split(' ')]
        t = find_min_time(C, F, X)
        print ''.join(['Case #', str(case_num), ':', ' ', str(t)])
        case_num += 1

def find_min_time(C, F, X):
    # rate at which we're given cookies for doing nothing.
    free_cookie_rate = 2.0
    if X < C:
        # we'll be done before we even have enough cookies
        # to buy the first farm.
        return X/free_cookie_rate
    else:
        farm_payoff = C / F # time for a farm to pay off
        # the next time-step we'll need to make a decision
        decision_time = C / free_cookie_rate
        num_farms = 0.0 # number of farms owned
        while True:
            # time yet to go without (w/o) buying a farm
            ttfwof = (X - C) / (free_cookie_rate + (num_farms * F))
            if ttfwof < farm_payoff:
                # best to not buy another farm
                return decision_time + ttfwof
            else:
                num_farms += 1
                decision_time += C / (free_cookie_rate + (num_farms * F))


if __name__ == "__main__":
    main()
