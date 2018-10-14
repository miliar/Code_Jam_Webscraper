# -*- coding: utf-8 -*-
# !python3

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
                time_data = [int(n) for n in file.readline().strip().split(' ')]
                yield time_data


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


def solve(data):
    # first method
    interval_estimate = [max(data[i-1] - data[i], 0) for i in range(1, len(data))]
    first_result = sum(interval_estimate)

    # second method
    max_per_10sec = max(interval_estimate)
    second_result = sum(min(max_per_10sec, max_eatable) for max_eatable in data[:-1])

    return '{} {}'.format(first_result, second_result)

if __name__ == '__main__':
    input_file = InputFile('a_b.in')
    answers = AnswerFile('a_b.out')
    for data in input_file:
        answers.put(solve(data))