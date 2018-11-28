import sys
memo = {}


def holes(size):
    if size in memo:
        return memo[size]
    if size == 1:
        return {1:1}
    if size == 2:
        return {2:1, 1:1}
    l = holes(size/2)
    r = holes(size - (size/2) - 1)
    res = {size:1}
    for k in l:
        if k not in res:
            res[k] = 0
        res[k] += l[k]
    for k in r:
        if k not in res:
            res[k] = 0
        res[k] += r[k]
    memo[size] = res
    return res

def solve(n,k):
    h = holes(n)
    l = list(h.iteritems())
    l.sort(reverse=True)
    for (sz, count) in l:
        k -= count
        if k <= 0:
            return (sz/2, sz-(sz/2)-1)

def main():
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        [n,k] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
        res = solve(n,k)
        print('Case #{}: {} {}'.format(i+1, res[0], res[1]))


if __name__ == '__main__':
    main()
