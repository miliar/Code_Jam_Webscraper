import sys

sys.stdin = open('cookiesL.in', 'r')
sys.stdout = open('cookies.out', 'w')

def main():
    total_cases = int(input())
    for case_number in range(1, total_cases + 1):
        print('Case #%d: %.7f' % (case_number, solve()))

def solve():
    farm_cost, farm_cookie_rate, win_count = [float(i) for i in input().split()]
    farms = 0
    total_farm_time_cost = 0
    last_time_cost = win_count / 2.0
    while True:
        # calculate cookie rate
        cookie_rate = 2.0 + farms*farm_cookie_rate

        # find how much time to get farm
        farm_time_cost = farm_cost / cookie_rate 

        # increment farms
        farms += 1

        # update cookie_rate
        cookie_rate += farm_cookie_rate

        # update total farm_cost
        total_farm_time_cost += farm_time_cost

        # check how much time it takes
        current_time_cost = win_count / cookie_rate + total_farm_time_cost
        # check if adding a farm has increased time cost
        if current_time_cost > last_time_cost:
            return last_time_cost
        else:
            last_time_cost = current_time_cost

if __name__ == '__main__':
    main()