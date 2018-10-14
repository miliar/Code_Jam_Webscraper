import copy
import sys

def is_valid_sum(v, denom):
    if v == 0:
        return True

    for c in denom:
        if is_valid_sum(v - c, filter(lambda x: x != c, denom)):
            return True

    return False

def solve_problem(c, v, d):
    denom = copy.copy(d)
    for v in xrange(1, v + 1):
        if v in denom:
            continue

        if is_valid_sum(v, denom):
            continue

        denom.append(v)

    #print v, denom

    return len(denom) - len(d)

if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())

    for i in xrange(1, num_of_cases + 1):
        c, d, v = map(int, sys.stdin.readline().split())
        denom = map(int, sys.stdin.readline().split())
        print "Case #{0}: {1}".format(i, solve_problem(c, v, denom))

