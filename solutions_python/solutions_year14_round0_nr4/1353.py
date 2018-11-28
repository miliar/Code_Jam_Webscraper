def dWar(n, k):
    N = len(n)
    score = 0
    for i in range(N):
        if n[0] < k[0]:
            n = n[1:]
            k = k[:-1]
        else:
            n = n[1:]
            k = k[1:]
            score += 1
    return score


def War(n, k):
    N = len(n)
    n = sorted(n, reverse=True)
    k = sorted(k, reverse=True)
    score = 0
    for i in range(N):
        if n[0] > k[0]:
            n = n[1:]
            k = k[:-1]
            score += 1
        else:
            n = n[1:]
            k = k[1:]
    return score


def load():
    raw_input()
    n = [float(f) for f in raw_input().split(' ')]
    k = [float(f) for f in raw_input().split(' ')]
    return sorted(n), sorted(k)

T = int(raw_input())
for t in range(1, T + 1):
    n, k = load()
    print "Case #{}: {} {}".format(t, dWar(n, k), War(n, k))
