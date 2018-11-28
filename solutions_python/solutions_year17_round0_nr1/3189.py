import bitarray as B

T = int(input())


def flips(orig_pan, K):
    happy = B.bitarray([True] * len(orig_pan))

    S = len(orig_pan)
    best_flips = None
    for x in range(2 ** (S - K + 1)):
        pan = B.bitarray([True if x == '+' else False for x in orig_pan])
        num_flips = 0

        for ii in range(S - K + 1):
            if (2 ** ii) & x:
                num_flips += 1
                pan[ii:ii + K] = ~ pan[ii:ii + K]

        if not (happy ^ pan).any():
            if best_flips is None:
                best_flips = num_flips
            else:
                best_flips = min(best_flips, num_flips)

    return best_flips if best_flips is not None else "IMPOSSIBLE"


ii = 0
while ii < T:
    ii += 1
    pan, K = input().split(' ')
    print('Case #{}: {}'.format(ii, flips(pan, int(K))))
