#!/usr/bin/python

def solve(case_no):
    n, p = map(int, raw_input().split())
    g = map(int, raw_input().split())
    a = map(lambda x: x % p, g)
    ans = a.count(0)
    a = sorted(filter(lambda x: x > 0, a))

    if p == 2:
        ans += (len(a) + 1) // 2

    elif p == 3:
        one = a.count(1)
        two = a.count(2)
        left = max(one, two) - min(one, two)
        ans += min(one, two) + (left + 2) // 3

    elif p == 4:
        one = a.count(1)
        two = a.count(2)
        three = a.count(3)

        ans += two // 2
        left_two = two % 2

        ans += min(one, three)
        left_one = max(one, three) - min(one, three)

        if left_two == 1:
            ans += 1
            left_one = max(left_one - 2, 0)

        ans += (left_one + 3) // 4

    print 'Case #%d: %d' % (case_no, ans)

t = int(raw_input())
for case_no in xrange(1, t+1):
    solve(case_no)
