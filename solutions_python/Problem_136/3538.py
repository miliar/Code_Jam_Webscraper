import sys


COOKIES_PER_SEC = 2


def cookie_clicker(c, f, x):
    # c = cost of farm
    # f = boost to CPS farm gives you
    # x = number of cookies needed to win

    # Amount of time with the next level of cookie production vs. amount of
    # time at the current. Once amount of time at current < amount of time at
    # next level, return answer.

    cps = COOKIES_PER_SEC

    wins = [ x / cps ]
    farms = [ c / cps ]
    for i in range(1, 10000):
        new_cps = cps + (i * f)
        wins.append(x / new_cps)
        farms.append(c / new_cps)
        time_cur = sum(farms[:-1]) + wins[-1]
        time_pre = sum(farms[:-2]) + wins[-2]

        if time_pre < time_cur:
            return time_pre


def main():
    with open(sys.argv[1], 'r') as f:
        t = int(f.readline())
        for line_num, line in enumerate(f.readlines()):
            c, f, x = list(map(float, line.split(' ')))
            print('Case #{0}: {1:.7f}'.format(line_num + 1, cookie_clicker(c, f, x)))


if __name__ == '__main__':
    main()
