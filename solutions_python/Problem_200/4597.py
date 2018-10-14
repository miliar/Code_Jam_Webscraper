import sys

def istidy(n):
    rep = str(n)
    return all(rep[i] <= rep[i + 1] for i in xrange(len(rep) - 1))


def largest_tidy_less_than(n):
    while not istidy(n):
        n -= 1
    return n


def tests():
    assert istidy(0)
    assert not istidy(10)
    assert largest_tidy_less_than(10) == 9
    assert largest_tidy_less_than(132) == 129
    assert largest_tidy_less_than(1000) == 999
    assert largest_tidy_less_than(7) == 7
    #assert largest_tidy_less_than(111111111111111110) == 99999999999999999

if __name__ == "__main__":
    tests()
    with open(sys.argv[1]) as input:
        lines = input.readlines()
    lines = lines[1:]
    for nr, line in enumerate(lines):
        result = largest_tidy_less_than(int(line))
        print "Case #{}: {}".format(nr + 1, result)