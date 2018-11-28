# Let's count 0 separately
#
# 1 digit:      9       1, ..., 9
# 2 digits:     9       *1, ..., 99
# 3 digits:     90      *?1, ..., 9?9
# 4 digits:     90      1001, ..., 9999
# 5 digits:     900     10001, ..., 99999

from math import sqrt


def ints(l):
    return [int(w.strip()) for w in l.strip().split()]


def ndigits10(n):
    return len(str(n))


def rev_str(s):
    return ''.join(reversed(s))

def digit(n):
    return chr(ord('0') + n)


DIGITS = [digit(i) for i in range(10)]
EMPTY_PLUS_DIGITS = [''] + DIGITS


def valid_halves(k):
    # print 'valid_halves(%d)' % k
    if k == 0:
        return ['']
    xs = [str(i) for i in range(1, 10)]
    for i in range(2, k+1):
        new_xs = []
        for d in DIGITS:
            for x in xs:
                new_xs.append(d+x)
        xs = new_xs
    return xs


def is_palindrome(n):
    s = str(n)
    hl = len(s) / 2
    for i in range(hl):
        if s[i] != s[-i-1]:
            return False
    return True


def palindromes_up_to_and_including(n):
    xs = []
    max_k = ndigits10(n) / 2
    # print 'max_k = ', max_k
    for k in range(max_k+1):
        # print 'k = ', k
        hs = valid_halves(k)
        # print hs
        for h in hs:
            rh = rev_str(h)
            for d in EMPTY_PLUS_DIGITS:
                s = rh + d + h
                if not s:
                    continue
                x = int(s)
                # print 'x = ', x
                # if x > n:
                #     print 'x > n, x = %d, n = %d' % (x, n)
                #     return xs
                if x <= n:
                    if not is_palindrome(x):
                        print 'Not a palindrome: %s' % x
                    assert is_palindrome(x)
                    xs.append(x)
    return sorted(xs)


def count_fair_and_square_up_to_and_including(n):
    sqrt_n_bound = int(sqrt(n) + 1)
    count = 0
    for sqrt_k in palindromes_up_to_and_including(sqrt_n_bound):
        k = sqrt_k ** 2
        if k <= n and is_palindrome(k):
            count += 1
    return count


def fair_and_square_up_to_and_including(n):
    sqrt_n_bound = int(sqrt(n) + 1)
    res = []
    for sqrt_k in palindromes_up_to_and_including(sqrt_n_bound):
        assert is_palindrome(sqrt_k)
        k = sqrt_k ** 2
        if k <= n and is_palindrome(k):
            res.append(k)
    return res


def comparison_fair_and_square_up_to_and_including(n):
    res = []
    for k in range(n+1):
        sqrt_k = int(sqrt(k)+0.5)
        if sqrt_k ** 2 == k and is_palindrome(k) and is_palindrome(sqrt_k):
            res.append(k)
    return res


MAX_N = 10 ** 16
# MAX_N = 1000000000000000000

FAIR_AND_SQUARE_UP_TO_AND_INCLUDING_MAX_N = fair_and_square_up_to_and_including(MAX_N)

def fast_fair_and_square_up_to_and_including(n):
    count = 0
    for x in FAIR_AND_SQUARE_UP_TO_AND_INCLUDING_MAX_N:
        if x <= n:
            count += 1
        else:
            break
    return count



from sys import argv

in_fname = argv[1]
f = open(in_fname)

T = int(f.readline())
for it in range(T):
    A, B = ints(f.readline())
    count = fast_fair_and_square_up_to_and_including(B) - fast_fair_and_square_up_to_and_including(A-1)
    print 'Case #%d: %d' % (it+1, count)

# print len(FAIR_AND_SQUARE_UP_TO_AND_INCLUDING_MAX_N)


# print is_palindrome(11)
# print is_palindrome(121)
# print is_palindrome(1331)

# for n in range(110):
#     count = count_fair_and_square_up_to_and_including(n)
#     res = fair_and_square_up_to_and_including(n)
#     print 'count(%d) = %d, %s' % (n, count, res)

# xs = fair_and_square_up_to_and_including(1000000000000000000)
# for x in xs:
#     assert is_palindrome(x)
#     assert is_palindrome(int(sqrt(x)))
#     print x
# print 'count = ', len(xs)

# N = 20000
# xs_comp = comparison_fair_and_square_up_to_and_including(n)

# for n in range(N):
#     xs = fair_and_square_up_to_and_including(n)
#     count = count_fair_and_square_up_to_and_including(n)
#     assert len(xs) == count


# print 'xs == xs_comp: ', xs == xs_comp

# for x, cx in zip(xs, xs_comp):
#     print x, cx

# print

# for b in range(10):
#     a = 10 ** b
#     print a, is_palindrome(a)

# print is_palindrome(100)

# for i in range(4):
#     xs = valid_halves(i)
#     for x in xs:
#         print x
#     print

# print palindromes_up_to_and_including(1001)