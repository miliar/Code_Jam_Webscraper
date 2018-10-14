def func(n):
    l = 0
    for x in range(n,0,-1):
        d = []
        val = list(str(x))
        for y in val:
            d.append(y)
        val.sort()
        if val==d:
            l = x
            break
    return l
n = int(input())
nlist = []
for x in range(n):
    value = int(input())
    m = func(value)
    nlist.append(m)
for y in range(n):
    print("Case #"+str(y+1)+": "+str(nlist[y]))
    
