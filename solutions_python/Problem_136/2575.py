#!/usr/bin/python3

base_cookie_rate = 2 # per sec

# C = cookie farm cost
# F = cookie farm rate gain
# X = target cookie amount
def solve(C, F, X):
    cur_gain = base_cookie_rate
    cur_time = X / cur_gain

    next_cost = C / cur_gain
    next_gain = cur_gain + F
    next_time = X / next_gain + next_cost

    while cur_time > next_time:
        cur_gain, cur_time = next_gain, next_time

        next_cost += C / cur_gain
        next_gain = cur_gain + F
        next_time = X / next_gain + next_cost

    return cur_time

def main():
    T = int(input())

    for i in range(T):
        C, F, X = [float(rawval) for rawval in input().split()]

        result = solve(C, F, X)

        print('Case #{0}: {1:.7f}'.format(i+1, result))

if __name__ == '__main__':
    main()
