#!/home/balazs/anaconda2/bin/python

from itertools import dropwhile


def prev_tidy_slow(n):
    while n > 1:
        l = list(str(n))
        if l == sorted(l):
            break
        n -= 1
    return n


def prev_tidy(s):
    return ''.join(dropwhile(lambda x: x == '0', prev_tidy0(list(s))))


def prev_tidy0(l):
    for i in xrange(len(l) - 1):
        # print i, l[i], l[i+1], len(l)-i-1
        if l[i] > l[i+1]:
            return prev_tidy0(l[:i] + [str(int(l[i])-1)] + ['9'] * (len(l)-i-1))
    return l


t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input()
    print "Case #{}: {}".format(i, prev_tidy(n))

# import random
# for _ in xrange(100):
#     n = ''.join(map(lambda x: str(random.randint(0, 9)), xrange(18)))
#     print n, prev_tidy(n)

# 111111111111111110
# 111111111111111109
#  99999999999999999

# 224388
# 223999

# 1110
#  999