import sys

def ok(pattern):
    for c in pattern:
        if c != '+':
            return False
    return True

def inversed(c):
    if c == '+':
        return '-'
    return '+'

def flip(pattern, start, K):
    ret = ''
    l = len(pattern)
    for i in range(0, l):
        if i in range(start, start + K):
            ret += inversed(pattern[i])
        else:
            ret += pattern[i]

    return ret

def solve(pattern, K):
    table = {}
    table[pattern] = 0
    queue = [pattern]
    m = -1
    while len(queue) > 0:
        p = queue[0]
        del queue[0]
        current = table[p]
        if m >= 0 and current >= m:
            break

        if ok(p):
            if m < 0 or current < m:
                m = current
            continue

        for i in range(0, len(pattern) - K + 1):
            flipped = flip(p, i, K)
            if flipped not in table:
                table[flipped] = current + 1
            elif table[flipped] > current + 1:
                table[flipped] = current + 1
            else:
                continue
            queue.append(flipped)

        queue = sorted(queue, key=lambda p: table[p])

    if m >= 0:
        return m
    return 'IMPOSSIBLE'

T = int(sys.stdin.readline())
for i in range(0, T):
    segments = sys.stdin.readline().split(' ')
    pattern = segments[0]
    K = int(segments[1])
    print('Case #%d: %s' % (i + 1, str(solve(pattern, K))))

