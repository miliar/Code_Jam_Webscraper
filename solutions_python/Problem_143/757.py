import fileinput, itertools

def output(test_case, result):
    print 'Case #{0}: {1}'.format(test_case + 1, result)

if __name__ == '__main__':
    problem_file = fileinput.input()
    num_test_cases = int(problem_file.readline())

    for test_case in xrange(num_test_cases):
        old_machine, new_machine, catalina = (long(arg) for arg in problem_file.readline().split())

        output(
            test_case,
            sum(
                itertools.imap(
                    lambda x: x[0] & x[1] < catalina,
                    itertools.product(xrange(old_machine), xrange(new_machine))
                )
            )
        )