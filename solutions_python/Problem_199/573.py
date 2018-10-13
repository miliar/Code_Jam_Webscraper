# coding: utf8
# Copyright: MathDecision


def convert(x):
    return [(1 if xx == '+' else -1) for xx in x]


def flip_first(x, k):
    for i in range(k):
        x[i] = -x[i]
    return x


def num_flips(x, k):
    if k > len(x):
        if all([xx == 1 for xx in x]):
            return 0
        else:
            return None
    elif k == len(x):
        if all([xx == 1 for xx in x]):
            return 0
        elif all([xx == -1 for xx in x]):
            return 1
        else:
            return None
    else:
        if x[0] == 1:
            return num_flips(x[1:], k)
        else:
            x = flip_first(x, k)
            rec = num_flips(x[1:], k)
            return 1 + rec if rec is not None else None


if __name__ == '__main__':
    responses = []
    with open('pank2.in', 'r') as f:
        cases = int(f.readline())
        for i in range(cases):
            pan, k = f.readline().split(' ')
            x = convert(pan)
            k = int(k)
            responses.append(num_flips(x, k))
    with open('pank2.out', 'w') as f:
        for i, r in enumerate(responses):
            f.write('Case #{}: {}\n'.format(i + 1, r if r is not None else 'IMPOSSIBLE'))
