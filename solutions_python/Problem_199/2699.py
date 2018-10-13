T = int(input())
i = 0
while i<T:
    i+=1
    s,k = input().split()
    k = int(k)
    w = [ True if e=='+' else False for e in s]
    n = len(w)
    c = 0
    j = 0
    posible = True
    while j<n and posible:
        if not w[j]:
            if j+k-1<n:
                c+=1
                x = 0
                while x<k:
                    w[j+x]=not w[j+x]
                    x+=1
                    pass
                pass
            else:
                posible = False
        j+=1
    print("case #%i: "%i,end="")
    if posible:
        print(c)
    else:
        print("IMPOSSIBLE")
    
