def flip(t, K):
    r = ''
    for i in range(K):
        if t[i] == '+':
            r += '-'
        else:
            r += '+'
    return r + t[K:]

def do(pancakes, K):
    t = pancakes
    count = 0
    for i in range(len(pancakes)):
#         print(t)
        if len(t) < K:
            break
        idx = t.find('-')
#         print(idx)
        if idx == -1:
            return count
        elif idx >= len(t)-K+1:
            return 'IMPOSSIBLE'
        t = flip(t[idx:], K)
        count += 1
    return 'IMPOSSIBLE'

T = int(input())
for i in range(1, 1+T):
    line = input().split()
    pancakes = line[0]
    K = int(line[1])
    print('Case #%d: %s' % (i, do(pancakes, K)))
