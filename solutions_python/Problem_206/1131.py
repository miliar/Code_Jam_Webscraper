t = int(input())
j = 0
while(t > 0):
    m , n = map(int,input().split())
    m = int(m)
    n = int(n)
    su = []
    for i in range(n):
        p , q = map(int,input().split())
        p = int(p)
        q = int(q)
        su.append((m - p)/q)
    g = max(su)
    print("Case #%d: %.6f"%(j+1,m / g))
    j+=1
    t-=1
        
