'''
Created on April 12, 2014

@author: Lior
'''

def solve(first_answer, first_arrangement, second_answer, second_arrangement):
    solutions = first_arrangement[first_answer-1] & second_arrangement[second_answer-1]
    print first_arrangement
    print second_arrangement
    print solutions
    if len(solutions) == 1:
        return solutions.pop()
    if len(solutions) > 1:
        return 'Bad magician!'
    return 'Volunteer cheated!'

def process_files(in_file, out_file):
    num_of_test_cases = int(in_file.next().strip())
    for test_number in xrange(num_of_test_cases):
        first_answer = int(in_file.next().strip())
        first_arrangement = []
        for i in xrange(4):
            first_arrangement.append(set(int(j) for j in in_file.next().split(' ')))
        second_answer = int(in_file.next().strip())
        second_arrangement = []
        for i in xrange(4):
            second_arrangement.append(set(int(j) for j in in_file.next().split(' ')))
        result = solve(first_answer, first_arrangement, second_answer, second_arrangement)
        out_file.write('Case #%d: %s\n' % (test_number+1, result))

if __name__ == '__main__':
    import sys, os
    in_file = sys.argv[1]
    out_file = in_file.replace('.in', '.out')
    with open(in_file, 'rb') as in_file:
        with open(out_file, 'wb') as out_file:
            process_files(in_file, out_file)
