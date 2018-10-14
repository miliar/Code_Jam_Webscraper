#note: digits of fair and sqare numbers seem to always be 0,1,2

from itertools import count, product

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def digits(n):
    return map(int, str(n))

def base3_count():
    yield [1]
    yield [2]
    for c in count(1):
        for p in product([0, 1, 2], repeat=c):
            yield [1] + list(p)

        for p in product([0, 1, 2], repeat=c):
            yield [2] + list(p)


def palindrome_digits(n):
    odd = n % 2 == 1

    for ii in count(1):
        d = digits(ii)

        if 2 * len(d) < n:
            nums = d + [0] * (n - 2 * len(d)) + d[::-1]
        elif odd:
            nums = d + d[::-1][1:]
        else:
            nums = d + d[::-1]

        if len(nums) > n:
            return

        yield int(''.join(map(str, nums)))

def palindromes(start, stop):
    start_digits = len(str(start))
    stop_digits = len(str(stop))

    for n in range(start_digits, stop_digits + 1):
        for p in palindrome_digits(n):
            assert is_palindrome(p)
            if p < start:
                continue
            #if p > stop:
            #    return
            yield p


def fair_square(start, stop):
    result = 0

    i = int(start ** (0.5)) - 1
    j = int(stop ** (0.5)) + 1

    for p in palindromes(i, j):
        p2 = p ** 2
        if p2 >= start and p2 <= stop and is_palindrome(p2):
            result += 1

    return result


def test():
    assert fair_square(1, 4) == 2, fair_square(1, 4)
    assert fair_square(10, 120) == 0
    assert fair_square(100, 1000) == 2
    #print fair_square(1, 10**50)

def main(fname):
    data = [d.strip() for d in open(fname + '.in')]
    out = open(fname + '.out', 'w')

    T = int(data[0])
    data = data[1:]
    for i in range(T):
        lo, hi = map(int, data[i].split())
        result = fair_square(lo, hi)
        print "Case #%i: %i" % (i+1, result)
        out.write("Case #%i: %i\n" % (i+1, result))

    out.close()

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
