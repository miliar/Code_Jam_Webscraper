# tidy numbers

def solution(upper_bound):
    last_tidy_num = 0

    for n in xrange(1, upper_bound + 1):
        last_num = 0
        broken = False

        str_n = str(n)
        for k in str_n:
            k = int(k)
            if (k >= last_num):
                last_num = k
                continue

            broken = True
            break

        if not broken:
            # if loop continued until the end,
            # then the number is "tidy"
            last_tidy_num = n

    return last_tidy_num


test_cases = int(raw_input())

solutions = []
for i in xrange(0, test_cases):
    test_case = int(raw_input())
    solutions.append('Case #{}: '.format(i+1) + str(solution(test_case)))

print '\n'.join([str(x) for x in solutions])
