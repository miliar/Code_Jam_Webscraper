ans = '0'
def solve(n, s, a, less):
    global ans
    if less:
        allowed = range(int(a[s-1]), 10)
    else:
        allowed = range(int(a[s-1]), int(n[s])+1)
    if not allowed:
        return
    allowed = list(allowed)[::-1]
    #print(allowed, s, a, less)
    if s == len(str(n)) - 1:
        ans = a + str(allowed[0])
        return
    for d in allowed:
        if d < int(n[s]):
            less = True
        solve(n, s+1, a+str(d), less)
        if ans:
            return


def call_solve(n):
    global ans
    n = '0'+str(n)
    ans = ''
    solve(n, 1, '0', False)
    return int(ans)

t = int(input())
for i in range(1, t+1):
    num = int(input())
    print("Case #%d: %d"%(i, call_solve(num)))
