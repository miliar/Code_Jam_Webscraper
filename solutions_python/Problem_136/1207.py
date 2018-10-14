T = int(input())
for t in range(1,T+1):
    c, f, x = map(float,input().split())
    v = 2
    ans = x / v
    cr = 0
    while ans > cr + c / v + x / (v + f):
        ans = cr + c / v + x / (v + f)
        cr += c / v
        v += f
        
        
        
    print('Case #'+str(t)+':', ans)
        