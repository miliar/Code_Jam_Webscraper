import fileinput

if __name__ == '__main__':
    problem_file = fileinput.input()
    num_test_cases = int(problem_file.readline())

    for test_case in xrange(num_test_cases):
        row_first_grid = int(problem_file.readline()) - 1
        first_grid = [set(problem_file.readline().split()) for row in xrange(4)]

        row_second_grid = int(problem_file.readline()) - 1
        second_grid = [set(problem_file.readline().split()) for row in xrange(4)]

        row_intersection = first_grid[row_first_grid] & second_grid[row_second_grid]
        if len(row_intersection) == 1:
            print 'Case #{0}: {1}'.format(test_case + 1, row_intersection.pop())
        elif len(row_intersection) == 0:
            print 'Case #{0}: {1}'.format(test_case + 1, 'Volunteer cheated!')
        else:
            print 'Case #{0}: {1}'.format(test_case + 1, 'Bad magician!')
