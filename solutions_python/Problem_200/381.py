def check(s):
    i = s[0]
    for idx, j in enumerate(s[1:], 1):
        if j < i:
            return False, idx
        i = j
    return True, 0


def solution(n):
    s = [int(i) for i in n]
    while True:
        is_ok, idx = check(s)
        if is_ok:
            break
        s[idx - 1] -= 1
        for i, _ in enumerate(s[idx:]):
            s[idx + i] = 9
        while s[0] == 0:
            s = s[1:]
    return ''.join(map(str, s))


n_tests = int(input())
for i in range(1, n_tests + 1):
    n = str(int(input()))
    print('Case #{}: {}'.format(i, solution(n)))