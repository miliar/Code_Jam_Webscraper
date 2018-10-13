k = int(input())
for case in range(k):
    _,b = input().split()
    a = [int(x) for x in b]
    res = 0
    add = 0
    for i in range(len(a)):
        add += max(i-res, 0)
        res += max(i-res, 0)+a[i]
    print("Case #"+str(case+1)+': '+str(add))
