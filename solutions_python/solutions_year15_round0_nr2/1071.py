# Case D = 1 (one pancake)
# Set f(n) = result for  p_1
# f(1) = 1, f(2) = 2, f(3) = 3 -> Just wait
# first interesting case: f(4) = 3
# Divide to 2 2 -> 1 1 -> 0 0
# f(1) = 1
# f(2) = 2
# f(3) = 3
# f(4) = 3  : 4  ->  2 2   --> 0 0
# f(5) = 4  : 5  ->  3 2   --> 0 0
# f(6) = 4  : 6  ->  3 3   --> 0 0
# f(7) = 5  : 7  ->  3 4   --> 0 0
# f(8) = 5  : 8  ->  4 4   --> 0 0
# f(9) = 5  : 9  ->  3 3 3 --> 0 0 0
# f(10) = 6 : 10 ->  4 3 3 --> 0 0
# f(11) = 6 : 11 ->  4 4 3 --> 0 0 0
# f(12) = 6 : 12 ->  4 4 4 --> 0 0 0
# f(13) = 7 : 13 ->  4 4 5


def f(n):
    return 0

# Series A249728
# Given more numbers
# But this is misleading, because in the general case
# we have D > 1 and thus shorter splits may be
# benefical.
# so it seems consider 3 splits from 3^2, 4 splits from 4^2 etc.
# so consider 1 .. math.floor(sqrt(p_i)) splits for each p_i
# the reason is that 16 -> 4 4 4 4 --> 0
# 25 -> 5 5 5 5 5 --> 0, i.e. there the further splits get
# more benefical (possibly)
# order numbers descending i.e. p_1 >= p_2 >= ... >= p_D
# So p_1 split when?
# 9 5 -> 5 5 4 --> 0 0 0, result: 6
# 6 5 -> 5 3 3  -> 3 3 3 3 --> 0 result: 5


def split(n, k):
    val = n / k
    rest = n - val * k
    result = [val] * k
    result[0:rest] = map(lambda x: x + 1, result[0:rest])
    return result


# optimized variant to just calculate the first element
def splitHead(n, k):
    val = n / k
    if val * k < n:
        return val + 1
    else:
        return val
# for large input D <= 1000, p_i <= 1000
# so exhaustive search would be problematic
# but fixing p_1 it is the case that no matter how we
# split the other p_i, the reductions needed on p_1
# will happen on the other p_i
# counts the minutes needed for the configuration

from math import sqrt


def count(pancakes, splitMaxBefore=0):
    if not pancakes:
        return splitMaxBefore

    head = pancakes[0]
    result = head

    for k in range(2, int(sqrt(head)) + 1):
        splitMax = splitHead(head, k)
        reducedPans = filter(lambda n: n > splitMax, pancakes[1:])
        resultSplit = (k-1) + count(reducedPans, max(splitMax, splitMaxBefore))

        if resultSplit < result:
            result = resultSplit

    return result

T = int(raw_input())

for t in xrange(1, T+1):
    D = int(raw_input())
    pi = map(int, raw_input().split())
    pi.sort()
    pi.reverse()  # sorted ascending now
    result = count(pi)
    print "Case #%d: %d" % (t, result)
