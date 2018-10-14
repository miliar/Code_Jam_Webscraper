base_rate = 2.0

def calc_time(farm_cost, farm_rate, end_goal):

    def time_to_goal(num_farms, goal):
        return goal / (base_rate + farm_rate * num_farms)

    num_farms = 0
    current_time = 0.0

    while True:
        time_to_end_plain = time_to_goal(num_farms, end_goal)
        time_to_farm = time_to_goal(num_farms, farm_cost)
        time_to_end_with_farm = time_to_farm + time_to_goal(num_farms + 1, end_goal)

        # print(time_to_end_plain, time_to_end_with_farm)

        if time_to_end_plain < time_to_end_with_farm:
            return current_time + time_to_end_plain
        else:
            current_time += time_to_farm
            num_farms += 1


import random

def input_gen(max_farm_cost, max_farm_rate, max_end_goal, max_num_inputs):
    for _ in range(max_num_inputs):
        farm_cost = random.randint(1, max_farm_cost)
        farm_rate = random.randint(1, max_farm_rate)
        end_goal = random.randint(1, max_end_goal)
        yield farm_cost, farm_rate, end_goal

small_input = input_gen(500, 4, 2000, 100)
large_input = input_gen(10000, 100, 100000, 100)


if __name__ == '__main__':

    with open('B-large.in') as f:
        numcases = int(f.readline().strip())
        lines = [[float(element) for element in line.split()] for line in f]

    # lines = list(large_input)
    results = (calc_time(*line) for line in lines)
    outputs = ['Case #{}: {}'.format(i+1, result) for i, result in enumerate(results)]

    with open('output.txt', 'w') as f:
        for output in outputs:
            print(output)
            print(output, file=f)

    with open('input_log.txt', 'w') as f:
        for line in lines:
            print(' '.join(str(e) for e in line), file=f)
