def is_tidy(numbers):
    if len(numbers) == 1:
        return True

    i = 0
    while i < len(numbers) - 1:
        if numbers[i] > numbers[i + 1]:
            return False
        i += 1

    return True


def find_longest_tidy(numbers):
    i = len(numbers) - 1
    while i > 0:
        if numbers[i - 1] > numbers[i]:
            break
        i -= 1
    return i


def find_tidy(N):
    n = map(int, list(str(N)))

    if is_tidy(n):
        return N

    while not is_tidy(n):
        i = find_longest_tidy(n)
        n[i - 1] -= 1
        while i < len(n):
            n[i] = 9
            i += 1
    n = map(str, n)
    return int("".join(n))


T = int(raw_input())

for t in xrange(T):
    N = int(raw_input())
    print "Case #%d: %d" % (t + 1, find_tidy(N))
