from helpers.logs import Logger

def input_function():
    data = {}
    data['D'], data['N'] = [int(s) for s in input().split(' ')]
    data['horses'] = []
    for i in range(data['N']):
        data['horses'].append(tuple(int(s) for s in input().split(' ')))
    return data

def solution_function(test_num, test_input, general_input):
    cur_input = test_input[test_num]
    max_time = max([(cur_input['D'] - horse[0]) / horse[1] for horse in cur_input['horses']])
    print('Case #{}: {}'.format(test_num + 1, cur_input['D'] / max_time))

logger = Logger(solution_function, input_function)
logger.start()