import bisect, fileinput

def output(test_case, result):
    print 'Case #{0}: {1}'.format(test_case + 1, result)

if __name__ == '__main__':
    problem_file = fileinput.input()
    num_test_cases = int(problem_file.readline())

    for test_case in xrange(num_test_cases):
        num_blocks              = int(problem_file.readline())
        naomi_deceitful_blocks  = sorted([float(weight) for weight in problem_file.readline().split()])
        ken_deceitful_blocks    = sorted([float(weight) for weight in problem_file.readline().split()])
        naomi_optimistic_blocks = naomi_deceitful_blocks[:]
        ken_optimistic_blocks   = ken_deceitful_blocks[:]

        naomi_deceitful_wins, naomi_optimistic_wins = 0, 0

        while len(naomi_deceitful_blocks) > 0:
            i = bisect.bisect_right(naomi_deceitful_blocks, ken_deceitful_blocks[0])

            if i != len(naomi_deceitful_blocks):
                naomi_deceitful_blocks.pop(i)
                ken_deceitful_blocks.pop(0)

                naomi_deceitful_wins = naomi_deceitful_wins + 1

            else:
                j = bisect.bisect_right(ken_deceitful_blocks, naomi_deceitful_blocks[0])

                naomi_deceitful_blocks.pop(0)
                ken_deceitful_blocks.pop(j)

        for i in xrange(num_blocks - 1, -1, -1):
            j = bisect.bisect_right(ken_optimistic_blocks, naomi_optimistic_blocks[i])

            if j != len(ken_optimistic_blocks):
                naomi_optimistic_blocks.pop()
                ken_optimistic_blocks.pop(j)
            else:
                naomi_optimistic_wins = naomi_optimistic_wins + 1
                naomi_optimistic_blocks.pop()
                ken_optimistic_blocks.pop(0)

        output(test_case, '{0} {1}'.format(naomi_deceitful_wins, naomi_optimistic_wins))