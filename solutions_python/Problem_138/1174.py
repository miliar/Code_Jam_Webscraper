T = int(input())
for t in range(1,T+1):
    n = int(input())
    a = list(map(float,input().split()))
    b = list(map(float,input().split()))
    a.sort(reverse=True)
    b.sort()
    L = 0
    R = n - 1
    z = 0
    y = 0
    for i in range(n):
        if a[i] > b[R]:
            z += 1
            L += 1
        else:
            R -= 1
    L = 0 
    R = n - 1
    y = 0
    a.sort()
   # print(*a)
   # print(*b)
    for i in range(n):
        if a[i] < b[L]:
            R -= 1
        else:
            L += 1
            y += 1    
    print('Case #'+str(t)+':', y, z)
        