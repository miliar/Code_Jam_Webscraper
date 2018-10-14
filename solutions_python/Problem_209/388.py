from math import pi

T = int(input())

for t in range(T):
    N, K = map(int, input().split())

    pancakes = []
    for n in range(N):
        r, h = map(int, input().split())

        pancakes.append((h * 2 * pi * r, pi * r * r))

    pancakes.sort(key=lambda x: x[1], reverse=True)

    max_surface = 0
    for i in range(len(pancakes)):
        others = sorted(pancakes[i+1:], reverse=True)
        if len(others) < K-1:
            break
        surf = sum(pancakes[i]) + sum(a for a, _ in others[:K-1])
        if surf > max_surface:
            max_surface = surf
    print("Case #{}: {}".format(t+1, max_surface))
