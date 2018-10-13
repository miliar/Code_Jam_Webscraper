def main():
    t = int(input().strip())
    for case in range(1, t + 1):
        d, n = map(int, input().split())
        horses = []
        for _ in range(n):
            k, s = map(int, input().split())
            horses.append((k, s))
        horses.sort()
        arrivals = ((d-k) / s for k, s in horses)
        max_t = max(arrivals)
        max_s = d / max_t
        print('Case #{}: {}'.format(case, max_s))


if __name__ == '__main__':
    main()
