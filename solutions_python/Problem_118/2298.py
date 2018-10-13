#!/usr/bin/env python

import sys
import math
from multiprocessing import Pool

def main(filename):
    cases = []
    results = {}
    with open(filename, "r") as f:
        no_of_cases = int(f.readline().strip())
        for i in range(no_of_cases):
            lower, upper = f.readline().strip().split(" ")
            cases.append((int(lower), int(upper)))

    with Pool(processes=8) as pool:
        for index, case in enumerate(cases, 1):
            proc = pool.apply_async(no_of_fair_and_square, [case])
            results[index] = proc.get()
    sorted(results)
    with open("{0}_out".format(filename), "w") as f:
        lines = [] 
        for index, case in results.items():
            lines.append("Case #{0}: {1}".format(index, case))
        f.write("\n".join(lines))

def no_of_fair_and_square(case):
    lower, upper = case
    numbers = range(lower, upper + 1)
    results = 0
    palindromes = (number for number in numbers if str(number) == str(number)[::-1])
    for palin in palindromes:
        sqrt = math.sqrt(palin)
        i_sqrt = int(sqrt)
        if sqrt != i_sqrt:
            continue
        sq_str = str(i_sqrt)
        if sq_str != sq_str[::-1]:
            continue
        results += 1
    return results

if __name__ == '__main__':
    main(sys.argv[1])
