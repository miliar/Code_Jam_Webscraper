# flip pancakes

def solution(test_case):
    tc_parsed = test_case.split(' ')
    pancakes = list(tc_parsed[0])
    original_pancakes = list(tc_parsed[0])
    flipper_size = int(tc_parsed[1])
    flips = 0

    # stop on repeat
    while True:
        # print "pancakes are currently {}".format(pancakes)
        try:
            pancakes_first_blank = pancakes.index('-')
        except ValueError:
            # no more blanks
            return flips

        if pancakes_first_blank + flipper_size - 1 > len(pancakes) - 1:
            # print 'first blank is {}'.format(pancakes_first_blank + flipper_size)
            # print 'len pancakes-1 is {}'.format(len(pancakes) - 1)
            return 'IMPOSSIBLE'

        # flip from first blank
        for p in xrange(pancakes_first_blank, pancakes_first_blank + flipper_size):
            # print p
            k = pancakes[p]
            if k == '-':
                np = '+'
            else:
                np = '-'

            pancakes[p] = np

        # if original pancake orientation after flip
        # then impossible
        if pancakes == original_pancakes:
            return 'IMPOSSIBLE'

        flips += 1

test_cases = int(raw_input())

solutions = []
for i in xrange(0, test_cases):
    test_case = raw_input()
    solutions.append('Case #{}: '.format(i+1) + str(solution(test_case)))

print '\n'.join([str(x) for x in solutions])
