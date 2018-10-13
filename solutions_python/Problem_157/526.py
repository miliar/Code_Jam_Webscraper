#!/usr/bin/env python
#
# Author: frrp
# Usage: python thisfile.py <input.in >output.out


multiplication = {
    '1': {
        '1': (1, '1'),
        'i': (1, 'i'),
        'j': (1, 'j'),
        'k': (1, 'k')
    },
    'i': {
        '1': (1, 'i'),
        'i': (-1, '1'),
        'j': (1, 'k'),
        'k': (-1, 'j')
    },
    'j': {
        '1': (1, 'j'),
        'i': (-1, 'k'),
        'j': (-1, '1'),
        'k': (1, 'i')
    },
    'k': {
        '1': (1, 'k'),
        'i': (1, 'j'),
        'j': (-1, 'i'),
        'k': (-1, '1')
    }
}

def multiply(A, B):
    sign, sym = multiplication[A[1]][B]
    return A[0] * sign, sym

def print_yes(case):
    print('Case #%d: YES' % (case+1))

def print_no(case):
    print('Case #%d: NO' % (case+1))

def find_letter(M, letter, index, current):
    while index < M * count:
        current = multiply(current, letters[index % count])
        index += 1
        if current[0] == 1 and current[1] == letter:
            return index
    return index

for case in range(int(raw_input())):
    count, repeat = map(int, raw_input().split())
    letters = raw_input()
    current = (1, '1')
    index = 0
    index = find_letter(4, 'i', index, current)
    if 4 * count == index:
        print_no(case)
    else:
        current = (1, '1')
        index = find_letter(8, 'j', index, current)
        if 8 * count == index:
            print_no(case)
        else:
            current = (1, '1')
            index = find_letter(12, 'k', index, current)
            if 12 * count == index:
                print_no(case)
            elif repeat <= (index - 1) // count:
                print_no(case)
            else:
                current = (1, '1')
                remaining = (repeat - 1 - (index - 1) // count) % 4
                while index % count != 0:
                    current = multiply(current, letters[index % count])
                    index += 1
                for i in range(remaining * count):
                    current = multiply(current, letters[index % count])
                    index += 1
                if current[0] == 1 and current[1] == '1':
                    print_yes(case)
                else:
                    print_no(case)

