from heapq import heappush, heappop, _heapify_max
from math import ceil
from operator import itemgetter
from sys import argv


def split(spaces):
    result = {}
    # top = heappop(spaces)
    top = spaces[0][0]
    mid = ceil(top / 2.0)
    ls = mid - 1
    rs = top - ls - 1
    result['max'] = max([ls, rs])
    result['min'] = min([ls, rs])

    return result


def compute(n_stalls, n_users, spaces, start):
    result = {}

    for j in range(start, n_users+1):
        result = split(spaces)

        if spaces[0][1] == 1:
            del spaces[0]
        else:
            spaces[0][1] = spaces[0][1] - 1

        if result['max'] != 0:
            added = False
            for idx, v in enumerate(spaces):
                if result['max'] == v[0]:
                    spaces[idx][1] = spaces[idx][1] + 1
                    added = True
                    break

            if not added:
                spaces.append([result['max'], 1])
            # heappush(spaces, result['max'])

        if result['min'] != 0:
            added = False
            for idx, v in enumerate(spaces):
                if result['min'] == v[0]:
                    spaces[idx][1] = spaces[idx][1] + 1
                    added = True
                    break

            if not added:
                spaces.append([result['min'], 1])
            # heappush(spaces, result['min'])

        spaces = sorted(spaces, key=itemgetter(0), reverse=True)
        # print(spaces)
        # _heapify_max(spaces)

    return [result, spaces]


if __name__ == '__main__':
    test_cases = open(argv[1])
    t = int(test_cases.readline())
    inputs = []
    outputs = []

    for i in range(0, t):
        input = test_cases.readline().split(' ')
        n_stalls = int(input[0])
        n_users = int(input[1].replace('\n', ''))
        inputs.append([n_stalls, n_users, i+1])

    inputs = sorted(inputs, key=itemgetter(0, 1))
    heap = []
    prev = [-1, -1, -1]

    for x in inputs:
        if prev[0] != x[0]:
            heap = [[x[0], 1]]
            start = 1
        else:
            start = prev[1] + 1

        out = compute(x[0], x[1], heap, start)
        result = out[0]
        heap = out[1]
        prev = x
        outputs.append([x[2], result['max'], result['min']])

    outputs = sorted(outputs, key=itemgetter(0))

    for out in outputs:
        print(f"Case #{out[0]}: {out[1]} {out[2]}")

    test_cases.close()
