DAY_RATE = 2
MAX_FARMS = 1000000
FARM_COST_ARRAY = [0] * MAX_FARMS

def main():

    f = open('input.in', 'rb')
    solution = open('solution.out', 'wb')
    test_cases = int(f.readline())

    for i in xrange(test_cases):
        line = f.readline()
        # 30.0 1.0 2.0
        line_arr = line.split(' ')
        farm_cost = float(line_arr[0])
        farm_rate = float(line_arr[1])
        target = float(line_arr[2])
        result = solve(farm_cost, farm_rate, target)
        solution.write('Case #{}: {}\n'.format(i + 1, result))


    f.close()
    solution.close()

def solve(farm_cost, farm_rate, target):
    FARM_COST_ARRAY[0] = 0
    for i in xrange(1, MAX_FARMS):
        FARM_COST_ARRAY[i] = FARM_COST_ARRAY[i - 1] + (farm_cost / ((i - 1) * farm_rate + 2))

    cur_min = target / 2
    for i in xrange(1, MAX_FARMS):
        time_to_target = FARM_COST_ARRAY[i] + target / (farm_rate * i + 2)
        if time_to_target < cur_min:
            cur_min = time_to_target
        else:
            break

    return cur_min

if __name__ == "__main__":
    main()