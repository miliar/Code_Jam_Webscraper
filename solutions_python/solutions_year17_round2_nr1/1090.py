t = int(input())

for lol in range(t):
    [d,n] = list(map(int,input().split()))
    h, t = [],[]
    for j in range(n):
        h.append(list(map(int,input().split())))
    for j in range(n):
        t.append((d-h[j][0])/h[j][1])
    s = d/max(t)
    print ("Case #",end="")
    print (lol+1,end="")
    print (":", end = " ")
    print (s)        
        
