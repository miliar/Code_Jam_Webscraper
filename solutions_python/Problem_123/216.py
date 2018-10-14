from sys import stdin


def read_int_line():
    return [int(x) for x in stdin.readline().strip().split()]

def solve(a, n, m):
    if a == 1: return n
    k = 0
    while k < n and m[k] < a:
        a += m[k]
        k += 1
    if k >= n: return 0
    a2 = a
    k_inc = 0
    while m[k] >= a2:
        a2 += a2 - 1
        k_inc += 1
    n_left = n - k
    r1 = solve(a2, n_left, m[k:])
    r = min(r1 + k_inc, n_left)
    return r

if __name__ == '__main__':
    T = int(stdin.readline())
    for caseNum in xrange(T):
        (a, n) = read_int_line()
        m = read_int_line()
        m.sort()
        r = solve(a, n, m)
        print 'Case #%d: %d' % (caseNum + 1, r)