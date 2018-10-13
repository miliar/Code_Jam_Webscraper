
def is_tidy(n):
    digits = [int(c) for c in str(n)]
    return digits == sorted(digits)


def last_tidy_slow(n):
    while True:
        if is_tidy(n):
            return n
        n -= 1


def last_tidy_fast(n):

    def reduce_once(n):
        res = []
        digits = [int(c) for c in str(n)]
        n_digits = len(digits)
        for i in range(n_digits):
            a = digits[i]
            if i+1 < n_digits:
                b = digits[i+1]
                if b < a:
                    if not (a-1 == 0 and res == []):
                        res.append(a-1)
                    res.extend([9] * (n_digits-i-1))
                    break
                else:
                    res.append(a)
            else:
                res.append(a)
        return int(''.join(str(d) for d in res))

    while True:
        prev, n = n, reduce_once(n)
        if prev == n:
            return n


if __name__ == '__main__':

    import sys

    T = int(sys.stdin.readline())

    for i, line in enumerate(sys.stdin):
        N = int(line)
        print "Case #{}: {}".format(i+1, last_tidy_fast(N))
        #assert last_tidy_fast(N) == last_tidy_slow(N)

