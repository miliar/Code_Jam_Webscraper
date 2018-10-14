T = input()
for t in range(T):
    input()
    x = map(int, raw_input().split())
    xor = 0
    for y in x:
        xor ^= y
    if xor == 0:
        x.sort()
        ans = str(sum(x[1:]))
    else:
        ans = 'NO'
    print 'Case #%d: %s'% (t+1, ans)