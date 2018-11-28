
def f(n,k):
    if k == 1:
        return n/2, (n-1)/2

    k -= 1
    if n % 2 == 1:
        return f((n-1)/2, (k+1)/2)

    if k % 2 == 0:
        return f(n/2-1, k/2)
    else:
        return f(n/2, (k+1)/2)


num_cases = int(raw_input())
for case in range(num_cases):
    n, k = map(int, raw_input().split())
    ans = f(n,k)
    print 'Case #%d: %d %d' % (case+1, ans[0], ans[1])
