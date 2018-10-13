from collections import deque
import sys


def flip(X, k):
    q = deque()
    c = 0
    for i in range(len(X)):
        if len(q) != 0:
            if q[0] == i:
                q.popleft()
        sign = 1 if len(q) % 2 == 0 \
                 else -1
        X[i] *= sign
        if X[i] == -1:
            if i <= len(X) - k:
                X[i] = 1
                q.append(i + k)
                c += 1
            else:
                return None
    assert all(x == 1 for x in X)
    return c


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        next(f)  # skip header

        for i, line in enumerate(f):
            X, k = line.strip().split(' ')
            X = [1 if x == '+' else -1
                 for x in X]
            k = int(k)
            result = flip(X, k)
            print('Case #{}: {}'.format(i + 1, str(result) if result is not None
                                               else 'IMPOSSIBLE'))
