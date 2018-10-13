import fileinput

def output(test_case, result):
    print 'Case #{0}: {1}'.format(test_case + 1, result)

if __name__ == '__main__':
    problem_file = fileinput.input()
    num_test_cases = int(problem_file.readline())

    for test_case in xrange(num_test_cases):
        farm_cost, farm_rate, win_count = (float(arg) for arg in problem_file.readline().split())
        cookie_rate   = 2.0
        total_cookies = 0.0
        seconds       = 0.0

        while(True):
            if ((win_count / cookie_rate) >
                    ((farm_cost / cookie_rate) + (win_count / (cookie_rate + farm_rate)))):
                seconds     = seconds + (farm_cost / cookie_rate)
                cookie_rate = cookie_rate + farm_rate
            else:
                seconds = seconds + (win_count / cookie_rate)
                output(test_case, round(seconds, 7))
                break