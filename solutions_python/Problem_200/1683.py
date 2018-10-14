#!/usr/bin/python3
from pprint import pprint
import numpy as np


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
            content.append(line)
    content = np.array(content).astype('int')
    return content


def solution(num):
    digits = list(reversed([int(d) for d in str(num)]))
    for i in range(len(digits) - 1):
        if digits[i] < digits[i+1]:
            digits[i] = 9
            digits[i + 1] -= 1
            for j in range(i):
                digits[j] = 9
    digits = int(''.join(list(reversed([str(i) for i in digits]))))
    return digits


def calculate(data):
    result = []
    index = 0
    for i in data:
        single_solution = solution(i)
        line = 'Case #' + str(index+1) + ': ' + str(single_solution) + '\n'
        result.append(line)
        index += 1
    return result


def write(result, output_file):
    with open(output_file, 'w') as f:
        for line in result:
            f.write(line)


if __name__ == '__main__':
    input_data = read_in('B-large.in')
    results = calculate(input_data)
    write(results, 'B-large.out')


