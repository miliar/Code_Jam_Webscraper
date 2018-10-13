from collections import deque

T = int(raw_input())

def next_highest(ken, chose):
    for i in range(0, len(ken)):
        if ken[i] > chose:
            return ken[i]
    return ken[0]

def play(n, k):
    score = 0
    n = list(reversed(n))
    k = list(k)
    while n != []:
        chosen = n[0]
        kens = next_highest(k, chosen)
        if kens < chosen:
            score += 1
        n = n[1:]
        k.remove(kens)
    return score

def lie(n, k):
    n = deque(n)
    k = deque(k)
    score = 0
    while len(n) > 0:
        if n[0] > k[0]:
            score += 1
            n.popleft()
            k.popleft()
        else:
            n.popleft()
            k.pop()
    return score
for i in range(1, T + 1):
    N = int(raw_input())
    naomi = map(float, raw_input().split(' '))
    ken = map(float, raw_input().split(' '))
    naomi.sort()
    ken.sort()
    print('Case #%d: %d %d' % (i, lie(naomi, ken), play(naomi, ken)))
