#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def solve(candy_values):
    xor = 0
    for candy_value in candy_values:
        xor = xor ^ int(candy_value)
    return xor

if __name__ == '__main__':
    with open('C-large.in', encoding='utf-8') as a_in_file:
        test_cases = int(next(a_in_file).rstrip())
        
        for i in range(test_cases):
            num_of_candies = int(next(a_in_file).rstrip())
            candy_values = sorted(next(a_in_file).rstrip().split(), key=int, reverse=True)
            if solve(candy_values):
                with open('C-small-1.out', mode='a', encoding='utf-8') as a_out_file:
                    a_out_file.write('Case #{}: NO\n'.format(i + 1))
            else:
                with open('C-small-1.out', mode='a', encoding='utf-8') as a_out_file:
                    a_out_file.write('Case #{}: {}\n'.format(i + 1, sum([int(elem) for elem in candy_values[:-1]])))