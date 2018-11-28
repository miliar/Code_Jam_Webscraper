

def min_flips(cakes, K):
    flips = 0
    for i in range(len(cakes) - K + 1):
        if not cakes[i]:
            flips += 1
            for j in range(i, i + K):
                cakes[j] = not cakes[j]
    return flips if all(cakes) else -1


def main():
    T = int(input())
    for case in range(1, T + 1):
        cakes, K = input().split()
        f = min_flips([c == '+' for c in cakes], int(K))
        print("Case #{}: {}".format(case, f if f != -1 else 'IMPOSSIBLE'))

if __name__ == '__main__':
    main()
