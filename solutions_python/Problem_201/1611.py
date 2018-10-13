#!/usr/bin/python3
from pprint import pprint
import numpy as np
from math import log


def read_in(input_file):
    """
    读取数据
    :param input_file: 
    :return: 
    """
    with open(input_file) as f:
        content = []
        f.readline()
        for line in f:
            content.append(line.split())
    content = np.array(content).astype('int')
    return content


def solution(stalls, persons):
    data = {stalls: 1}
    index = 0
    while True:
        slots = list(sorted(data.keys(), reverse=True))[index]
        times = data[slots]
        first = slots//2
        second = first - (slots + 1) % 2 if first > 0 else 0
        if first in data.keys():
            data[first] += times
        else:
            data[first] = times
        if second in data.keys():
            data[second] += times
        else:
            data[second] = times
        if sum(list(data.values())) >= persons:
            sum_of_person = 0
            for key in sorted(data.keys(), reverse=True):
                sum_of_person += data[key]
                if sum_of_person >= persons:
                    slots = key
                    first = slots // 2
                    second = first - (slots + 1) % 2 if first > 0 else 0
                    return [first, second]
        index += 1


def calculate(data):
    result = []
    index = 1   # case number # 从1 开始
    for i in data:
        print('===========================', i)
        single_solution = solution(i[0], i[1])
        line = 'Case #' + str(index) + ': ' + str(single_solution[0]) + ' ' + str(single_solution[1]) + '\n'
        result.append(line)
        index += 1
    return result


def write(result, output_file):
    with open(output_file, 'w') as f:
        for line in result:
            f.write(line)


if __name__ == '__main__':
    input_data = read_in('C-large.in')
    pprint(input_data)
    results = calculate(input_data)
    write(results, 'C-large.quick')

