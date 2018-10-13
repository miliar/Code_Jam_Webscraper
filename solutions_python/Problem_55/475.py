from collections import deque

T = int(raw_input())
for case in xrange(1, T + 1):
    coaster = deque()

    R, k, N = map(int, raw_input().split())

    queue = deque(map(int, raw_input().split()))
    assert len(queue) == N

    money = 0
    for ride in xrange(R):
        size = 0
        while queue:
            next = queue[0]
            new_size = size + next
            if new_size > k:
                break
            coaster.append(queue.popleft())
            size = new_size
        money += size

    #    print coaster

        queue.extend(coaster)
        coaster.clear()

    print 'Case #%d: %d' % (case, money)

