__author__ = 'robertking'


def solve(mtrx):
    return 0

cases = input()
for case in range(1, cases + 1):
    N = input()
    mushrooms = map(int, raw_input().split())
    cnt1 = 0
    max_rate = 0
    for m1, m2 in zip(mushrooms, mushrooms[1:]):
        if m2 < m1:
            cnt1 += m1 - m2
            max_rate = max(m1 - m2, max_rate)
    cnt2 = 0
    for m1 in mushrooms[:-1]:
        cnt2 += min(m1, max_rate)
    cnt2 = max(cnt2, 0)
    print "Case #%d: %d % d" % (case, cnt1, cnt2)


