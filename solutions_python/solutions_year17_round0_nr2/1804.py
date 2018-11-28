FILENAME = 'b-large.txt'

f = open(FILENAME)


def is_tidy(n):
    return find_untidy_index(n) is None


def find_untidy_index(n):
    string = str(n)
    for i in xrange(1, len(string)):
        if string[-(i + 1)] > string[-i]:
            return i
    return None


def answer(n):
    while True:
        index = find_untidy_index(n)
        if index is None:
            return n
        n -= n % (10 ** index)
        n -= 1


num_cases = int(f.readline())
for case in xrange(1, num_cases + 1):
    n = int(f.readline().strip())
    val = answer(n)
    print 'Case #{}: {}'.format(case, val)
