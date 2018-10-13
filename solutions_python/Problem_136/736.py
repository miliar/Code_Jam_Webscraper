def solve(c, f, x):
    now_speed = 2
    ans = 0
    while True:
        t1 = x / now_speed
        t2 = x / (now_speed + f) + c / now_speed
        if t1 < t2:
            ans += t1
            break
        else:
            ans += c / now_speed
            now_speed += f
    return ans
        
T=input()
for t in range(T):
    print "Case #%d: %.12f" % (t+1,solve(*(map(float, raw_input().split()))))

