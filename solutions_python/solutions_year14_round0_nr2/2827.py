import sys

def calculate_time(farm_cost, farm_rate, target, rate=2.0):
    total_time = 0

    while True:
        time_without_farm = target / rate
        time_to_buy_farm = farm_cost / rate
        time_with_farm = target / (rate + farm_rate) + time_to_buy_farm

        if time_without_farm <= time_with_farm:
            total_time += time_without_farm
            break
        else:
            total_time += time_to_buy_farm
            rate += farm_rate

    return total_time

if __name__ == '__main__':
    num_tests = int(sys.stdin.readline())

    for i in xrange(num_tests):
        farm_cost, farm_rate, target = map(float, sys.stdin.readline().split())

        print 'Case #{}:'.format(i + 1), calculate_time(farm_cost, farm_rate, target)
