#!/usr/local/bin/pypy
# run with PyPy 2.6.1

def read_strings():
    return raw_input().strip().split(' ')

def read_ints():
    return [int(x) for x in read_strings()]

test_count, = read_ints()
for test in xrange(1, test_count + 1):
    s, k = read_strings()
    s = [c == '+' for c in s]
    k = int(k)
    swap_count = 0
    for i in xrange(len(s) - k + 1):
        if not s[i]:
            swap_count += 1
            for j in xrange(i, i + k):
                s[j] = not s[j]
    if not all(s):
        ans = 'IMPOSSIBLE'
    else:
        ans = swap_count
    print 'Case #{}: {}'.format(test, ans)
