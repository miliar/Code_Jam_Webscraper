#!/usr/bin/env python

from StringIO import StringIO
import sys

TEST_INPUT = '''2
5
1 2 3 4 5
3
3 5 6
'''

TEST_OUTPUT = '''Case #1: NO
Case #2: 11
'''

def main(stdin, stdout):
    '''Simple. Patrick is doing an XOR. See if the XOR of the numbers is 0 (an XOR of two equal
    numbers is 0) and if it is, add up all the numbers except the smallest for Sean.
    '''
    number_of_test_cases = int(stdin.next())
    for i in range(1, number_of_test_cases+1):
        stdin.next()
        numbers = [int(n) for n in stdin.next().split()]
        numbers.sort()  # Forgot to sort :/
        xor = 0
        for n in numbers:
            xor = xor^n
        if xor == 0:
            result = sum(numbers[1:])
        else:
            result = 'NO'
        stdout.write('Case #{0}: {1}\n'.format(i, result))

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        output = StringIO()
        main(StringIO(TEST_INPUT), output)
        output.seek(0)
        output = output.read()
        assert output == TEST_OUTPUT, '{0} != {1}'.format(output, TEST_OUTPUT)
        print "OK"
    else:
        main(sys.stdin, sys.stdout)
