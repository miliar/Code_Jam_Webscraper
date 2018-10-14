def argmax(d):
    return max(d, key=d.get)


def check_consistency(arr):
    assert arr[0] != arr[-1]
    assert all(a != b for a, b in zip(arr[:-1], arr[1:]))


def is_consistent(arr):
    if arr[0] == arr[-1]:
        return False
    if any(a == b for a, b in zip(arr[:-1], arr[1:])):
        return False
    return True


def solve_small(R, Y, B):
    if max(R, Y, B) > sum([R, Y, B])/2:
        return "IMPOSSIBLE"

    counts = {'R': R, 'Y': Y, 'B': B}
    last = None
    horses = []
    while any(counts.values()):
        (high, _), (snd, _), _ = sorted(counts.items(), key=lambda x: -x[1])  # sorted([(R, 'R'), (Y, 'Y'), (B, 'B')])
        if high != last:
            choice = high
        else:
            choice = snd

        horses.append(choice)
        counts[choice] -= 1
        last = choice

        # print(horses)
    result = ''.join(horses)

    if not is_consistent(result):
        result = result[:-2] + ''.join(reversed(result[-2:]))

    check_consistency(result)

    return result


T = int(input())

for i in range(T):
    N, R, O, Y, G, B, V = [int(x) for x in input().split(' ')]
    assert N == sum([R, O, Y, G, B, V])
    assert O == G == V == 0
    print('Case #{}: {}'.format(i + 1, solve_small(R, Y, B)))

# print(solve(10, 5, 5))
