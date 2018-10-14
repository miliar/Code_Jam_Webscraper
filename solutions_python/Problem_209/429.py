import math
from helpers.logs import Logger
from heapq import nlargest


def input_function():
    data = {}
    data['N'], data['K'] = [int(s) for s in input().split(' ')]
    data['pancakes'] = []
    for i in range(data['N']):
        data['pancakes'].append(tuple(int(s) for s in input().split(' ')))
    return data


def solution_function(test_num, test_input, general_input):
    cur_input = test_input[test_num]
    pancakes = cur_input['pancakes']
    N = cur_input['N']
    K = cur_input['K']
    # index = 0
    # for radius, height in pancakes:
    #     # index, side area, top area
    #     pancakes_data.append((index, radius, height))
    #     index += 1

    pancakes_sorted_by_side = sorted(pancakes,
                                     key=lambda pancake: 2 * math.pi * pancake[
                                         0] * pancake[1])
    pancakes_sorted_by_radius = sorted(pancakes,
                                       key=lambda pancake: -pancake[0])

    side_area_by_radius = [2 * math.pi * pancake[0] * pancake[1] for pancake in
                           pancakes_sorted_by_radius]

    total_areas = []

    for i in range(N - K + 1):
        start_p = pancakes_sorted_by_radius[i]
        total_area = math.pi * start_p[0] ** 2 + 2 * math.pi * start_p[0] * start_p[1]
        for j in nlargest(K - 1, side_area_by_radius[i + 1:]):
            total_area += j
        total_areas.append(total_area)

    print('Case #{}: {}'.format(test_num + 1, max(total_areas)))


logger = Logger(solution_function, input_function)
logger.start()
