INF = 999999999999


def solve():
    d, n = map(int, input().split())
    h = []
    for i in range(n):
        k, s = map(int, input().split())
        h.append([k, s])
    h.sort()
    h.append([d, 0])
    p = [(-1, INF)] * len(h)
    for i in range(len(h) - 1):
        for j in range(i + 1, len(h)):
            if h[j][1] < h[i][1]:
                t = (h[j][0] - h[i][0]) / (h[i][1] - h[j][1])
                dist = h[j][0] + h[j][1] * t
                if p[j][1] > t and dist < d:
                    p[j] = (i, dist)
    i = 0
    t = 0
    cd = h[0][0]
    while i < len(h) - 1:
        j = i + 1
        while j < len(h) and p[j][0] == -1:
            j += 1
        if j < len(h):
            t += (p[j][1] - cd) / h[i][1]
            cd = p[j][1]
        else:
            t += (d - cd) / h[i][1]
            cd = d
        i += 1

    return d / t


def main():
    for t in range(int(input())):
        print('Case #{}: {:.6f}'.format(t + 1, solve()))


if __name__ == '__main__':
    main()
