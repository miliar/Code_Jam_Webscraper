#!/usr/bin/env python

def num_to_list(num):
    num_str = str(num)
    digits = [int(i) for i in num_str]
    return digits

def is_tidy(num):
    if num < 10:
        return True

    digits = num_to_list(num)
    
    last = digits[0]
    for i in digits[1:]:
        if i < last:
            return False
        last = i
    return True

def brute_force(num):
    while not is_tidy(num):
        num -= 1
    return num

def calculate(num):
    digits = num_to_list(num)

    new_num = num
    while not is_tidy(new_num):
        for i in range(0, len(digits) - 1):
            if digits[i] > digits[i+1]:
                if digits[i] == 0:
                    digits[i] = 9
                else:
                    digits[i] -= 1
                for j in range(i+1, len(digits)):
                    digits[j] = 9
        new_num = int(''.join([str(i) for i in digits]))
    return new_num

def main():
    lines = []
    with open('B-large.in', mode='r') as input:
        lines = input.readlines()

    with open('B-large.out', mode='w') as output:
        for i, line in enumerate(lines[1:], start=1):
            result = 'Case #{}: {}\n'.format(i, calculate(int(line)))
            output.write(result)

if __name__ == '__main__':
    main()
