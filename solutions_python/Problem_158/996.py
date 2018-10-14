T = int(input())
for t in range(1,T+1):
    x, r, c = map(int,input().split())
    r , c = min(r, c), max(r, c)
    if x == 1:
        ans = 'GABRIEL'
    elif (r * c) % x != 0:
        ans = 'RICHARD'
    elif x == 2:
        ans = 'GABRIEL'
    elif x == 3:
        if r > 1:
            ans = 'GABRIEL'
        else: 
            ans = 'RICHARD'
    else:
        if r > 2:
            ans = 'GABRIEL'
        else:
            ans = 'RICHARD'  
    print('Case #'+str(t)+':', ans)
        