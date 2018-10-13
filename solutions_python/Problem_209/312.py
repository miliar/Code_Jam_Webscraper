import math

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N, K = map(int, input().split())
        R, H = [], []
        pancakes = [tuple(map(int, input().split())) for _ in range(N)]
        max_top_surfaces = 0
        surfaces = 0
        for _ in range(K):
            pancakes.sort(key=lambda l: 2 * math.pi * l[1] * l[0] + max(0, math.pi * l[0] * l[0] - max_top_surfaces))
            r, h = pancakes.pop()
            surfaces += 2 * math.pi * h * r + max(0, math.pi * r * r - max_top_surfaces)
            max_top_surfaces = max(max_top_surfaces, math.pi * r * r)
        print("Case #{x}: {y}".format(x=t, y=surfaces))