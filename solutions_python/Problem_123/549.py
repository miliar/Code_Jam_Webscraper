def solve(A, motes):
    if not motes:
        return 0
    m, rest = motes[0], motes[1:]
    min_size = m + 1
    if A >= min_size:
        return solve(A + m, rest)
    else:
        # Try remove
        rem = 1 + solve(A, rest)
        if A == 1:
            return rem
        # Try insert
        add = 0
        x = A
        while x < min_size:
            x = x + x - 1
            add += 1
        add += solve(x + m, rest)
        ans = min(rem, add)
        return ans

def line(f):
    return map(int, f.readline().split())

def main(f):
    (T,) = line(f)
    for i in range(T):
        A, N = line(f)
        motes = line(f)
        assert len(motes) == N
        print('Case #{}: {}'.format(i + 1, solve(A, sorted(motes))))

if __name__ == '__main__':
    import sys
    main(sys.stdin)
