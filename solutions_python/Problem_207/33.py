NO_SOL = 'IMPOSSIBLE'


def check_exception(counts, special, simple_c, complex_c):
    if counts[complex_c] == 0:
        return False

    if counts[simple_c] < counts[complex_c]:
        print(NO_SOL)
        return True

    if counts[simple_c] == counts[complex_c]:
        nonzero = {k for k, v in counts.items() if v > 0}
        if nonzero == {simple_c, complex_c}:
            print((simple_c + complex_c) * counts[simple_c])
        else:
            print(NO_SOL)
        return True

    special[simple_c] = (simple_c + complex_c) * counts[complex_c] + simple_c
    counts[simple_c] -= counts[complex_c]
    counts[complex_c] = 0
    return False


def get_small_solution(counts):
    items = sorted((v, k) for k, v in counts.items())
    if items[0][0] + items[1][0] < items[2][0]:
        return None

    seps = ['' for i in range(items[2][0])]
    for i in range(items[0][0]):
        seps[i] += items[0][1]
    for i in range(len(seps) - items[1][0], len(seps)):
        seps[i] += items[1][1]
    return ''.join(items[2][1] + sep for sep in seps)


def solve():
    counts = {}
    N, counts['R'], counts['O'], counts['Y'], counts['G'], counts['B'], counts['V'] = map(int, input().split())

    special = {}
    for simple_c, complex_c in ('BO', 'RG', 'YV'):
        if check_exception(counts, special, simple_c, complex_c):
            return

    for ch in 'OGV':
        del counts[ch]
    result = get_small_solution(counts)

    if result is None:
        print(NO_SOL)
        return
    for ch in 'BRY':
        if ch in special:
            result = result.replace(ch, special[ch], 1)
    print(result)


def main():
    T = int(input())
    for no in range(1, T + 1):
        print('Case #{}: '.format(no), end='')
        solve()


main()
