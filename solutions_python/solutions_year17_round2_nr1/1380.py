import sys


def max_speed(D, H):
    T = [(D - k_i) / s_i for k_i, s_i in H]
    return min([k_i / t + s_i for (k_i, s_i), t in zip(H, T)])


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        T = int(next(f))
        for i in range(T):
            D, N = map(int, next(f).split(' '))
            H = []
            for j in range(N):
                k_i, s_i = map(int, next(f).split(' '))
                H.append((k_i, s_i))
            r = max_speed(D, H)
            print('Case #{}: {}'.format(i + 1, r))
