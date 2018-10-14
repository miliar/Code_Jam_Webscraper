from decimal import *


def main():
    inp = open("input.txt", "r")
    out = open("output.txt", "w")
    test_count = int(splited_line(inp)[0])
    for x in xrange(1, test_count + 1):
        C, F, X = [float(i) for i in splited_line(inp)]
        a = solve(C, F, X)
        ans = "Case #%s: %.7f\n"
        out.write(ans % (x, a))


def solve(C, F, X):
    initial_speed = 2.0
    farm_count = 0
    min_time = X / (initial_speed + farm_count * F)
    spent_time = 0.0
    while True:
        time_buy = C / (initial_speed + farm_count * F)
        new_time = X / \
            (initial_speed + (farm_count + 1) * F) + time_buy + spent_time
        if new_time < min_time:
            min_time = new_time
            farm_count += 1
            spent_time += time_buy
        else:
            break
    return min_time


def splited_line(f):
    return f.readline().strip('\r\n').split(' ')

if __name__ == '__main__':
    main()
