def gg(n):
    if (len(n) == 1):
        return n
    k = 1
    while k < len(n):
        if int(n[k - 1]) > int(n[k]):
            r = str(int(n[:k-1] + str(int(n[k-1])-1) + "9"*(len(n)-k)))
            g = gg(r)
            if  g == r:
                return r
            else:
                return g
        k += 1
    return n
t = int(input())
i = 1
while i <= t:
    n = input()
    res = gg(n)
    print("Case #"+str(i)+":",res)
    i+=1