import sys


def flip(s, offs, k):
    return s[:offs] + ''.join('+' if x == '-' else '-' for x in s[offs:offs+k]) + s[offs+k:]


def solve(line, test_case):
    
    initial, k = line.split()
    k = int(k)
    n = len(initial)
    
    cache = { '+' * n : 0 }
    
    def min_flips(s):
        if s not in cache:
            cache[s] = None
            mf = None
            for i in range(n - k + 1):
                sf = min_flips(flip(s, i, k))
                if (sf is not None) and ((mf is None) or (sf < mf)):
                    mf = sf
            if mf is not None:
                cache[s] = mf + 1
        return cache[s]
    
    mf = min_flips(initial)
    print('Case #{}: {}'.format(test_case, mf if mf is not None else 'IMPOSSIBLE'))


def solve_all(input_file):
    
    with open(input_file) as f:
        for t, l in enumerate(f):
            if (t > 0) and (l.strip() != ''):
                solve(l.strip(), t)


if __name__ == '__main__':
    solve_all(sys.argv[1])