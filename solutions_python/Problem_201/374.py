from collections import defaultdict

def solution(line):
    n, k = [int(i) for i in line.split()]
    d = defaultdict(int)
    d[n] = 1
    while k > 0:
        for i in sorted(d.keys(), reverse=True):
            v = d[i]
            k -= v
            if k <= 0:
                return (i // 2, i // 2 - (i % 2 == 0))
            del d[i]
            if i % 2 == 1:
                d[i//2] += v * 2
            else:
                d[i//2] += v
                d[i//2 - 1] += v
    return (0, 0)


n_tests = int(input())
for i in range(1, n_tests + 1):
    n = input()
    print('Case #{0}: {1[0]} {1[1]}'.format(i, solution(n)))