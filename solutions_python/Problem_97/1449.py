#! /usr/bin/env python

import math
import sys
from datetime import datetime


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[1].replace(".in", ".out"), 'w')
for num, row in enumerate(input_file):
    if num == 0:
        continue

    start, end = [int(x) for x in row.split(' ')]
    all_numbers = set([str(x) for x in range(start, end + 1)])
    
    digit_count = len(str(start))
    total_recycled_count = 0
    while all_numbers:
        number = all_numbers.pop()
        recycled_count = 0
        for x in range(0, digit_count - 1):
            number = number[1:] + number[0]
            try:
                all_numbers.remove(number)
                recycled_count += 1
            except Exception as ex:
                pass
        if recycled_count:
            total_recycled_count += nCr(recycled_count + 1, 2)
    
    output_file.write(
        'Case #{0}: {1}\n'.format(num, total_recycled_count)
    )
