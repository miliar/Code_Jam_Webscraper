#score_thresholds = {}
#
#for i in range(11):
#    suprising_part = i-2
#    if suprising_part < 0:
#        suprising_part = 0
#    min_surprising = i + 2*suprising_part
#
#    non_surprising_part = i-1
#    if non_surprising_part < 0:
#        non_surprising_part = 0
#
#    min_non_surprsing = i + 2*non_surprising_part
#    score_thresholds[i] = (min_surprising, min_non_surprsing)

score_thresholds = {0: (0, 0), 1: (1, 1), 2: (2, 4), 3: (5, 7), 4: (8, 10), 5: (11, 13), 6: (14, 16), 7: (17, 19), 8: (20, 22), 9: (23, 25), 10: (26, 28)}

def process(s):
    line_as_ints = [int(elem) for elem in s.split()]
    n, s, b = line_as_ints[0:3]
    scores = line_as_ints[3:]

    at_least_b_no_surprises = 0
    at_least_b_with_surprises = 0
    for score in scores:
        if score >= score_thresholds[b][1]:
            at_least_b_no_surprises += 1
        elif score >= score_thresholds[b][0]:
            at_least_b_with_surprises += 1

    return at_least_b_no_surprises + min(at_least_b_with_surprises, s)

#print process('3 1 5 15 13 11')
#print process('3 0 8 23 22 21')
#print process('2 1 1 8 0')
#print process('6 2 8 29 20 8 18 18 21')
#
number_of_cases = int(raw_input())
for case_number in xrange(1, number_of_cases+1):
    s = raw_input()

    result = process(s)

    print "Case #%d: %s" % (case_number, result)
    case_number += 1