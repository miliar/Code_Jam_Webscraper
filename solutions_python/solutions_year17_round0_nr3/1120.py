def solve():
    n, k = [int(w) for w in input().split()]
    return rec(n, k)

def rec(n, k):
    if k == 1:
        if n%2 == 0:
            return n/2, n/2-1
        else:
            return (n-1)/2, (n-1)/2
    '''
    if k == 2:
            return rec(n//2, 1)
    '''
    if n%2 == 1:
        return rec(n//2, k//2)
    if k%2 == 1:
        return rec(n//2-1, k//2)
    return rec(n//2, k//2)

T = int(input())
for t in range(1, T + 1):
    sol = solve()
    print('Case #%d: %d %d' % (t, sol[0], sol[1]))

