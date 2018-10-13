#!/usr/bin/env python
import fileinput

BASE_RATE = 2

def get_time(cookies, cost, goal, rate):
    need = goal - cookies
    return need / rate

if __name__ == "__main__":
    lines = fileinput.input()

    n_cases = int(lines.readline())

    for case in range(1, n_cases + 1):
        time = 0
        cookies = 0
        rate = BASE_RATE

        cost, harvest, goal = [float(i) for i in lines.readline().split()]

        while cookies < goal:
            # (we can assume cookies either 0 or cost)
            next = cost if cost < goal else goal
            if cookies < next:
                # jump to when we have enough money or have won
                cookies = next
                delta = next / rate
                time += delta
            else:
                buy_time = get_time(cookies - cost, cost, goal, rate + harvest)
                wait_time = get_time(cookies, cost, goal, rate)
                if buy_time < wait_time:
                    # locally optimal to purchase a farm
                    # don't need to update time, that'll happen next iteration
                    cookies -= cost
                    rate += harvest
                else:
                    time += wait_time
                    cookies = goal

        print("Case #{}: {}".format(case, time))
