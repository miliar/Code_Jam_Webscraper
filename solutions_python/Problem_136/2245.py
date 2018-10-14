def solve(c, f, x):
    time = 0.0
    acc = 0.0
    rate = 2.0
    
    while 1:
        if acc >= x:
            break
            
        if x < c:
            time = x/rate
            break
        
        if acc < c:
            time += (c-acc)/rate;
            acc = c
        else:
            buy = x/(rate+f)
            nobuy = (x-acc)/rate
            if buy < nobuy:
                rate += f
                acc = 0.0
            else:
                time += nobuy
                acc = x
                
    return time
    
    
templ = "Case #%d: %.8f"
T = int(raw_input())
for t in xrange(1, T+1):
    c, f, x = map(float, raw_input().strip().split())
    ans = solve(c,f,x)
    if t < T:
        print templ %(t, ans)
    else:
        print templ %(t, ans),