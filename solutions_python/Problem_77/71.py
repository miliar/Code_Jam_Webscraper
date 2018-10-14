#!/usr/bin/env python

from StringIO import StringIO
import sys

TEST_INPUT = '''3
2
2 1
3
1 3 2
4
2 1 4 3
'''

TEST_OUTPUT = '''Case #1: 2.000000
Case #2: 2.000000
Case #3: 4.000000
'''

def main(stdin, stdout):
    '''This is actually a really simple problem. First, we figure out how many elements, P, are already in
    place. Then, the average number times Goro must hit the table to sort the array is N-P=M. The
    reason for this is as follows:

        If there is an array of N elements and P are in place, this is the same as an unsorted array
        of M elements; Goro will always hold down integers that are in place.

        For the remaining M elements, there are M*(M-1)*(M-2)*... = M! different permutations of the
        array. If we consider the first element, e0, of the array, there are (M-1)*(M-2)*... = (M-1)!
        permutations with e0 in place. So, there is an (M-1)!/M! = 1/M chance that e0 will fall in
        place. This reasoning holds for the rest of the elements. So, there is a 1/M chance that any
        element will fall in place, and on average it will take Goro M tries for all elements to fall in
        place (remembering that Goro will hold down any elements once they fall in place).
    '''
    number_of_test_cases = int(stdin.next())

    for i in range(1, number_of_test_cases+1):
        stdin.next()  # Skip the first line of each test case
        array = [int(e) for e in stdin.next().split()]
        sorted_array = array[:]
        sorted_array.sort()

        elements_in_place = sum(1 for (e, f) in zip(array, sorted_array) if e == f)
        elements_not_in_place = len(array) - elements_in_place

        stdout.write('Case #{0}: {1:f}\n'.format(i, elements_not_in_place))

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
