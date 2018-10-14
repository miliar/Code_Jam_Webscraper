
number_of_tests = int(raw_input())


def possible_best_scores():
    not_surprising = [0 for i in range(31)]
    surprising = [0 for i in range(31)]

    for x in xrange(11):
        for y in xrange(x, 11):
            for z in xrange(y, 11):
                total = x + y + z
                delta = z - x
                if delta < 2:
                    not_surprising[total] = z
                if delta == 2:
                    surprising[total] = z

    return [(ns, max(s, ns)) for i, (ns, s) in enumerate(zip(not_surprising, surprising))]

possible_best_scores = possible_best_scores()


def performed_good():
    data = map(int, raw_input().split())

    number_of_googlers = data[0]
    surprizing_count = data[1]
    points_to_be_good = data[2]
    googlers_totals = data[3:]

    good_results = 0

    for total in sorted(googlers_totals, reverse = True):

        if possible_best_scores[total][0] >= points_to_be_good:
            good_results += 1
        elif possible_best_scores[total][1] >= points_to_be_good and surprizing_count:
            good_results += 1
            surprizing_count -= 1

    return good_results


for test in xrange(number_of_tests):
    print "Case #%s: %s" % (test + 1, performed_good())