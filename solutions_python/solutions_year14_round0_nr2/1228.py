from __future__ import print_function
from decimal import Decimal

INPUT = "B-large.bin"
OUTPUT = "B-large-result.txt"


def round(fp):
    cookies_rate = Decimal(2)
    time_spent = Decimal(0)
    farm_cost, cookies_burst, target = [Decimal(x) for x in fp.readline().split(' ')]

    actual_cost = time_spent + target / cookies_rate
    with_more_farm = time_spent + farm_cost / cookies_rate + target / (cookies_rate + cookies_burst)

    while actual_cost >= with_more_farm:
        time_spent += farm_cost / cookies_rate
        cookies_rate += cookies_burst
        actual_cost = time_spent + target / cookies_rate
        with_more_farm = time_spent + farm_cost / cookies_rate + target / (cookies_rate + cookies_burst)

    return actual_cost


def solver(filename):
    with open(filename, 'r') as fp:
        cases = int(fp.readline())
        for case in range(cases):
            yield case + 1, round(fp)

if __name__ == "__main__":
    with open(OUTPUT, "wt") as fp:
        for result in solver(INPUT):
            fp.write("Case #%d: %s\n" % (result))
    print("DONE")
