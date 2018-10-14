# -*- coding: utf-8 -*-
# !python3
import math

__author__ = 'lostcoaster'


class InputFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.test_count = 0

    def __iter__(self):
        with open(self.filename) as file:
            self.test_count = int(file.readline().strip())
            for test_i in range(1, self.test_count+1):
                file.readline()  # skip the count, we don't need it.
                plate_data = [int(n) for n in file.readline().strip().split(' ')]
                yield plate_data


class AnswerFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.case_num = 0

    def put(self, answer):
        self.case_num += 1
        with open(self.filename, 'a') as file:
            to_write = 'Case #{}: {}\n'.format(self.case_num, str(answer))
            print(to_write)
            file.write(to_write)


# 1000x1000 is not such big thing, just brute force :)
def solve(array):
    return min(target_function(i, array) for i in range(1, max(array)+1))

# Well when you have a real big thing, it can still be solved with the target function given.
# But I have no time to mathematically prove the correctness of the functions :P


def target_function(x, array):
    return sum(math.ceil(n/x)-1 for n in array) + x
    # explain : x is the MAX size plate AFTER all the moving
    # so for every plate, ceil(n/x)-1 moves must be done to move pancakes to empty plates
    # each move also take 1 pancake time. and finally, time of eating x pancakes is added

if __name__ == '__main__':
    input_file = InputFile('b_b.in')
    answers = AnswerFile('b_b.out')
    for data in input_file:
        answers.put(solve(data))