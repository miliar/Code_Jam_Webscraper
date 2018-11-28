import sys
import itertools

def num_needed(a):
    r = range(1, len(a) + 1)
    s = list(itertools.accumulate(a))
    need = 0
    i = 0
    N = len(s)
    while i < N:
        if s[i] < r[i]:
            d = r[i] - s[i]
            need += d
            j = i
            while j < N:
                s[j] += d
                j += 1
        i += 1

    return need

if __name__ == '__main__':
    lines = """4
    4 11111
    1 09
    5 110011
    0 1""".strip().split('\n')
    lines = sys.stdin.readlines()

    T = int(lines[0].strip())
    test_cases = lines[1:T+1]
    for i, test_case in enumerate(test_cases):
        smax, audience = test_case.strip().split()
        smax = int(smax)
        audience = audience[:smax]
        audience = list(map(int, audience))
        print('Case #{}: {}'.format(i + 1, num_needed(audience)))
