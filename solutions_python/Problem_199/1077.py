def solve(s, k):
    s = [x == '+' for x in s]
    c = s.count(False)
    if c == 0:
        return 0
    flip = 0
    for i in range(len(s) - k + 1):
        if s[i]:
            continue
        flip += 1
        for j in range(i, i + k):
            s[j] = not s[j]
    return flip if all(s) else 'IMPOSSIBLE'


def test_solve():
    assert solve('---+-++-', 3) == 3
    assert solve('+++++', 4) == 0
    assert solve('-+-+-', 4) == 'IMPOSSIBLE'


def main():
    T = int(input())
    for i in range(1, T + 1):
        S, K = input().split()
        K = int(K)
        print('Case #{}: {}'.format(i, solve(S, K)))


if __name__ == '__main__':
    main()
