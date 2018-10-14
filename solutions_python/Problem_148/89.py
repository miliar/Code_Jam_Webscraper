def solve(testnum):
    n,x = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    s.sort()
    assert len(s) == n
    i = 0
    i2 = n-1
    num = 0
    while i <= i2:
        if s[i] + s[i2] <= x:
            num += 1; i += 1; i2 -= 1
        else:
            num += 1; i2 -= 1
    print("Case #%d: %d"%(testnum,num))

for i in range(int(input())): solve(i+1)
