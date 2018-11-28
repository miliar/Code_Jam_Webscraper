import sys

def find_time_to_finish(farm_cost, farm_extra_cookies, win_condition):
    #print('Farm cost: %f' % farm_cost)
    #print('Fast extra cookies: %f' % farm_extra_cookies)
    #print('Win condition: %f' % win_condition)

    base_prod = 2
    farms = 0
    shortest_time_to_finish = -1

    while True:
        extra_time = 0
        for i in range(1, farms + 1):
            production_this_round = base_prod + (i - 1) * farm_extra_cookies
            extra_time += farm_cost / production_this_round

        production_with_all_farms = base_prod + farms * farm_extra_cookies
        time_to_finish = extra_time + win_condition / production_with_all_farms

        if shortest_time_to_finish == -1 or time_to_finish < shortest_time_to_finish:
            shortest_time_to_finish = time_to_finish
        else:
            break

        farms += 1

    return shortest_time_to_finish

def writeline(f, line):
    #print(line)
    f.write('%s\n' % line)

def main():
    if len(sys.argv) != 2:
        print('Usage: %s INPUT_FILENAME' % sys.argv[0])
        return 1

    input_file = sys.argv[1]
    f = file(input_file)

    output_file = input_file[:-3] + ".out"
    out = file(output_file, 'w')

    number_of_test_cases = int(f.readline())

    for case in range(1, number_of_test_cases + 1):
        line = f.readline()
        farm_cost, farm_extra_cookies, win_condition = [
            float(x) for x in line.split(' ')]

        time_to_finish = find_time_to_finish(farm_cost, farm_extra_cookies,
            win_condition)
        writeline(out, 'Case #%d: %.07f' % (case, time_to_finish))

    return 0

if __name__ == '__main__':
    sys.exit(main())

