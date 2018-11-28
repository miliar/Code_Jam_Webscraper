def answer(distance, horses):
    # s = d / t
    t = None
    for horse in horses:
        (k, s) = horse
        ht = (distance - k) / s
        if t is None or t < ht:
            t = ht
    return distance / t


T = int(input())
for t in range(1, T + 1):
    (D, N) = map(int, input().split(' '))
    h = []
    for n in range(N):
        (k, s) = map(int, input().split(' '))
        h.append((k, s))
    result = answer(D, h)
    print('Case #' + str(t) + ': ' + str(result))
