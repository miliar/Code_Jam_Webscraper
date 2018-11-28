
def cookie_time(farm_cost, farm_rate, cookies_needed):
    rate = 2.0
    time_no_buy = cookies_needed / rate
    farm_time = 0.0
    while True:
        farm_time += farm_cost / rate
        time_buy = farm_time + cookies_needed / (rate + farm_rate)
        if time_buy < time_no_buy:
            time_no_buy = time_buy
            rate += farm_rate
        else:
            return time_no_buy


def solve_case(line):
    C, F, X = map(float, line.split())
    return cookie_time(C, F, X)


def read_input(filename):
    with open(filename, "r") as in_file:
        n_cases = int(in_file.readline().split()[0])
        for case in range(n_cases):
            yield case + 1, solve_case(in_file.readline())

cases = read_input("input.txt")
outfile = open("output.txt", "w+")

for case, result in cases:
    outfile.write("Case #{}: {:.7f}\n".format(case, result))
