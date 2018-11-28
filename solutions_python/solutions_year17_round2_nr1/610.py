import sys

T = int(raw_input())

for tc in xrange(1, T + 1):
    D, N = map(int, raw_input().split())
    horses = []

    for i in xrange(N):
        pos, speed = map(int, raw_input().split())
        horses.append((pos, speed))

    horses = sorted(horses)

    maxTime = None
    for pos, speed in reversed(horses):
        time = (D - pos) / (speed * 1.0)
        if maxTime is None or time > maxTime:
            maxTime = time

    ans = D / maxTime

    print "Case #%d: %.6f" % (tc, ans)