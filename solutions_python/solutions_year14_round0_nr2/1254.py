# Cookie Clicker Alpha
# Submitted for Google Code Jam 2014
# Author: Johnathon Beaumier


def time_at_rate(rate, goal):
    return 1.0 * goal / rate


def total_time(cost, production, win_amount):
    """ Solves one test case """

    rate = 2
    result = 0
    while True:
        farm_time = time_at_rate(rate, cost)
        current_time = time_at_rate(rate, win_amount)
        increased_time = farm_time + time_at_rate(rate + production, win_amount)
        if current_time > increased_time:
            result += farm_time
        else:
            result += current_time
            break
        rate += production
    return result


def solve():
    """ Runs through each test case and gives the output """

    file_name = "b"
    file = open(file_name + ".out", "w")
    for i, test_case in enumerate(test_cases(file_name + ".in")):
        c = float(test_case[0])
        f = float(test_case[1])
        x = float(test_case[2])

        line = "Case #{0}: ".format(i + 1)
        line += str(total_time(c, f, x))
        record(line, file)


def test_cases(file_name):
    """ Collects data for each test case """

    file = open(file_name, "r")
    num_test_cases = int(file.readline())
    results = []
    for __ in range(num_test_cases):
        results.append(file.readline().split())
    return results


def record(string, file):
    print(string)
    file.write(string + "\n")


solve()