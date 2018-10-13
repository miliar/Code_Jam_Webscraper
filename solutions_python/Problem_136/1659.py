#!/usr/bin/env python

from collections import deque

FILENAME = 'B-small-attempt0.in'

def seconds_to_reach(target, farms, f_factor):
    default_rate = 2.0

    return (target/((farms*f_factor)+default_rate))


def load_dataset(q):
    item = q.popleft()

    result= deque(item.split())

    return result

def load_from_file():
    result = None

    with open(FILENAME) as f:
        result = [line.rstrip('\n') for line in f]

    return deque(result)


def main():
    data = load_from_file()
    number_of_cases = int(data.popleft())

    for x in range(0, number_of_cases):
        case = load_dataset(data)

        farm_price = float(case.popleft())
        f_factor = float(case.popleft())
        win_target = float(case.popleft())

        #print farm_price
        #print f_factor
        #print win_target


        ceiling = win_target / farm_price
        #print ceiling
        winner = {
            'seconds': 9999999,
            'farms': 0
        }

        for i in range(0, int(ceiling)+1):
            tally = 0
            my_farms = 0
            for j in range(0, i):
                tally += seconds_to_reach(farm_price, my_farms, f_factor)
                my_farms += 1

            tally += seconds_to_reach(win_target, my_farms, f_factor)

            if tally < winner['seconds']:
                winner['seconds'] = tally
                winner['farms'] = my_farms

        print "Case #" + str(x+1) + ": " + str('%.7f' % winner['seconds'])




if __name__ == "__main__":
    main()
