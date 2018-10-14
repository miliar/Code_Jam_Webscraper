#!/usr/bin/python

def read_input():
    test_cases = int(raw_input())
    numbers = []
    for i in xrange(test_cases):
        numbers.append(int(raw_input()))
    return numbers

def is_tidy(num):
    last_digit = None
    for digit in map(int, str(num)):
        if digit < last_digit:
            return False
        last_digit = digit
    return True

def downgrade(num):
    last_digit = None
    for i, digit in enumerate(map(int, str(num))):
        if digit < last_digit:
            break
        last_digit = digit
    index_to_downgrade = str(num).find(str(last_digit))
    downgraded = map(int, str(num))
    downgraded[index_to_downgrade] -= 1
    for i in xrange(index_to_downgrade+1, len(downgraded)):
        downgraded[i] = 9
    num = int(''.join(map(str, downgraded)))
    return num

def find_last_tidy(num):
    while not is_tidy(num):
        num = downgrade(num)
    return num

inputs = read_input()
for i, case in enumerate(inputs):
    print 'Case #%s: %s' % (i+1, find_last_tidy(case),)
