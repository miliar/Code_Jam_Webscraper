from __future__ import print_function
import sys


def read_input(f):
    T = int(f.readline().strip())

    for i in xrange(T):
        yield [float(val) for val in f.readline().strip().split(" ")]


def check_case(case):
    farm_cost, farm_rate, target = case
    current_max_rate = 2.0
    current_min_time = target / current_max_rate
    # compare to building one farm
    farm_building_time = (farm_cost / current_max_rate)
    new_time = (farm_building_time +
                (target / (current_max_rate + farm_rate)))
    while new_time < current_min_time:
        # add the time to build the number of farms in the new_rate to
        # the time to complete at the new rate
        current_min_time = new_time
        current_max_rate += farm_rate
        # add the time to build the next farm
        farm_building_time += farm_cost / current_max_rate
        new_time = (farm_building_time +
                    (target / (current_max_rate + farm_rate)))
    return current_min_time

if __name__ == "__main__":
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            print("Case #" + str(case_no) + ": " + str(check_case(case)))
