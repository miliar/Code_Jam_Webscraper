#!/usr/bin/env python3
#coding: utf-8
import sys
import unittest
from io import StringIO

def solve_case(line):
    shymax, shyness_str = line.strip().split()
    shymax = int(shymax)
    if shymax == 0:
        return 0
    people = []
    stand_so_far = 0
    required = 0
    for index, digit in enumerate(shyness_str):
        digit = int(digit)
        if index == 0:
            stand_so_far += digit
            continue
        if digit > 0:
            people.append((index, digit))
    for shyness, number in people:
        if stand_so_far < shyness:
            required += shyness-stand_so_far
            stand_so_far += shyness
        stand_so_far += number

    return required


def solve(inp, outp):
    inp.readline()
    for index, line in enumerate(inp):
        result = solve_case(line)
        outp.write('Case #%d: %d\n' % (index+1, result))
        outp.flush()


test_data = [
'4 11111',
'1 09',
'5 110011',
'0 1',
'5 000009'
]

test_data = '%d\n' % len(test_data) + ''.join(x+'\n' for x in test_data)

test_result = \
'''Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 5
'''

class MagicTest(unittest.TestCase):
    def test_magic_usual(self):
        outp = StringIO()
        #solve(StringIO(test_data), outp)
        solve(open('A-small0.in'), outp)
        self.assertEqual(outp.getvalue(), test_result)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        sys.argv.pop()
        unittest.main()
    else:
        solve(sys.stdin, sys.stdout)
