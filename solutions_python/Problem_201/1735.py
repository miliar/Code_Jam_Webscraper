FILENAME = 'c-small.txt'

f = open(FILENAME)


def is_tidy(n):
    return find_untidy_index(n) is None


def find_untidy_index(n):
    string = str(n)
    for i in xrange(1, len(string)):
        if string[-(i + 1)] > string[-i]:
            return i
    return None


def answer(n, k):
    stalls = [True] + [False] * n + [True]
    for person in xrange(k):
        taken_stalls = [i for i in xrange(n + 2) if stalls[i]]
        distances = []
        for i in xrange(len(taken_stalls) - 1):
            stall1 = taken_stalls[i]
            stall2 = taken_stalls[i + 1]
            distance = (stall2 - stall1 - 1)
            if distance == 0:
                continue
            l = (distance - 1) / 2
            r = distance - l - 1
            distances.append((l, r, -(stall1 + l + 1)))
        (l, r, index) = max(distances)
        stalls[-index] = True
    return max(l, r), min(l, r)


num_cases = int(f.readline())
for case in xrange(1, num_cases + 1):
    n, k = [int(x) for x in f.readline().split()]
    val = answer(n, k)
    print 'Case #{}: {} {}'.format(case, val[0], val[1])
