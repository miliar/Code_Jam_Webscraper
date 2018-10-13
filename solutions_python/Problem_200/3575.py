import os
import time

__author__ = 'ricky'


def make_tidy(num):
    num_str = str(num)
    step = len(str(num_str))
    for i in range(1, step):
        # if 59
        num1 = int(num % 10 ** i / 10 ** (i - 1))  # first 9
        num2 = int(num % 10 ** (i + 1) / 10 ** i)  # second 5
        # print(num2, num1)
        if num1 < num2:
            factor = int(num % 10 ** i) + 1
            num -= factor

    return num


def read_file(input):
    i = 0
    lines = (line.rstrip('\n') for line in open(input))
    for xx in lines:
        i += 1
        if i == 1:
            continue
        res = make_tidy(int(xx))
        yield ('Case #{}: {}'.format(i - 1, res))


if __name__ == '__main__':

    start = time.clock()
    with open('sample-data/B-small-attempt0.out', 'w') as the_file:
        for line in (read_file('sample-data/B-small-attempt0.in')):
            the_file.write(line + os.linesep)
    end = time.clock()
    print("%.2gs" % (end - start))
