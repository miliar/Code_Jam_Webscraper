def flip(ch):
    if ch == '+':
        return '-'
    else:
        return '+'


def solve(seq, n):
    # print(seq, n)
    cnt = 0
    for i in range(len(seq) - n + 1):
        # print(seq[i])
        if seq[i] == '-':
            seq[i:i + n] = map(flip, seq[i:i + n])
            cnt += 1
        # print(seq)
    # print(cnt)
    return cnt if all(ch == '+' for ch in seq) else -1


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        seq, k = input().split()
        seq = list(seq)
        k = int(k)
        ret = min(solve(seq[::], k), solve(seq[::-1], k))
        if ret != -1:
            print(f'Case #{_ + 1}: {ret}')
        else:
            print(f'Case #{_ + 1}: IMPOSSIBLE')
