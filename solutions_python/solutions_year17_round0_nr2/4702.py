import sys
import itertools


# predicate - function that returns true / false
def is_tidy(k):
    t = [int(d) for d in str(k)]
    # get by tens and do modulo to get number list
    return all([j >= i for i, j in zip(t[:-1], t[1:])])


def greatest_tidy(k):
    while not is_tidy(k):
        k -= 1
    return k

# print is_tidy(111111111111111110)
for i, line in enumerate(sys.stdin):
    if i > 0:
        k = int(line)
        print "Case #{}: {}".format(
            i,
            greatest_tidy(k)
        )
