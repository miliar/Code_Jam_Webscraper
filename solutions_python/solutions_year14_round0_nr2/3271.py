def initialize(fname):
    # open
    with open(fname) as f:
        lines = f.readlines()

    # clean
    for i, line in enumerate(lines):
        lines[i] = [float(n) for n in line.split()]
        if len(lines[i]) == 1:
            lines[i] = int(lines[i][0])

    # parse
    NUM_TESTS = lines.pop(0)

    return lines

def finalize(answers):
    for test_num, answer in enumerate(answers, 1):
        print('Case #{}: {}'.format(test_num, answer))

def process_test(test):
    c, f, x = test
    farm_cost, farm_boost, cookies_left = c, f, x
    time = 0.0
    cookies_per_second = 2.0

    while True:
        time_to_win = cookies_left / cookies_per_second
        time_to_buy = farm_cost / cookies_per_second
        time_if_bought = cookies_left / (cookies_per_second + farm_boost)

        if time_to_win <= time_to_buy + time_if_bought:
            time += time_to_win
            return round(time, 7)

        time += time_to_buy
        cookies_per_second += farm_boost

def main(fname='B-sample.in'):
    tests = initialize(fname)
    answers = [process_test(t) for t in tests]
    finalize(answers)

if __name__ == '__main__':
    import sys
    fname = sys.argv[1]
    main(fname)
