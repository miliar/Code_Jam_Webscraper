def flip(s):
    out_s = ''
    for ch in s:
        out_s += '+' if ch == '-' else '-'
    return out_s


def solve():
    t = int(raw_input())
    for i in range(t):
        s, k = raw_input().split(' ')
        k = int(k)
        flip_count = 0
        size_s = len(s)
        for j in range(size_s - k + 1):
            if s[j] == '-':
                s = s[:j] + flip(s[j:j + k]) + s[j + k:]
                flip_count += 1

        all_flipped = all([ch == '+' for ch in s])
        print 'Case #{}: {}'.format(i + 1, flip_count if all_flipped else 'IMPOSSIBLE')


solve()
