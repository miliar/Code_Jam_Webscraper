import sys

__author__ = 'Oles Savluk'

def solve(num):
    ns = [int(v) for v in num]
    leftmost = it = len(ns) - 1
    for it in range(len(ns) - 1, 0, -1):
        if (ns[it] < ns[it - 1]):
            ns[it - 1] = ns[it - 1] - 1
            leftmost = it - 1
        it = it - 1

    start = 0 if ns[0] > 0 else 1
    res = ns[start:leftmost+1] + [9] * (len(ns) - leftmost - 1)

    return ''.join(str(v) for v in res)

# assert solve('1') == '1'
# assert solve('123') == '123'

# assert solve('132') == '129'
# assert solve('1000') == '999'
# assert solve('111111111111111110') == '99999999999999999'

if __name__ == '__main__':
    lines = sys.stdin.readlines()

    T = int(lines[0].strip())
    it = 1
    for i in range(T):
        N = lines[it].strip()
        it += 1
        print('Case #{}: {}'.format(i + 1, solve(N)))





