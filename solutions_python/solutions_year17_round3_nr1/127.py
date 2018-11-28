from math import pi

def helper(pancakes, K, index):
    if index < K-1:
        return 0
    heights = sorted([r*h for r, h in pancakes[:index]])
    h = sum(heights[-K+1:]) + pancakes[index][1] * pancakes[index][0] if K > 1 else pancakes[index][1] * pancakes[index][0]
    return pi * (pancakes[index][0]**2 + 2 * h)


def main(index):
    print 'Case #%d:' % index,
    N, K = map(int, raw_input().split())
    pancakes = sorted([map(float, raw_input().split()) for i in xrange(N)])
    m = 0
    for index in xrange(K-1, N):
        M = helper(pancakes, K, index)
        if m < M:
            m = M
    print m

T = int(raw_input())
for i in xrange(1, T+1):
    main(i)
